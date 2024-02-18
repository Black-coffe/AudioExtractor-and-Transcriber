from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os  # Добавляем импорт модуля os

def extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath):
    """
    Извлекает аудиодорожку из видеофайла, преобразует ее в моно и устанавливает
    частоту дискретизации 16kHz, затем сохраняет в формате WAV.

    Args:
    - video_filepath: Путь к исходному видеофайлу.
    - output_audio_filepath: Путь к выходному аудиофайлу в формате WAV.
    """
    # Загружаем видео и извлекаем аудио как временный файл
    video_clip = VideoFileClip(video_filepath)
    temp_audio_filepath = "temp_audio.mp3"  # Используем временный файл для аудио
    video_clip.audio.write_audiofile(temp_audio_filepath)

    # Используем pydub для конвертации аудио в моно и установки нужной частоты дискретизации
    audio = AudioSegment.from_file(temp_audio_filepath)
    audio = audio.set_channels(1)  # Преобразуем в моно
    audio = audio.set_frame_rate(16000)  # Устанавливаем частоту дискретизации 16kHz

    # Сохраняем обработанное аудио в WAV
    audio.export(output_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"])

    # Удаляем временный аудиофайл
    os.remove(temp_audio_filepath)

# Пример использования функции
video_filepath = 'files/v1.mp4'  # Укажите путь к вашему видеофайлу
output_audio_filepath = 'files/output_audio.wav'  # Укажите, куда сохранить аудиофайл
extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath)
