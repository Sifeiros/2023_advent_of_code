from pathlib import Path

def read_input_file(fpath: Path):
    print(fpath.absolute())
    with open(fpath) as f:
        lines = f.readlines()

    return lines