import ply.lex as lex
import ply.yacc as yacc
import sys
from ajson_lexer import LexerClass
from ajson_parser import ParserClass

p = ParserClass()
print("Fichero " + str(sys.argv[1]))
p.test_with_files(sys.argv[1])