from pathlib import Path
import math,json,subprocess
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parent;ROOT=R.parent
P=json.loads((R/'plan.json').read_text(encoding='utf-8'));D=P['chapters'][0]['start'];W,H=1920,1080
fontpath='C:/Windows/Fonts/arialbd.ttf'
fonts={s:ImageFont.truetype(fontpath,s) for s in [24,30,36,42,54,66,78,92,120,164]}
bg=Image.new('RGB',(W,H));pix=bg.load()
for y in range(H):
 for x in range(W):
  g=max(0,1-math.hypot((x-1400)/1500,(y-260)/950));pix[x,y]=(int(15+24*g),int(13+6*g),int(24+19*g))
def txt(d,s,xy,size=78,col='#ffda7b',anchor='mm'):
 d.text(xy,s,font=fonts[size],fill=col,anchor=anchor)
def heart(d,x,y,s,col):
 pts=[]
 for k in range(101):
  a=2*math.pi*k/100;pts.append((x+s*16*math.sin(a)**3/18,y-s*(13*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)-math.cos(4*a))/18))
 d.polygon(pts,fill=col)
cmd=[str(ROOT.parent/'ffmpeg.exe'),'-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-an','-c:v','h264_nvenc','-preset','p4','-qp','18','-pix_fmt','yuv420p',str(ROOT/'media/intro_v2.mp4')]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
bounds=P['intro_bounds']
for frame in range(round(D*30)):
 t=frame/30;im=bg.copy();d=ImageDraw.Draw(im)
 for k in range(22):
  x=(k*137+math.sin(t*.4+k)*28)%W;y=(k*93-t*10)%H
  d.ellipse((x,y,x+3,y+3),fill='#635039')
 d.line((110,110,1810,110),fill='#665137',width=2);txt(d,'REKVON  /  ANIME', (110,77),24,'#e6dfe8','lm')
 idx=sum(t>=b for b in bounds);start=0 if idx==0 else bounds[idx-1]
 ease=1-(1-min(1,(t-start)/.6))**3;dy=int((1-ease)*65)
 if idx==0:
  txt(d,'ONE MESSAGE.',(960,250+dy),120);txt(d,'A THOUSAND WHAT-IFS.',(960,385+dy),78,'#ffffff')
  d.rounded_rectangle((450,530+dy,1470,750+dy),radius=36,fill='#282434',outline='#786251',width=3)
  txt(d,'Hey...',(510,590+dy),54,'#ffffff','lm')
  for k in range(3):
   r=9+int(4*math.sin(t*4+k));x=1320+k*35;d.ellipse((x-r,650+dy-r,x+r,650+dy+r),fill='#ffda7b')
 elif idx==1:
  txt(d,'CAN YOU HELP ME',(960,245+dy),92,'#ffffff');txt(d,'WIN SOMEONE ELSE OVER?',(960,380+dy),92)
  heart(d,960,675+dy,145,'#d95470');d.line([(1000,555+dy),(944,643+dy),(999,681+dy),(924,791+dy)],fill='#201420',width=18)
 elif idx==2:
  txt(d,'LOVE GETS COMPLICATED.',(960,260+dy),92)
  for j,(title,sub,col) in enumerate([('FRIENDSHIP','Unspoken feelings','#c997f0'),('FATE','One different choice','#ffda7b'),('DANGER','Everything at stake','#ef7080')]):
   x=150+j*550;d.rounded_rectangle((x,410+dy,x+520,785+dy),radius=28,fill='#252031',outline=col,width=3)
   heart(d,x+260,510+dy,57,col);txt(d,title,(x+260,635+dy),54,col);txt(d,sub,(x+260,710+dy),30,'#ffffff')
 elif idx==3:
  txt(d,'10',(470,510+dy),164);d.line((655,335+dy,655,745+dy),fill='#ffda7b',width=4)
  txt(d,'ROMANCE STORIES',(1220,410+dy),78,'#ffffff');txt(d,'FIND YOUR NEXT WATCH',(1220,540+dy),54)
  txt(d,'The premise. The mood. Where to start.',(1220,655+dy),36,'#cbc0cf')
 else:
  txt(d,'REKVON',(960,355+dy),164);txt(d,'FALL 2026 WATCHLIST',(960,535+dy),66,'#ffffff')
  txt(d,'Early-season picks • No story spoilers',(960,650+dy),36,'#cfc2d2')
  remain=max(0,D-t);d.rounded_rectangle((590,780,1330,792),radius=6,fill='#413244');d.rounded_rectangle((590,780,590+max(8,740*(1-remain/max(.1,D-start))),792),radius=6,fill='#ffda7b')
 p.stdin.write(im.tobytes())
p.stdin.close();assert p.wait()==0
print('Intro rendered',D,flush=True)
cmd[-1]=str(ROOT/'media/outro_v2.mp4');p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
od=P['duration']-P['outro_start']
for frame in range(round(od*30)):
 t=frame/30;im=bg.copy();d=ImageDraw.Draw(im)
 for k in range(6):heart(d,200+k*310,540+math.sin(t*.7+k)*220,35,'#50304b')
 txt(d,'YOUR #1 PICK?',(960,305),120);txt(d,'Tell us in the comments',(960,455),54,'#ffffff')
 d.line((620,580,1300,580),fill='#ffda7b',width=3)
 txt(d,'REKVON',(960,705),92);txt(d,'MORE ANIME WATCHLISTS',(960,815),36,'#ffffff')
 if t>od-.8:im=Image.blend(im,Image.new('RGB',(W,H)),min(1,(t-od+.8)/.8))
 p.stdin.write(im.tobytes())
p.stdin.close();assert p.wait()==0
print('Outro rendered',flush=True)
