# Anime editing source example

Snapshot of the accepted 7:31 anime production. All Python editing code is included, including earlier iterations. V3 is the accepted trailer-only opening; V2 contains the original typography opening retained as revision history.

This is project-specific source, not a one-command installer. No footage, narration, model weights, FFmpeg binary, browser credentials or rendered output is included. Source links and timing plans are included for reference, not an enduring claim about future seasons.

## Layout and dependencies

Scripts expect this folder as `anime_fall2026` inside a working media workspace, with `ffmpeg.exe` in its parent and media under `media/`. Local renderers use NVIDIA NVENC; adapt to an available encoder if necessary. Intro graphics use Pillow and Windows Arial. Transcription uses faster-whisper, CUDA libraries and a locally provisioned speech model. ASR output and its derived alignment are runtime inputs and are not bundled. No installation or downloads occur automatically here.

## Relevant code

- `transcribe_v2.py`, `v2/align_script.py`: narration transcription and approximate script alignment.
- `v2/build.py`: chapter/shot plan and title generation for the earlier revision.
- `v2/make_intro.py`: earlier animated opening/outro.
- `v2/render.py`, `v2/verify.py`: rendering and full decoding plus sampled visual review.
- `create_v3.py`: replacement opening montage with unchanged countdown clips; expects the V2 render cache for hard links.
- `v3/update_opening.py`: narrow update of the running FableCut timeline with a backup.
- `v3/render.py`, `v3/verify.py`: current export and verification.

Run only the stage needed for the requested edit, after reading its paths. `save_project.py` replaces an entire live timeline; use the narrow updater for an opening-only revision. Historical `fix_shots.py` and `check_scope.py` are project-specific, not general repair tools. Cached numbered renders must be invalidated when their shot plan changes. Inspect internal trailer cuts, because a plausible source timestamp alone does not guarantee an action matches the narration.
