#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    import docstring_parser as dp

file_types = [dp.DocstringStyle.REST, dp.DocstringStyle.GOOGLE, dp.DocstringStyle.NUMPYDOC, dp.DocstringStyle.EPYDOC]
rendering_style = [dp.RenderingStyle.COMPACT, dp.RenderingStyle.CLEAN, dp.RenderingStyle.EXPANDED]

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    try:
        doc = dp.parser.parse(fdp.ConsumeUnicodeNoSurrogates(4096), fdp.PickValueInList(file_types))
        dp.parser.compose(doc, fdp.PickValueInList(file_types), fdp.PickValueInList(rendering_style))
    except dp.ParseError:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
