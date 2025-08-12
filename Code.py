import whisper
import os
import subprocess
from moviepy.editor import VideoFileClip

# STEP 1: Paths (Edit this for your video)
video_path = "path"
output_srt = "subtitles.srt"
filename, ext = os.path.splitext(os.path.basename(video_path))
output_video = "video_with_subs.mp4"
output_path = f"{filename}_with_subs.mp4"

# STEP 2: Load Whisper model
print("[INFO] Loading Whisper model...")
model = whisper.load_model("small")  # you can use "base", "small", "medium", "large"

# STEP 3: Transcribe and translate (if needed)
print(f"[INFO] Transcribing {video_path}...")
result = model.transcribe(video_path, task="translate")
segments = result["segments"]

# STEP 4: Save transcription to SRT file
print(f"[INFO] Saving subtitles to {output_srt}...")
with open(output_srt, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        def format_time(seconds):
            h = int(seconds // 3600)
            m = int((seconds % 3600) // 60)
            s = int(seconds % 60)
            ms = int((seconds - int(seconds)) * 1000)
            return f"{h:02}:{m:02}:{s:02},{ms:03}"

        f.write(f"{i+1}\n")
        f.write(f"{format_time(start)} --> {format_time(end)}\n")
        f.write(f"{text}\n\n")

# STEP 5: Burn subtitles using FFmpeg
print(f"[INFO] Adding subtitles to video as {output_video}...")
ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-i", video_path,
    "-vf", f"subtitles={output_srt}",
    "-c:a", "copy",
    output_video
]
subprocess.run(ffmpeg_cmd)

# STEP 6: Play the output video
print("[INFO] Playing video with subtitles...")
clip = VideoFileClip(output_video)
clip.write_videofile(output_path, codec="libx264", audio_codec="aac")


print("\n✅ Done: Transcription + Subtitles added and video played.")

