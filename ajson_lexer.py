import sys
import ply.lex as lex
import ply.yacc as yacc

""" Reconocedor léxico. """
class LexerClass:
    # Palabras reservadas
    reserved = (
        "NULL",
        "TR", 
        "FL"
    )

    # Tokens
    tokens = (
        "INT", 
        "REAL",
        "NCIENT",
        "BIN",
        "OCT",
        "HEX",
        "CADENASIN",
        "CADENACON",
        "EQ",
        "LT",
        "GT",
        "LE",
        "GE",
        "LLAVEA",
        "LLAVEC",
        "PUNTOS",
        "COMA",
    ) + reserved

    reserved_map = {}
    for r in reserved:
        reserved_map[r.lower()] = r
        reserved_map[r.upper()] = r

    def __init__(self):
        self.lexer = lex.lex(module = self)
        self.reserved_map = LexerClass.reserved_map

    # Ignorar espacios, tabulaciones y saltos de línea
    t_ignore = " \t\n"

    # Expresiones regulares
    t_EQ = r'=='
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='
    t_LLAVEA = r'\{'
    t_LLAVEC = r'\}'
    t_PUNTOS = r':'
    t_COMA = r','

    def t_REAL(self, t):
        r'-?\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_NCIENT(self, t):
        r'-?\d+(e|E)-?\d+'
        t.value = float(t.value)
        return t

    def t_BIN(self, t):
        r'(0b|OB)[01]+'
        t.value = int(t.value, 2)
        return t

    def t_OCT(self, t):
        r'0[0-7]+'
        t.value = int(t.value, 8)
        return t

    def t_HEX(self, t):
        r'(0x|0X)[0-9A-F]+'
        t.value = int(t.value, 16)
        return t

    def t_INT(self, t):
        r'-?\d+'
        t.value = int(t.value)
        return t

    def t_CADENACON(self, t):
        r'"[^"\n]*"'
        t.value = t.value[1:-1]
        return t

    def t_CADENASIN(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved_map.get(t.value, "CADENASIN")
        return t

    def t_error(self, token):
        print("Caracter ilegal", token.value)
        token.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)
    
    def test_with_files(self, path):
        file = open(path)
        content = file.readlines()
        for line in content:
            self.test(line)

