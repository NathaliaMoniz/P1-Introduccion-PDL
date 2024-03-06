import sys
import ply.yacc as yacc
from ajson_lexer import LexerClass

""" Reconocedor sintáctico. """
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
            p[0] = None

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
            p[0] = p[1] + p[3]
        

    def p_asignacion(self, p):
        ''' asignacion : CADENACON PUNTOS valor
                       | CADENASIN PUNTOS valor
                       | CADENASIN PUNTOS axioma '''
        p[0] = str({p[1] : p[3]})
        

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
            # El error es por el valor que no es correcto.
            print("[Syntax Error] At value ", p.value)
        else: 
            # El error es por la cadena que es incompleta o no correcta.
            print("[Syntax Error] EOF")
    
    def test(self, data):
        self.parser.parse(data)
    
    def test_with_files(self, path):
        file = open(path)
        content = file.read()  
        self.test(content)
        print(self.contenido)
        """self.imprimir()"""

    """def imprimir(self):
        if self.contenido == "":
            print('FICHERO AJSON VACÍO "' + sys.argv[1] + '"')
            return
        print('FICHERO AJSON "' + sys.argv[1] + '"')
        print(self.contenido)"""

