#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from docstring_parser import parse


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    parse(fdp.ConsumeUnicodeNoSurrogates(128))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
