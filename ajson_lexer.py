import sys
import ply.lex as lex

""" Reconocedor léxico. """
# Palabras reservadas
reserved = (
    "NULL", "null",
    "TR", "tr", 
    "FL", "fl"
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
    "NULO",
    "BOOL"
) + reserved

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
t_CADENASIN = r'[A-Z_][A-Za-z0-9_]*'

def t_REAL(t):
    r'-?\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NCIENT(t):
    r'-?\d+(e|E)-?\d+'
    t.value = float(t.value)
    return t

def t_BIN(t):
    r'(0b|OB)[01]+'
    t.value = int(t.value, 2)
    return t

def t_OCT(t):
    r'0[0-7]+'
    t.value = int(t.value, 8)
    return t

def t_HEX(t):
    r'(0x|0X)[0-9A-F]+'
    t.value = int(t.value, 16)
    return t

def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_CADENACON(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

def t_NULO(t):
    r'NULL|null'
    t.type = "NULO"
    return t

def t_BOOL(t):
    r'FL|fl|TR|tr'
    t.type = "BOOL"
    return t

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = " \t\n"

# Manejo de errores
def t_error(token):
    print("Caracter ilegal", token.value)
    token.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno = t.value.count('\n')

"""Leer el fichero de entrada y ejecutar el analizador."""
lexer = lex.lex()
file = open(sys.argv[1], "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)