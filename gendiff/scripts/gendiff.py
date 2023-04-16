#!/usr/bin/env python3
from gendiff.cli import parse_cli_args
from gendiff import generate_diff


def main():
    path1, path2, format_name = parse_cli_args()
    generate_diff(path1, path2, format_name)


if __name__ == '__main__':
    main()
