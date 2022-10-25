#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from docstring_parser import rest, parser, DocstringStyle, RenderingStyle, ParseError

file_types = [DocstringStyle.REST, DocstringStyle.GOOGLE, DocstringStyle.NUMPYDOC, DocstringStyle.EPYDOC]
rendering_style = [RenderingStyle.COMPACT, RenderingStyle.CLEAN, RenderingStyle.EXPANDED]
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    try:
        doc = parser.parse(fdp.ConsumeUnicodeNoSurrogates(128), fdp.PickValueInList(file_types))
        parser.compose(doc, fdp.PickValueInList(file_types), fdp.PickValueInList(rendering_style))

    except (ParseError, IndexError):
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
