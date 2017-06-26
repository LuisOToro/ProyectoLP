import tokens
#desde aqui analizador sintactico
import ply.yacc as yacc
tokens  = tokens.tokens
names = {}

precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )


def p_statement_bloque(p):
    'statement : STRING'
    p[0] = p[1]

def p_statement_arroba_assign(p):
    'statement : ARROBA BOOK'
    names[p[0]] = p[2]

def p_statement_reservadas(p):
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

def p_statement_title_assign(p):
    'titulo : TITLE EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]

def p_statement_autor_assign(p):
    'autor : AUTOR EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]

def p_statement_publisher(p):
    'publicado : PUBLISHER EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]

def p_statement_year_assing(p):
    'anio : YEAR EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_volumen_assign(p):
    'volumen : VOLUMEN EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_series_assing(p):
    'series : SERIES EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_address_assing(p):
    'direccion : ADDRESS EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]

def p_statement_edition_assign(p):
    'edition : EDITION EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_mes_assign(p):
    'mes : MONTH EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_note_assign(p):
    'nota : NOTE EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]

def p_expression_name(p):
    'statement : ARROBA BOOK LLLAVE STRING COMMA'
    names[p[0]] = p[4]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_statement_isbn_assign(p):
    'isbn : ISBN EQUALS LLLAVE NUMBER RLLAVE'
    names[p[1]] = p[4]

def p_estructura(p):
    '''book : ARROBA BOOK LLLAVE STRING COMMA autor COMMA titulo COMMA publicado COMMA anio COMMA volumen COMMA series COMMA direccion COMMA edition COMMA mes COMMA nota COMMA isbn RLLAVE'''
    print("si vale la estructura")

def p_expression_binop(p):
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

def p_error(p):
    print("\nERROR DE COMPILACION\n")

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input("Ingrese la ruta del archivo: ")
    except EOFError:
        break
    yacc.parse(s)