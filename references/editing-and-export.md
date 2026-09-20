# Editing and export

## FableCut access

- Discover the actual MCP tools, current browser tab, project location and editor manual. A website or connection card is not proof of working MCP access. Do not install a new editor or launch another server when a usable session already exists.
- FableCut may support direct project.json edits with revision increments and live reload. Use that only after reading its installed AGENTS.md / CLAUDE.md. Call this direct project editing, not an MCP operation.
- The established schema uses media entries plus clips with id, mediaId, kind, track, start, in, duration and props. Text overlays are text clips; volume must be explicitly zero on video clips. The current manual takes precedence.
- Keep narration as a single continuous clip. Check separate source-audio clips, muted/solo track state, clip gain and speed. Inventory both imported source assets and distinct sources actually used in the picture edit.
- Verify canvas and **delivery crop** independently. A 1920×1080 canvas with a 9:16 export crop is not a full-width 1080p delivery. Do not carry a stale crop or preview frame-rate setting into the export unnoticed.

## Timing and footage

- Quantize picture cuts to the project frame rate. Prevent gaps, overlaps without intended transitions, out-of-bounds source ranges and subsecond filler flashes.
- Use source sheets for discovery, then inspect a proposed shot's start, middle and end. A contact-sheet thumbnail does not guarantee a ten-second range stays on the same subject.
- Store an EDL with timeline in/out, source file, source in/out and topic. Generate chapter times from the final timeline, not from an earlier script.
- Current-project constraints such as nine videos, 100 points or a 20-minute duration are parameters. Never embed the old GTA chronology or feature claims as verified facts in a future video.

## Local rendering fallback

When the task permits a local export, keep it consistent with the saved editor timeline and disclose the route. Do not claim it used the browser compositor if it did not.

- Reuse available trusted FFmpeg/Python runtimes; inspect before installing large transcription models or GPU dependencies. Do not download gigabytes speculatively.
- Rebuild revised captions from clean source footage, not an earlier export containing burned-in captions.
- Render 1080p with a quality scaler when necessary, keeping caption text at output resolution. Avoid unnecessary encoding generations. Preserve source frame rate unless the user asks otherwise.
- Use a continuous narration master, preferably lossless for intermediate work; encode delivery audio once. Map only that audio stream into a narration-only export. Do not concatenate independently encoded audio for each picture shot.
- Use MP4, H.264, progressive 4:2:0, an appropriate SDR color declaration and AAC-LC at 48 kHz. Use current YouTube guidance for the exact profile, bitrate, GOP and container recommendations. Enable fast start. Verify audio sync if changing edit-list or negative-timestamp handling.
- Do not promise a job completed until the encoder exits successfully and the resulting file has passed inspection. Retain originals and prior deliveries.

## Playback stutter diagnosis

First establish whether stuttering occurs in the browser editor, the exported MP4, the original voice recording, or YouTube playback. Ask for one timestamp or a screenshot while performing independent checks.

For exports, decode the entire file and inspect errors and timestamps. Comparing short-window audio energy against the narration master can detect introduced silence, but cannot prove every word sounds correct or identify YouTube's internal problem. Account for encoder priming and align streams before interpreting a comparison.

For FableCut preview issues, two problems were observed in the original project and locally corrected:

1. Creating/preloading a media element for every inactive cut overloaded preview resources. Instantiate active clips as needed while pausing existing inactive players.
2. Clamping every display-frame elapsed time to 100 ms made the timeline clock fall behind audio during slow frames, triggering repeated corrective seeks. Keep playback elapsed time separate from bounded meter animation time.

These are diagnostic leads, not universal patches. Inspect the installed version, reproduce the applicable behavior, back up code, and modify it only when the current repair task warrants it. Test inactive-player loading and playback across a simulated slow frame. Reload safely and verify the real UI afterward.

## Verification levels

- Timeline check: requested sources present, no unintentional gaps, correct narration length, source audio muted, English captions timed to final audio.
- Export check: real metadata, complete successful decode when warranted, selected frames across chapters including the last second, caption legibility and last spoken sentence.
- Listening/editorial check: speech intelligibility, wording, synchronization, scene relevance and claims. Report explicitly when this has not been completed. A zero-error decode is not a full editorial review.
