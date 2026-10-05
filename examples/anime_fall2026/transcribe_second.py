from pathlib import Path
import os, sys, json, time

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
dll_dirs=sorted({str(p.parent) for p in (ROOT/'gpu_tools').rglob('*.dll')})
dll_handles=[os.add_dll_directory(p) for p in dll_dirs]
os.environ['PATH']=os.pathsep.join(dll_dirs+[os.environ.get('PATH','')])
os.environ['HF_HOME'] = str(ROOT / 'models')
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
os.environ['HF_HUB_DISABLE_XET'] = '1'
from faster_whisper import WhisperModel, BatchedInferencePipeline

out = ROOT / 'anime_fall2026' / 'research' / 'second_pass'
out.mkdir(parents=True,exist_ok=True)
print('Loading Hindi transcription model', flush=True)
model = WhisperModel(str(ROOT / 'speech_model_turbo'), device='cuda', compute_type='int8_float16', cpu_threads=8,
                     download_root=str(ROOT / 'models'))
pipeline=BatchedInferencePipeline(model=model)
segments, info = pipeline.transcribe(
    str(ROOT / 'anime_fall2026' / 'media' / 'narration.wav'),
    language='hi', beam_size=5, word_timestamps=True, vad_filter=True, chunk_length=30, batch_size=2,
    initial_prompt='Blue Box, My Happy Marriage, Chitose, Ranma, Pia, Rufus, Noriko, Izark, Koharu, Sota, Roze, Harij, Ramparts of Ice, Koyuki, Firefly Wedding, Satoko, Shinpei, Taiki, Chinatsu।',
    condition_on_previous_text=False)
rate=1.0
rows = []
with (out / 'narration_segments.jsonl').open('w', encoding='utf-8') as f:
    for seg in segments:
        row = {'start':seg.start/rate, 'end':seg.end/rate, 'text':seg.text.strip(),
               'words':[{'start':w.start/rate,'end':w.end/rate,'word':w.word,'probability':w.probability} for w in (seg.words or [])]}
        rows.append(row)
        f.write(json.dumps(row, ensure_ascii=False)+'\n'); f.flush()
        print(f'{seg.end:.1f} / {info.duration:.1f}', flush=True)
(out/'narration_segments.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('TRANSCRIPTION COMPLETE', flush=True)
