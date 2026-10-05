from pathlib import Path
import subprocess,json,io
from PIL import Image,ImageDraw
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parent
FF=R.parent/'ffmpeg.exe'
def board(p):
 j=json.loads(p.read_text(encoding='utf-8')); v=p.with_name(j['id']+'.mp4')
 times=[round(3+(j['duration']-10)*i/11,1) for i in range(12)]
 canvas=Image.new('RGB',(1280,800),'#121826'); d=ImageDraw.Draw(canvas)
 d.text((12,8),j['id']+' | '+j['channel'],fill='white')
 for i,t in enumerate(times):
  b=subprocess.check_output([str(FF),'-v','error','-ss',str(t),'-i',str(v),'-frames:v','1','-vf','scale=320:180','-f','image2pipe','-vcodec','mjpeg','-'])
  canvas.paste(Image.open(io.BytesIO(b)),((i%4)*320,35+(i//4)*250))
  d.text(((i%4)*320+8,220+(i//4)*250),str(t)+'s',fill='white')
 canvas.save(R/'research'/('board_'+j['id']+'.jpg'))
 return j['id']
with ThreadPoolExecutor(max_workers=3) as pool:
 for x in pool.map(board,sorted((R/'media').glob('*.info.json'))):print(x,flush=True)
