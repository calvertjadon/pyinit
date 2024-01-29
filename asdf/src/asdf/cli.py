import argparse
import sys
from typing import Sequence


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("name", type=str)

    return argument_parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    args = parse_args(argv)
    print(f"Hello, {args.name.title()}!")


if __name__ == "__main__":
    main()
