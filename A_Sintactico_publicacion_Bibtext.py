import tokens
#desde aqui analizador sintactico
import ply.yacc as yacc
tokens = tokens.tokens
names = {}

precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),

    )

def p_statement_reservadas(p):
    '''statement : titulo
                    | autor
                    | unpublished
                    | nota
                    | mes
                    | anio'''
    p[0] = p[1]

def p_statement_bloque(p):
    'statement : STRING'
    p[0] = p[1]


def p_statement_year_assing(p):
    'anio : YEAR EQUALS NUMBER'
    names[p[1]] = p[3]


def p_statement_arroba_assign(p):
    'statement : ARROBA UNPUBLISHED'
    names[p[0]] = p[2]


def p_statement_title_assign(p):
    'titulo : TITLE EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]


def p_statement_autor_assign(p):
    'autor : AUTOR EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]


def p_statement_note_assign(p):
    'nota : NOTE EQUALS LLLAVE STRING RLLAVE'
    names[p[1]] = p[4]


def p_statement_mes_assign(p):
    'mes : MONTH EQUALS NUMBER'
    names[p[1]] = p[3]


def p_expression_name(p):
    'statement : ARROBA UNPUBLISHED LLLAVE STRING COMMA'
    names[p[0]] = p[4]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_estructura(p):
    '''unpublished : ARROBA UNPUBLISHED LLLAVE STRING COMMA autor COMMA titulo COMMA nota COMMA mes COMMA anio RLLAVE'''
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