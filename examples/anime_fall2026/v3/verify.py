from pathlib import Path
import json,subprocess,io
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;F=R.parent.parent/'ffmpeg.exe';V=R.parent/'exports/Rekvon_Fall2026_Romance_Top10_v3.mp4'
p=json.loads((R/'plan.json').read_text(encoding='utf-8'))
issues=[]
for a,b in zip(p['shots'],p['shots'][1:]):
 if abs(a['start']+a['duration']-b['start'])>0.04:issues.append(['gap',a,b])
q=subprocess.run([str(F),'-v','error','-i',str(V),'-f','null','NUL'],capture_output=True)
meta=subprocess.run([str(F),'-hide_banner','-i',str(V)],capture_output=True).stderr.decode(errors='replace')
(R/'research/export_metadata.txt').write_text(meta,encoding='utf-8')
(R/'research/qa.json').write_text(json.dumps({'decode_exit_code':q.returncode,'decode_errors':q.stderr.decode(errors='replace'),'timeline_issues':issues,'file_bytes':V.stat().st_size,'duration_planned':p['duration'],'shots':len(p['shots']),'source_video_count':10,'source_audio_in_export':False,'full_listening_review':False},indent=2))
times=[1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49.5,444]
for group in range(3):
 subset=times[group*6:group*6+6]
 im=Image.new('RGB',(1280,3*390),'#121826');d=ImageDraw.Draw(im)
 for i,t in enumerate(subset):
  b=subprocess.check_output([str(F),'-v','error','-ss',str(t),'-i',str(V),'-frames:v','1','-vf','scale=640:360','-f','image2pipe','-vcodec','mjpeg','-'])
  im.paste(Image.open(io.BytesIO(b)),((i%2)*640,(i//2)*390));d.text(((i%2)*640+12,(i//2)*390+365),str(t)+' seconds',fill='white')
 im.save(R/'research'/f'export_review_{group+1}.jpg')
print('Decode:',q.returncode,'Timeline issues:',len(issues),flush=True)
