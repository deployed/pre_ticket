#!/usr/bin/env python

import argparse
import sys

from .tickets import add_ticket_number


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Script that adds ticket number to each commit"
    )
    parser.add_argument("filenames", nargs="+")
    parser.add_argument(
        "--regex", default="(feature|bug|chore)/(?P<ticket>[0-9]+)-.*", type=str
    )
    parser.add_argument("--format", default="{message}\\n\\nRef: #{ticket}", type=str)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    format_template = args.format.encode("utf-8").decode(
        "unicode_escape"
    )  # argparse escapes backslash by default

    add_ticket_number(args.filenames[0], args.regex, format_template)


if __name__ == "__main__":
    sys.exit(main())
