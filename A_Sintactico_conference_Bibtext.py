from tokens import tokens
#desde aqui analizador sintactico
import ply.yacc as yacc
names = []

precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )


def p_statement_bloque(p):
    'statement : BLOQUE'
    p[0] = p[1]
    print("exito")

def p_statement_arroba_assign(p):
    'statement : ARROBA CONFERENCE'
    names[p[0]] = p[2]

def p_statement_autor_assign(p):
    'autor : AUTOR EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_title_assign(p):
    'titulo : TITLE EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_bookTitle_assign(p):
    'booktitle : BOOKTITLE EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_year_assing(p):
    'ano : YEAR EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statements_editor_assign(p):
    'editor : EDITOR EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_volumen_assign(p):
    'volumen : VOLUMEN EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_series_assing(p):
    'series : SERIES EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_paginas_assign(p):
    'pagina : PAGE EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_address_assing(p):
    'address : ADDRESS EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_mes_assign(p):
    'mes : MONTH EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_organization_assign(p):
    'organization : ONGANIZATION EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_statement_publisher(p):
    'publicado : PUBLISHER EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]


def p_statement_note_assign(p):
    'nota : NOTE EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[4]

def p_expression_name(p):
    'expression : ARROBA CONFERENCE LLLAVE NAME COMMA'
    names[p[0]] = p[4]

def p_expression_number(p):
    'expression : NUMBER'

def p_estructura(p):
    '''conference : ARROBA CONFERENCE LLLAVE NAME COMMA autor COMMA titulo COMMA booktitle COMMA ano COMMA editor COMMA volumen COMMA series COMMA paginas COMMA address COMMA mes COMMA organization COMMA publiser COMMA note RLLAVE'''
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
