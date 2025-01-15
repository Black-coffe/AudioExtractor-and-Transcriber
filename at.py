import argparse
import json
import os
import uuid

from atlib.mp42wav import extract_audios_from_video
from atlib.wav2text import transcribe_audio


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audio transcriber")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_mp42wav = subparsers.add_parser("mp42wav", help="Extract audio from video file")
    parser_mp42wav.add_argument("-s", "--source", type=str, help="path to source MP4 file", required=True)
    parser_mp42wav.add_argument("-d", "--destination", type=str, help="path to destination WAV file", required=True)

    parser_wav2text = subparsers.add_parser("wav2text", help="Get raw text transcription from audio file")
    parser_wav2text.add_argument("-s", "--source", type=str, help="path to source WAV file", required=True)
    parser_wav2text.add_argument("-dj", "--destination_json", type=str, default="", help="path to JSON transcription file")
    parser_wav2text.add_argument("-dt", "--destination_text", type=str, help="path to text transcription file", required=True)
    parser_wav2text.add_argument("-m", "--model", type=str, help="path to vosk model directory, e.g. model/vosk-model-ru-0.42, be sure that you have downloaded it", required=True)
    parser_wav2text.add_argument("-e", "--encoding", type=str, default="utf8", help="encoding of final file")

    parser_wav2text = subparsers.add_parser("mp42text", help="Get raw text transcription from MP4 file")
    parser_wav2text.add_argument("-s", "--source", type=str, help="path to source MP4 file", required=True)
    parser_wav2text.add_argument("-dj", "--destination_json", type=str, default="", help="path to JSON transcription file")
    parser_wav2text.add_argument("-dt", "--destination_text", type=str, help="path to text transcription file", required=True)
    parser_wav2text.add_argument("-m", "--model", type=str, help="path to vosk model directory, e.g. model/vosk-model-ru-0.42, be sure that you have downloaded it", required=True)
    parser_wav2text.add_argument("-e", "--encoding", type=str, default="utf8", help="encoding of final file")

    return parser.parse_args()

def main():
    if args.command == "mp42wav":
        extract_audios_from_video(args.source, args.destination)
        print(f"Resulting WAV file saved to {args.destination}")

    elif args.command == "wav2text":
        data = transcribe_audio(args.source, args.model)
        if args.destination_json:
            with open(args.destination_json, "w", encoding=args.encoding) as f:
                f.write(data)
            print(f"Resulting JSON file saved to {args.destination_json}")
        with open(args.destination_text, "w", encoding=args.encoding) as f:
            json_data = json.loads(data)
            f.write(json_data.get("text", ""))
        print(f"Resulting transcription file saved to {args.destination_text}")

    elif args.command == "mp42text":
        tmp_file = f"files/{uuid.uuid4()}.wav"
        extract_audios_from_video(args.source, tmp_file)
        data = transcribe_audio(tmp_file, args.model)
        os.remove(tmp_file)
        if args.destination_json:
            with open(args.destination_json, "w", encoding=args.encoding) as f:
                f.write(data)
            print(f"Resulting JSON file saved to {args.destination_json}")
        with open(args.destination_text, "w", encoding=args.encoding) as f:
            json_data = json.loads(data)
            f.write(json_data.get("text", ""))
        print(f"Resulting transcription file saved to {args.destination_text}")


if __name__ == "__main__":
    args = parse_args()
    main()