#!/usr/bin/env python3
import argparse
import json
from gendiff.cli import parse_cli_args
from gendiff.scripts.generate_difference import generate_diff

def main():
    path1, path2 = parse_cli_args()
    generate_diff(path1, path2)


if __name__ == '__main__':
    main()