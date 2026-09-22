import math
import wave

from tqdm import tqdm
from vosk import KaldiRecognizer, Model


def transcribe_audio(src: str, model_path: str) -> str:
    model = Model(model_path)
    with wave.open(src, "rb") as wf:
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)  # to get words instead of simple results

        step = 4000
        # round up so the last partial chunk is read too
        chunks = math.ceil(wf.getnframes() / step)

        for _ in tqdm(range(chunks), desc="Audio to text processing"):
            data = wf.readframes(step)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

    # final result
    return rec.FinalResult()
