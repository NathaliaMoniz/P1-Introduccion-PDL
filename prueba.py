import sys
import ply.yacc as yacc
from ajson_lexer import LexerClass

class ParserClass:
    tokens = LexerClass.tokens
    
    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = LexerClass().lexer
        self.contenido = None

    def p_axioma(self, p):
        ''' axioma : LLAVEA contenido LLAVEC 
                   | LLAVEA LLAVEC'''

        if len(p) == 4:
            p[0] = p[2]
        
        else:
            p[0] = {}

        self.contenido = p[0]
    
    def p_contenido(self, p): 
        ''' contenido : asignacion
                      | asignacion COMA
                      | asignacion COMA contenido '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1]
        elif len(p) == 4:
            # unión de diccionarios
            p[0] = {**p[1], **p[3]}
        

    def p_asignacion(self, p):
        ''' asignacion : CADENACON PUNTOS valor
                       | CADENASIN PUNTOS valor
                       | CADENASIN PUNTOS axioma '''
        p[0] = {p[1] : p[3]}
        

    def p_valor(self, p):
        ''' valor : numero
                | comparacion
                | NULL
                | TR
                | FL
                | CADENACON 
                | axioma'''
        p[0] = p[1]
       
    
    def p_numero(self, p):
        '''numero : INT
                | REAL
                | NCIENT
                | BIN
                | OCT
                | HEX '''
        
        p[0] = p[1]

    def p_comparacion(self, p):
        ''' comparacion : numero LT numero
                        | numero GT numero
                        | numero EQ numero
                        | numero LE numero
                        | numero GE numero '''
        if p[2] == "<":
            p[0] = (p[1] < p[3])
        elif p[2] == ">":
            p[0] = (p[1] > p[3])
        elif p[2] == "==":
            p[0] = (p[1] == p[3])
        elif p[2] == "<=":
            p[0] = (p[1] <= p[3])
        elif p[2] == ">=":
            p[0] = (p[1] >= p[3])
        

    def p_error(self, p):
        if p.value: 
            print("[Syntax Error] At value ", p.value)
        else: 
            print("[Syntax Error] EOF")
    
    def test(self, data):
        self.parser.parse(data)
    
    def imprimir_anidado(self, dic, clave_previa=''):
        for clave, valor in dic.items():
            if clave_previa:
                nueva_clave = clave_previa + '.' + clave
            else:
                nueva_clave = clave
            if isinstance(valor, dict):
                self.imprimir_anidado(valor, nueva_clave)
            else:
                print(f'{{ {nueva_clave}:  {valor} }}')

    def imprimir(self, filename):
        print(f'FICHERO AJSON "{filename}"')
        self.imprimir_anidado(self.contenido)

    def test_with_files(self, path):
        file = open(path)
        content = file.read()  
        self.test(content)
        self.imprimir(path)    
    


