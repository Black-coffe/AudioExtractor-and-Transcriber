import os
import tempfile

from moviepy import VideoFileClip
from pydub import AudioSegment


def wav_from_video(src: str, dst: str) -> None:

    # temporary MP3 in the system temp dir, so the script runs from any directory
    fd, temp_audio_filepath = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    try:
        mp3_from_video(src, temp_audio_filepath)

        # use pydub to convert audio to mono and set the desired sampling rate
        audio = AudioSegment.from_file(temp_audio_filepath)
        # switch to mono
        audio = audio.set_channels(1)
        # set sampling rate 16kHz
        audio = audio.set_frame_rate(16000)

        # save result audio to WAV
        audio.export(dst, format="wav", parameters=["-acodec", "pcm_s16le"])
    finally:
        # remove temporary file even if conversion failed
        os.remove(temp_audio_filepath)


def mp3_from_video(src: str, dst: str) -> None:

    with VideoFileClip(src) as video_clip:
        video_clip.audio.write_audiofile(dst)
