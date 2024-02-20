import ply.lex as lex
import sys

reserved = (
    "TR", "tr",
    "FL", "fl",
    "NULL", "null"
)

tokens = (
    "ENT",
    "REAL",
    "NCIENT",
    "BIN",
    "OCT",
    "HEX",
    "CADENA",
    "COMILLAS",
    "LT",
    "LE",
    "EQ",
    "GE",
    "GT",
    "LBRACKET",
    "RBRACKET",
    "COMA",
    "ASIGNACION"
) + reserved

t_ignore = ' \t\n'

def t_newline(token):
    r'\n+'
    token.lexer.lineno = token.value.count('\n')

t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'=>'
t_EQ = r'=='
t_COMA = r','
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ASIGNACION = r':'

t_CADENA = r'[a-zA-Z_][0-9a-zA-Z_]*'
t_COMILLAS = r'^\"[^"]*\"$'

def t_REAL(token):
    r'\-?[0-9]*\.[0-9]*'
    token.value = float(token.value) 
    return token

def t_ENT(token):
    r'\-?[1-9][0-9]*'  
    token.value = int(token.value)
    return token

def t_error(token):
    # imprime información sobre el error
    print("[Ex1][Lexer] Illegal character", token.value)
    # se salta la linea del error
    token.lexer.skip(1)

lexer = lex.lex()

# input para el lexer
lexer.input('.9')
for token in lexer:
    print(token.type, token.value)