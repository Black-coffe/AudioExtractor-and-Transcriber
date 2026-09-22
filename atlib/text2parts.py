from pathlib import Path


def split_text_into_files(src: str, chunk_size: int, encoding: str = "utf8") -> list[str]:
    text = Path(src).read_text(encoding=encoding)
    base = Path(src).with_suffix("")

    paths = []
    for i in range(0, len(text), chunk_size):
        part = Path(f"{base}_part_{i // chunk_size + 1}.txt")
        part.write_text(text[i:i + chunk_size], encoding=encoding)
        paths.append(str(part))
    return paths
