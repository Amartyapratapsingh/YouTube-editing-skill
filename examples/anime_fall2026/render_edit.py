from pathlib import Path
import subprocess,json
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parent
F=R.parent/'ffmpeg.exe'
P=json.loads((R/'edit_plan.json').read_text())
W=R/'render_work';W.mkdir(exist_ok=True)
def render(arg):
 i,s=arg; out=W/f'{i:03}.mp4'
 if out.exists(): return i
 z=s['zoom'];width=round(1920*z/2)*2;height=round(1080*z/2)*2
 vf=f'crop=iw:trunc(ih*0.88/2)*2:0:0,scale={width}:{height}:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=30,eq=contrast=1.025:saturation=1.025,format=yuv420p'
 cmd=[str(F),'-v','error','-y','-threads','2','-ss',str(s['source']),'-i',str(R/'media'/f"{s['mediaId']}.mp4"),'-an','-vf',vf,'-frames:v',str(round(s['duration']*30)),'-c:v','h264_nvenc','-preset','p4','-rc','constqp','-qp','19','-g','60','-video_track_timescale','15360',str(out)]
 p=subprocess.run(cmd,capture_output=True)
 if p.returncode: raise RuntimeError(p.stderr.decode(errors='replace'))
 return i
with ThreadPoolExecutor(max_workers=2) as pool:
 for i in pool.map(render,enumerate(P['shots'])):
  if i%10==0:print('Rendered shot',i+1,'/',len(P['shots']),flush=True)
(W/'concat.txt').write_text('\n'.join(f"file '{i:03}.mp4'" for i in range(len(P['shots']))))
cmd=[str(F),'-v','warning','-y','-f','concat','-safe','0','-i',str(W/'concat.txt'),'-i',str(R/'media/narration.wav'),'-vf','drawbox=x=0:y=0:w=iw:h=144:color=black:t=fill,drawbox=x=0:y=936:w=iw:h=144:color=black:t=fill,ass=highlights.ass','-map','0:v:0','-map','1:a:0','-c:v','h264_nvenc','-preset','p5','-rc','vbr','-cq','19','-b:v','8M','-maxrate','14M','-bufsize','28M','-g','60','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','192k','-ar','48000','-af','apad=pad_dur=1','-t',str(P['duration']),'-movflags','+faststart',str(R/'exports/Rekvon_Fall2026_Romance_Top10_review_v1.mp4')]
print('Rendering titles and continuous audio',flush=True)
subprocess.run(cmd,cwd=R,check=True)
print('EXPORT COMPLETE',flush=True)
