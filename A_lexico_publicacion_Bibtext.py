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
    'statement : ARROBA ARTICULO'
    names[p[0]] = p[2]

def p_statement_title_assign(p):
    'titulo : TITLE EQUALS LLLAVE BLOQUE RLLAVE'
    names[p[1]] = p[3]

def p_statement_autor_assign(p):
    'autor : AUTOR EQUALS LLAVE BLOQUE RLLAVE'
    names[p[1]] = p[3]

def p_statement_year_assing(p):
    'ano : YEAR EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_paginas_assign(p):
    'pagina : PAGE EQUALS LLAVE BLOQUE RLLAVE'
    names[p[1]] = p[3]

def p_statement_note_assign(p):
    'nota : NOTE EQUALS LLAVE BLOQUE RLLAVE'
    names[p[1]] = p[3]

def p_statement_volumen_assign(p):
    'volumen : VOLUMEN EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_journal_assign(p):
    'journal : JOURNAL EQUALS LLAVE BLOQUE RLLAVE'
    names[p[1]] = p[3]

def p_statement_number_assign(p):
    'numero : NUMERO EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_mes_assign(p):
    'mes : MONTH EQUALS NUMBER'
    names[p[1]] = p[3]

def p_expression_name(p):
    'expression : ARROBA ARTICULO LLLAVE NAME COMMA'
    names[p[0]] = p[4]

def p_expression_number(p):
    'expression : NUMBER'

def p_estructura(p):
    '''articulo : ARROBA ARTICULO LLLAVE NAME COMMA autor COMMA titulo COMMA journal COMMA ano COMMA numero COMMA pagina COMMA mes COMMA nota COMMA volumen COMMA'''
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
