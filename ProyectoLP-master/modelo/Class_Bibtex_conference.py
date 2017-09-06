import ply.yacc as yacc
from modelo import Class_bibtext


class A_sintactico_conference:
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )

    def __init__(self,tokens):
        self.tokens = tokens
        self.names = {}
        self.bandera = 0


    def p_statement_reservadas(self,p):
        '''statement : titulo
                        | autor
                        | anio
                        | pagina
                        | nota
                        | volumen
                        | bookTitle
                        | editor
                        | mes
                        | series
                        | direccion
                        | organization
                        | publicado
                        | conference'''
        p[0] = p[1]

    def p_statement_bloque(self,p):
        'statement : STRING'
        p[0] = p[1]
        print(p[1])

    def p_statement_arroba_assign(self,p):
        'statement : ARROBA CONFERENCE'
        self.names[p[0]] = p[2]

    def p_statement_autor_assign(self,p):
        'autor : AUTOR EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_title_assign(self,p):
        'titulo : TITLE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_bookTitle_assign(self,p):
        'bookTitle : BOOKTITLE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_year_assing(self,p):
        'anio : YEAR EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statements_editor_assign(self,p):
        'editor : EDITOR EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_volumen_assign(self,p):
        'volumen : VOLUMEN EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_series_assing(self,p):
        'series : SERIES EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_paginas_assign(self,p):
        'pagina : PAGE EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_address_assing(self,p):
        'direccion : ADDRESS EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_mes_assign(self,p):
        'mes : MONTH EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_organization_assign(self,p):
        'organization : ONGANIZATION EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_publisher(self,p):
        'publicado : PUBLISHER EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_note_assign(self,p):
        'nota : NOTE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_expression_name(self,p):
        'statement : ARROBA CONFERENCE LLLAVE STRING COMMA'
        self.names[p[0]] = p[4]

    def p_expression_number(self,p):
        'expression : NUMBER'
        p[0] = p[1]

    def p_estructura(self,p):
        '''conference : ARROBA CONFERENCE LLLAVE STRING COMMA autor COMMA titulo COMMA bookTitle COMMA anio COMMA editor COMMA volumen COMMA series COMMA pagina COMMA direccion COMMA mes COMMA organization COMMA publicado COMMA nota RLLAVE'''
        listTmp = p[4]
        lista = list(self.names.values())
        self.bandera = 1
        self.conference = Class_bibtext.Bibtex_Conference(listTmp,lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],
                                                          lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12])



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
