from pathlib import Path

def read_input_file(fpath: Path):
    print(fpath.absolute())
    with open(fpath) as f:
        lines = f.readlines()
    lines = [lin.strip() for lin in lines]

    return lines