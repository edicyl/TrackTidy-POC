# 🎵 TrackTidy - A Terminal-Based DJ Music Manager

TrackTidy is a **command-line tool** for managing your music files. It allows you to:
- ✅ **Edit metadata** (song title, artist, album, track number)
- ✅ **Convert audio files** between formats (MP3, WAV, FLAC, AAC, OGG)
- ✅ **Fetch and apply cover art** (coming soon!)

---

## 📦 Installation

### 1️⃣ Install Dependencies
Make sure you have **Python 3.10+** installed. Then install the required libraries:

```sh
pip install rich mutagen
```

### 2️⃣ Install FFmpeg
TrackTidy uses **FFmpeg** for audio conversion. Install it:

- **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to `PATH`.
- **Linux (Ubuntu/Debian)**:
  ```sh
  sudo apt install ffmpeg
  ```
- **Mac (Homebrew)**:
  ```sh
  brew install ffmpeg
  ```

---

## 🚀 Usage

### Convert an Audio File
```sh
python audio_converter.py
```
- Enter the path to your audio file.
- Choose an output format (MP3, WAV, FLAC, AAC, OGG).
- TrackTidy will display a **real-time progress bar** while converting.

### Edit Metadata
```sh
python metadata_editor.py
```
- View existing metadata.
- Edit **title, artist, album, track number** interactively.

---

## 🛠 Features in Development
- 🎨 **Cover Art Fetching & Management**
- 📁 **Batch Processing for Bulk Conversions**
- 🔍 **Automatic Audio File Organization**

---

## 📜 License
TrackTidy is an open-source project. Feel free to modify and contribute!

---
