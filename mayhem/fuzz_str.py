#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from docstring_parser import parse, compose


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    doc = parse(fdp.ConsumeUnicodeNoSurrogates(128))
    compose(doc)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
