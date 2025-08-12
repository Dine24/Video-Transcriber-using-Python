# 🎥 Multilingual Video Transcriber & Subtitle Generator

An end-to-end Python tool that:
- Automatically **transcribes video/audio** files in **any spoken language**
- **Translates** non-English speech into **English**
- **Generates .srt subtitles**
- **Burns subtitles** into the video using FFmpeg
- Enables playback **within Google Colab** or download for local viewing

---

## 🔧 Technologies Used
- [OpenAI Whisper](https://github.com/openai/whisper) – speech-to-text & translation
- `ffmpeg-python` & FFmpeg CLI – video and subtitle processing
- `Google Colab` – hosted execution and file interface
- Python Libraries: `whisper`, `moviepy`, `IPython`, `base64`, `os`, `subprocess`

---


---


---

## ✅ Features

- 🎙️ Supports **MP4**, **MP3**, and other audio/video formats
- 🌍 **Auto language detection** + **translation to English**
- 📝 Accurate **.srt subtitle generation** with timecodes
- 🔥 **Hardcoded subtitles** using FFmpeg
- ▶️ **Plays video with subs** directly in Colab
- 📦 Option to **download output** or ZIP

---

## 🛠️ How to Use

1. **Upload your video/audio** file in Google Colab
2. **Run the transcription cell**
3. **Subtitles (.srt)** will be auto-generated
4. Subtitles are **burned into the video** using FFmpeg
5. Play video inline or **download output**

---

## 🖥️ Example Output

```srt
1
00:00:00,000 --> 00:00:03,210
Welcome to the future of video translation.

2
00:00:03,210 --> 00:00:06,000
This video was originally in Hindi.
