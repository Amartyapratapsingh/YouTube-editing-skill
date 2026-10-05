from pathlib import Path
import json,shutil,os
root=Path(__file__).resolve().parent
old=root/'v2'; new=root/'v3';new.mkdir(exist_ok=True)
p=json.loads((old/'plan.json').read_text(encoding='utf-8'))
# 48.1-second trailer montage. Windows selected from the reviewed source boards.
windows=[('8XgKVzuLmJw',25,2.7),('sWvfeHOkAOU',14,2.7),
 ('nvWCcqdBycQ',36,3),('nvWCcqdBycQ',54,3),
 ('8RHh2AyKRfY',63,3),('dXeAqvXkSUM',26,3),('kLfQNqd_NA0',31,3),
 ('dLRKywRu3iM',24,2.5),('CeUZpSuOuS4',24,2.2),('7fXK-8PHGL0',76,2.5),
 ('n0ugKku1fzc',88,2.5),('8XgKVzuLmJw',38,2.5),('sWvfeHOkAOU',51,2.5),
 ('dLRKywRu3iM',76,2.5),('8RHh2AyKRfY',98,2.5),('CeUZpSuOuS4',39,2.5),
 ('7fXK-8PHGL0',82,2.5),('n0ugKku1fzc',44,2),('dXeAqvXkSUM',23,1)]
t=0;shots=[]
for i,(mid,src,d) in enumerate(windows):
 if i==len(windows)-1:d=48.1-t
 shots.append(dict(start=round(t*30)/30,duration=round(d*30)/30,mediaId=mid,source=src,zoom=1,reason='Opening trailer montage — no added text'))
 t+=d
assert abs(t-48.1)<.01
rest=[s for s in p['shots'] if s['start']>=48.1-.001]
shots+=rest
p['shots']=shots
(new/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(old/'highlights.ass',new/'highlights.ass')
w=new/'render_work';w.mkdir(exist_ok=True)
for j,s in enumerate(rest,start=len(windows)):
 i=next(i for i,a in enumerate(json.loads((old/'plan.json').read_text(encoding='utf-8'))['shots']) if a==s)
 dest=w/f'{j:03}.mp4'
 if not dest.exists():os.link(old/'render_work'/f'{i:03}.mp4',dest)
render=(old/'render.py').read_text().replace('Top10_v2.mp4','Top10_v3.mp4')
(new/'render.py').write_text(render)
save=(old/'save_project.py').read_text(encoding='utf-8').replace("'Rekvon — Romance Anime V2 — Hindi Narration'","'Rekvon — Romance Anime V3 — Trailer Opening'").replace("'project_v2.json'","'project_v3.json'")
save=save.replace("start=P['chapters'][0]['start'],duration=P['outro_start']-P['chapters'][0]['start']","start=0,duration=P['outro_start']")
(new/'save_project.py').write_text(save,encoding='utf-8')
(new/'research').mkdir(exist_ok=True)
verify=(old/'verify.py').read_text().replace('Top10_v2.mp4','Top10_v3.mp4').replace('times=[3,8,26,38,49.5,89.5,128.5,164,169,202,238,278,316,353,390,399,401.7,444]','times=[1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49.5,444]')
(new/'verify.py').write_text(verify)
print('Opening shots',len(windows),'Total shots',len(shots))
