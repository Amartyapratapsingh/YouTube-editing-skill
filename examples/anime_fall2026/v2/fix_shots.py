from pathlib import Path
import json
r=Path('anime_fall2026/v2');p=json.loads((r/'plan.json').read_text(encoding='utf-8'))
for i,s in enumerate(p['shots']):
 if (s['start'] <= 399 < s['start']+s['duration']) or (s['start'] <= 278 < s['start']+s['duration']):
  s['source']=44 if s['mediaId']=='n0ugKku1fzc' else 31
  f=r/'render_work'/f'{i:03}.mp4'
  if f.exists():f.rename(f.with_suffix('.before_fix.mp4'))
  print(i,s['start'],s['duration'],s['source'])
(r/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
