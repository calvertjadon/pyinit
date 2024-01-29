import argparse
import sys
import venv
from pathlib import Path
from typing import Sequence

from pyinit.project import Project
from pyinit.res import Resources

VENV_NAME = ".venv"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("path", type=Path)
    argument_parser.add_argument("--venv", "-v", action="store_true", required=False)

    return argument_parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    args = parse_args(argv)
    res = Resources()

    project = Project(args.path, res)
    project.initialize()

    if args.venv:
        venv_path = project.path / VENV_NAME
        venv.create(str(venv_path))
        print(f"created virtual environment at {venv_path}")


if __name__ == "__main__":
    main()
