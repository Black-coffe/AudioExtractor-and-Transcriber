# Audio-Transcriber

Inspired by https://github.com/Black-coffe/AudioExtractor-and-Transcriber

This repository contains a comprehensive script for handling video to transcribe it into text.
You can do several task by them:
1. Get transcription from video file (mp42text)
2. Extract audio from video file (mp42wav)
3. Get text transcription from audio file (wav2text)

## Features

- **Extract Audio from Video**: Utilizes `moviepy` to extract audio tracks from video files.
- **Process Audio Track**: Leverages `pydub` for audio processing, including conversion to mono and setting the sampling rate to 16kHz.
- **Transcribe Audio to Text**: Employs `vosk`, a powerful tool for speech recognition, to convert audio into text.
- **Text Processing**: Saves the transcribed text and can split it into manageable parts for easier handling.

## Use Cases

This script is ideal for:
- Creating text versions of video lectures and podcasts.
- Automating subtitle creation for videos.
- Extracting meaningful quotes from video content.
- Preparing data for analysis in machine learning projects.

## Technical Requirements

### Libraries and Models

- **moviepy**: For video file manipulation.
- **pydub**: For audio processing tasks. Requires [FFmpeg](https://www.gyan.dev/ffmpeg/builds/#release-builds) for operations like format conversion.
- **vosk**: For accurate speech recognition. You will need to download a model compatible with your audio content's language from [Vosk Models](https://alphacephei.com/vosk/models).

### FFmpeg

FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video. It's required for `pydub` to process audio files. You can download FFmpeg builds from [here](https://www.gyan.dev/ffmpeg/builds/#release-builds).

### Vosk Models

Vosk offers a variety of models that support different languages and are optimized for various audio types. You can download the appropriate model for your project from [Vosk Models](https://alphacephei.com/vosk/models). Ensure to download and specify the correct model path within the script. Save the model to model folders.

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/gs1571/audio-transcriber.git
cd audio-transcriber
pip install -r requirements.txt

```
Additionally, you need to install [FFmpeg](https://www.gyan.dev/ffmpeg/builds/#release-builds). On macOS, you can install FFmpeg using Homebrew:

```bash
brew install ffmpeg
```

### Usage

Use script follow the help information
```
python at.py --help
```
