from pathlib import Path
import json,subprocess
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parent;ROOT=R.parent;F=ROOT.parent/'ffmpeg.exe'
P=json.loads((R/'plan.json').read_text(encoding='utf-8'));W=R/'render_work';W.mkdir(exist_ok=True)
def render(arg):
 i,s=arg;out=W/f'{i:03}.mp4'
 if out.exists():return i
 native=s['mediaId'] in ['intro_v2','outro_v2'];frames=round(s['duration']*30)
 vf='scale=1920:1080,setsar=1,fps=30' if native else 'crop=iw:trunc(ih*0.88/2)*2:0:0,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=30,eq=contrast=1.025:saturation=1.025'
 if not native and s['zoom']>1:vf+=f",zoompan=z='1+0.018*on/{frames}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1920x1080:fps=30"
 if not native:vf+=',drawbox=x=0:y=0:w=iw:h=144:color=black:t=fill,drawbox=x=0:y=936:w=iw:h=144:color=black:t=fill'
 cmd=[str(F),'-v','error','-y','-threads','2','-ss',str(s['source']),'-i',str(ROOT/'media'/f"{s['mediaId']}.mp4"),'-an','-vf',vf,'-frames:v',str(frames),'-c:v','h264_nvenc','-preset','p4','-rc','constqp','-qp','19','-g','60','-pix_fmt','yuv420p','-video_track_timescale','15360',str(out)]
 p=subprocess.run(cmd,capture_output=True)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
 return i
with ThreadPoolExecutor(max_workers=2) as pool:
 for i in pool.map(render,enumerate(P['shots'])):
  if i%15==0:print('Rendered',i+1,'/',len(P['shots']),flush=True)
(W/'concat.txt').write_text('\n'.join(f"file '{i:03}.mp4'" for i in range(len(P['shots']))))
print('Rendering final titles and narration',flush=True)
subprocess.run([str(F),'-v','warning','-y','-f','concat','-safe','0','-i',str(W/'concat.txt'),'-i',str(ROOT/'media/narration_v2.wav'),'-vf','ass=highlights.ass','-map','0:v:0','-map','1:a:0','-c:v','h264_nvenc','-preset','p5','-rc','vbr','-cq','19','-b:v','8M','-maxrate','14M','-bufsize','28M','-g','60','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','192k','-ar','48000','-af','apad=pad_dur=1','-t',str(P['duration']),'-movflags','+faststart',str(ROOT/'exports/Rekvon_Fall2026_Romance_Top10_v2.mp4')],cwd=R,check=True)
print('V2 EXPORT COMPLETE',flush=True)
