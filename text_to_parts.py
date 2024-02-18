import json

def extract_text_from_json(input_file):
    encodings = ['windows-1251']  # Try different encodings
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                data = json.load(f)
            break
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
    else:
        raise ValueError("Unable to decode the file with any of the specified encodings or parse JSON")

    text = data.get("text", "")
    return text

def split_text_into_files(text, chunk_size):
    total_length = len(text)
    num_chunks = (total_length + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        chunk = text[start:end]

        output_filename = f"part_{i + 1}.txt"
        with open(output_filename, 'w', encoding='utf-8') as out_f:
            out_f.write(chunk)

if __name__ == "__main__":
    input_file = "files/transcribed_text.txt"
    chunk_size = 4000
    text = extract_text_from_json(input_file)
    split_text_into_files(text, chunk_size)
