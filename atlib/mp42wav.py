import os
import uuid

from moviepy import VideoFileClip
from pydub import AudioSegment


def extract_audios_from_video(src: str, dst: str) -> None:

    video_clip = VideoFileClip(src)
    temp_audio_filepath = f"files/{uuid.uuid4()}.mp3"  # use temporary file to store MP3
    video_clip.audio.write_audiofile(temp_audio_filepath)

    # use pydub to convert audio to mono and set the desired sampling rate
    audio = AudioSegment.from_file(temp_audio_filepath)
    # switch to mono
    audio = audio.set_channels(1)
    # set sampling rate 16kHz
    audio = audio.set_frame_rate(16000)

    # save result audio to WAV
    audio.export(dst, format="wav", parameters=["-acodec", "pcm_s16le"])

    # remove temporary file
    os.remove(temp_audio_filepath)
