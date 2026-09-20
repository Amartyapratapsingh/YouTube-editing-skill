# Upload and processing diagnosis

Ask for the exact message, elapsed time and uploaded filename (or screenshot). Begin local checks without waiting when the intended file is clear. Do not infer the Studio stage from the HD icon alone.

## Read the status precisely

- Uploading: bytes are still being transferred; file size, bandwidth and interruptions matter.
- Processing SD/HD: YouTube is converting the uploaded file. HD may take substantially longer than SD.
- Copyright, monetization or initial checks: separate from basic video transcoding.
- "Taking longer than expected. Please wait": a delay message, not proof of a failed upload or corrupted file.
- "Processing abandoned" or an explicit error: record the exact text and follow current official troubleshooting guidance.

Use current YouTube Help, including:

- https://support.google.com/youtube/answer/1722171 — recommended encoding settings
- https://support.google.com/youtube/answer/58134 — audio/video troubleshooting and HD processing
- https://support.google.com/youtube/answer/4525858 — slow or stuck uploads

## Check the file

Verify the file the user actually uploaded; they may have renamed it or exported another copy. Inspect size, duration, dimensions, frame rate, codec/profile, pixel/color format, audio codec/sample rate, stream count and timestamps. Check fast-start/container structure when relevant.

A bounded full decode with an existing trusted FFmpeg binary is useful:

```text
ffmpeg -hide_banner -v warning -xerror -i INPUT.mp4 -map 0:v:0 -map 0:a:0 -f null -
```

Use structured process arguments or proper shell quoting; capture the exit code and error log. This example assumes the video has an audio stream. Do not use -t 0 and claim the whole video was checked: that only inspects the header/startup path.

A clean decode means no corruption was detected by that test, not that every YouTube recommendation is met. For example, a Main-profile H.264 file may decode correctly while differing from a recommended High-profile setting. MP4 timing edit lists also deserve inspection if processing repeatedly fails, because YouTube recommends avoiding them. Neither observation establishes causation by itself.

Avoid dumping trace output: MP4 sample tables can produce hundreds of thousands of lines. Prefer structured probing or narrowly bounded parsing for individual atoms/timing fields.

## Respond and act proportionately

If the file decodes cleanly and Studio only reports slow processing, explain the result and recommend keeping the upload while it processes. Do not promise a completion time or call it a confirmed YouTube outage without evidence. A private saved upload can remain private while the user finishes metadata.

If the upload explicitly fails or remains stalled beyond the official guidance, identify concrete incompatibilities and prepare a separately named compatible copy if warranted. Preserve the original; verify duration and audio sync after any remux or transcode. Do not recommend repeated blind re-uploads, downgrade resolution against the user's preference, or delete/publish the current upload without authorization.
