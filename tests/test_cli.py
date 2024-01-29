from pathlib import Path

from pyinit.cli import parse_args


def test_parse_args():
    argv = ["/home/test/my-project", "--venv"]
    args = parse_args(argv)
    assert args.path == Path(argv[0])
    assert args.venv == True
