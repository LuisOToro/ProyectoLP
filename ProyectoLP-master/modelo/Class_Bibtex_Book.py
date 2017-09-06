import ply.yacc as yacc
from modelo import Class_bibtext

class A_sintactico_book:
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )

    def __init__(self,tokens):
        self.tokens = tokens
        self.names = {}
        self.bandera = 0



    def p_statement_bloque(self,p):
        'statement : STRING'
        p[0] = p[1]

    def p_statement_arroba_assign(self,p):
        'statement : ARROBA BOOK'
        self.names[p[0]] = p[2]

    def p_statement_reservadas(self,p):
        '''statement : titulo
                        | autor
                        | anio
                        | series
                        | nota
                        | volumen
                        | direccion
                        | edition
                        | mes
                        | isbn
                        | publicado
                        | book'''
        p[0] = p[1]

    def p_statement_title_assign(self,p):
        'titulo : TITLE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_autor_assign(self,p):
        'autor : AUTOR EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_publisher(self,p):
        'publicado : PUBLISHER EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_year_assing(self,p):
        'anio : YEAR EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_volumen_assign(self,p):
        'volumen : VOLUMEN EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_series_assing(self,p):
        'series : SERIES EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_address_assing(self,p):
        'direccion : ADDRESS EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_edition_assign(self,p):
        'edition : EDITION EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_mes_assign(self,p):
        'mes : MONTH EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_note_assign(self,p):
        'nota : NOTE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_expression_name(self,p):
        'statement : ARROBA BOOK LLLAVE STRING COMMA'
        self.names[p[0]] = p[4]

    def p_expression_number(self,p):
        'expression : NUMBER'
        p[0] = p[1]

    def p_statement_isbn_assign(self,p):
        'isbn : ISBN EQUALS LLLAVE NUMBER RLLAVE'
        self.names[p[1]] = p[4]

    def p_estructura(self,p):
        '''book : ARROBA BOOK LLLAVE STRING COMMA autor COMMA titulo COMMA publicado COMMA anio COMMA volumen COMMA series COMMA direccion COMMA edition COMMA mes COMMA nota COMMA isbn RLLAVE'''
        listTmp = p[4]
        lista = list(self.names.values())
        self.book = Class_bibtext.Bibtex_Book(listTmp,lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],
                                              lista[9],lista[10])
        self.bandera = 1

    def p_expression_binop(self,p):
        '''expression : expression PLUS expression
                          | expression MINUS expression
                          | expression TIMES expression
                          | expression DIVIDE expression'''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

    def p_error(self,p):
        print("\nERROR DE COMPILACION\n")

    def parse(self, data, **kwargs):
        self.parser.parse(data, **kwargs)


    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)


