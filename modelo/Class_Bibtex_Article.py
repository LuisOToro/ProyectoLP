import ply.yacc as yacc


class A_sintactico_article:
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )

    def __init__(self,tokens):
        self.tokens = tokens
        self.names = {}


    def p_statement_bloque(self,p):
        'statement : STRING'
        p[0] = p[1]

    def p_statement_arroba_assign(self,p):
        'statement : ARROBA ARTICULO'
        p[0] = p[2]

    def p_statement_reservadas(self,p):
        '''statement : titulo
                        | autor
                        | anio
                        | pagina
                        | nota
                        | volumen
                        | journal
                        | numero
                        | mes
                        | articulo'''
        p[0] = p[1]

    def p_statement_title_assign(self,p):
        'titulo : TITLE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_autor_assign(self,p):
        'autor : AUTOR EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_year_assing(self,p):
        'anio : YEAR EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_paginas_assign(self,p):
        'pagina : PAGE EQUALS LLLAVE NUMBER MINUS NUMBER RLLAVE'
        self.names[p[1]] = p[4]

    def p_expression_number(self,p):
        'expression : NUMBER'
        p[0] = p[1]

    def p_statement_note_assign(self,p):
        'nota : NOTE EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_volumen_assign(self,p):
        'volumen : VOLUMEN EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_journal_assign(self,p):
        'journal : JOURNAL EQUALS LLLAVE STRING RLLAVE'
        self.names[p[1]] = p[4]

    def p_statement_number_assign(self,p):
        'numero : NUMERO EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_statement_mes_assign(self,p):
        'mes : MONTH EQUALS NUMBER'
        self.names[p[1]] = p[3]

    def p_estructura(self,p):
        'articulo : ARROBA ARTICULO LLLAVE STRING COMMA autor COMMA titulo COMMA journal COMMA anio COMMA numero COMMA pagina COMMA mes COMMA nota COMMA volumen RLLAVE'
        print("si vale la estructura")

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


