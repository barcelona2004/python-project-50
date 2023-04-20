#!/usr/bin/env python3
from gendiff.cli import parse_cli_args
from gendiff import generate_diff
import os


def main():
    path1, path2, format_name = parse_cli_args()
    path11 = os.path.abspath(path1)
    path22 = os.path.abspath(path2)
    print(generate_diff(path11, path22, format_name))


if __name__ == '__main__':
    main()
