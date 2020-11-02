import sys
from antlr4 import *
from gen.BCCLexer import BCCLexer
from gen.BCCParser import BCCParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = BCCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BCCParser(stream)
    tree = parser.prog()

if __name__ == '__main__':
    main(sys.argv)