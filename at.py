import argparse
import json
import os
import uuid
from pathlib import Path

from atlib.mp42wav import wav_from_video, mp3_from_video
from atlib.wav2text import transcribe_audio


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audio transcriber")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_mp42wav = subparsers.add_parser("mp42wav", help="Extract audio from video file and save to WAV")
    parser_mp42wav.add_argument("-s", "--source", type=str, help="path to source MP4 file", required=True)
    parser_mp42wav.add_argument("-d", "--destination", type=str, help="path to destination WAV file, if absent use source path with .wav extension", default="")

    parser_mp42mp3 = subparsers.add_parser("mp42mp3", help="Extract audio from video file and save to MP3")
    parser_mp42mp3.add_argument("-s", "--source", type=str, help="path to source MP4 file", required=True)
    parser_mp42mp3.add_argument("-d", "--destination", type=str, help="path to destination MP3 file, if absent use source path with .mp3 extension", default="")

    parser_wav2text = subparsers.add_parser("wav2text", help="Get raw text transcription from audio file")
    parser_wav2text.add_argument("-s", "--source", type=str, help="path to source WAV file", required=True)
    parser_wav2text.add_argument("-dj", "--destination_json", type=str, default="", help="path to JSON transcription file")
    parser_wav2text.add_argument("-dt", "--destination_text", type=str, help="path to text transcription file, if absent use source path with .txt extension", default="")
    parser_wav2text.add_argument("-m", "--model", type=str, help="path to vosk model directory, e.g. model/vosk-model-ru-0.42, be sure that you have downloaded it", required=True)
    parser_wav2text.add_argument("-e", "--encoding", type=str, default="utf8", help="encoding of final file")

    parser_mp42text = subparsers.add_parser("mp42text", help="Get raw text transcription from MP4 file")
    parser_mp42text.add_argument("-s", "--source", type=str, help="path to source MP4 file", required=True)
    parser_mp42text.add_argument("-dj", "--destination_json", type=str, default="", help="path to JSON transcription file")
    parser_mp42text.add_argument("-dt", "--destination_text", type=str, help="path to text transcription file, if absent use source path with .txt extension", default="")
    parser_mp42text.add_argument("-m", "--model", type=str, help="path to vosk model directory, e.g. model/vosk-model-ru-0.42, be sure that you have downloaded it", required=True)
    parser_mp42text.add_argument("-e", "--encoding", type=str, default="utf8", help="encoding of final file")

    return parser.parse_args()

def main():
    if args.command == "mp42wav":
        if not args.destination:
            destination = str(Path(args.source).with_suffix('.wav'))
        else:
            destination = args.destination
        wav_from_video(args.source, destination)
        print(f"Resulting WAV file saved to {destination}")

    elif args.command == "mp42mp3":
        if not args.destination:
            destination = str(Path(args.source).with_suffix('.mp3'))
        else:
            destination = args.destination
        mp3_from_video(args.source, destination)
        print(f"Resulting MP3 file saved to {destination}")

    elif args.command == "wav2text":
        data = transcribe_audio(args.source, args.model)
        if args.destination_json:
            with open(args.destination_json, "w", encoding=args.encoding) as f:
                f.write(data)
            print(f"Resulting JSON file saved to {args.destination_json}")
        if not args.destination_text:
            destination_text = str(Path(args.source).with_suffix('.txt'))
        else:
            destination_text = args.destination_text

        with open(destination_text, "w", encoding=args.encoding) as f:
            json_data = json.loads(data)
            f.write(json_data.get("text", ""))
        print(f"Resulting transcription file saved to {destination_text}")

    elif args.command == "mp42text":
        tmp_file = f"files/{uuid.uuid4()}.wav"
        wav_from_video(args.source, tmp_file)
        data = transcribe_audio(tmp_file, args.model)
        os.remove(tmp_file)
        if args.destination_json:
            with open(args.destination_json, "w", encoding=args.encoding) as f:
                f.write(data)
            print(f"Resulting JSON file saved to {args.destination_json}")

        if not args.destination_text:
            destination_text = str(Path(args.source).with_suffix('.txt'))
        else:
            destination_text = args.destination_text

        with open(destination_text, "w", encoding=args.encoding) as f:
            json_data = json.loads(data)
            f.write(json_data.get("text", ""))
        print(f"Resulting transcription file saved to {destination_text}")


if __name__ == "__main__":
    args = parse_args()
    main()