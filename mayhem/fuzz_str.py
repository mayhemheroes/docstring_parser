#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from docstring_parser import rest, parser

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    doc = parser.parse(fdp.ConsumeUnicodeNoSurrogates(128))
    parser.compose(doc)

    doc2 = rest.parse(fdp.ConsumeUnicodeNoSurrogates(128))
    rest.compose(doc2)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
