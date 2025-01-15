import wave

from tqdm import tqdm
from vosk import KaldiRecognizer, Model


def transcribe_audio(src: str, model_path: str) -> str:
    # Read WAV file
    wf = wave.open(src, "rb")
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)  # to get words instead of simple results

    total_frames = wf.getnframes()
    step = 4000

    for _ in tqdm(range(int(total_frames/step)), desc="Audio to text processing"):
        data = wf.readframes(step)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    # final result
    result = rec.FinalResult()
    return result
