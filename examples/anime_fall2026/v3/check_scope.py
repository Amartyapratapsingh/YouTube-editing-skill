from pathlib import Path
import json
r=Path('anime_fall2026/v3');p=json.loads((r/'plan.json').read_text(encoding='utf-8'))
bad=[]
for c in p['chapters']:
 for s in p['shots']:
  if c['start']<=s['start']<c['end']-.01 and s['mediaId']!=c['mediaId']:bad.append(s['start'])
print('Wrong-anime shots inside countdown:',bad)
print('Added intro text cues:',[c for c in p['cues'] if c['start']<48.1])
(r/'README.txt').write_text('V3: original text-based opening replaced with 19 selected trailer excerpts covering all ten anime. No added opening text. Countdown footage remains within its corresponding anime entry. Existing narration and 7:31 duration preserved. 1920x1080, 30fps. Rendered locally with FFmpeg; corresponding FableCut project saved as project_v3.json. Keep the media folder with that project. Prior V2 preserved. Full listening review remains pending.',encoding='utf-8')
