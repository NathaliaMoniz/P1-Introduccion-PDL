import sys
import ply.lex as lex
import ply.yacc as yacc
""" Reconocedor léxico. """
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

def t_CADENASIN(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_map.get(t.value, "CADENASIN")
    return t

# Manejo de errores
def t_error(token):
    print("Caracter ilegal", token.value)
    token.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno = t.value.count('\n')

"""Leer el fichero de entrada y ejecutar el analizador."""
lexer = lex.lex()
"""file = open(sys.argv[1], "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)
"""

"""
Simbolos terminales: INT REAL NCIENT BIN OCT HEX == >= <= > < : , ¿...??
Simbolos no terminales: axioma asignacion

"""



def p_axioma(p):
    ''' axioma : LLAVEA contenido LLAVEC 
               | LLAVEA LLAVEC'''
    
    if len(p) == 4:
        p[0] = p[2]
        print(p[1], p[2], p[3])
    elif(len(p)==3):
        p[0] = p[1] + p[2]
        print(None)
    
        
    

def p_contenido(p): 
    ''' contenido : asignacion
                 |  asignacion COMA contenido '''
    
    if(len(p) == 2):

        p[0] = p[1]

    elif(len(p) == 4):
        p[0] =  p[1] + p[2] + p[3]


def p_asignacion(p):
    ''' asignacion : CADENACON PUNTOS valor
                   | CADENASIN PUNTOS valor
                   | CADENASIN PUNTOS axioma '''
    if len(p) == 4:
        p[0] = p[1] + p[2] + str(p[3])
    else:
        p[0] = p[1] + p[2] + p[3]

def p_valor(p):
    ''' valor : numero
              | comparacion
              | NULL
              | TR
              | FL
              | CADENACON 
              | axioma'''
    p[0] = p[1]

def p_numero(p):
    '''numero : INT
              | REAL
              | NCIENT
              | BIN
              | OCT
              | HEX '''
    p[0] = p[1]



def p_comparacion(p):
    ''' comparacion : numero LT numero
                    | numero GT numero
                    | numero EQ numero
                    | numero LE numero
                    | numero GE numero '''
    p[0] = str(p[1]) + p[2] + str(p[3])
    

def p_error(p):
    if p.value: 
        # El error es por el valor que no es correcto.
        print("[Syntax Error] At value ", p.value)
    else: 
        # El error es por la cadena que es incompleta o no correcta.
        print("[Syntax Error] EOF")

# Constructor del parser
parser = yacc.yacc()
file = open(sys.argv[1], "r")
content = file.read()
parser.parse(content)