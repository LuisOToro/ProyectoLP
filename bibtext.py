import ply.lex as lex
#analizador lexico
reservadas = {'articulo': "ARTICULO","autor": "AUTOR","titulo" : "TITLE", "año": "YEAR", "paginas": "PAGE",
              "notas" : "NOTE", "volumen" : "VOLUMEN", "journal": "JOURNAL", "name" : "NAME", "numero" : "NUMERO", "mes" : "MONTH"}

tokens = ['LLLAVE','RLLAVE','EQUALS','COMMA','NUMBER','ARROBA','BLOQUE','PLUS','MINUS','TIMES','DIVIDE'] +  list(reservadas.values())

t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_EQUALS = r'='
t_COMMA = r','
t_ARROBA = r'@'
t_BLOQUE =  r'.+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_MONTH(t):
    r'month'
    t.type = reservadas.get(t.value, "mes")
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "name")
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO(t):
    r'number'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Error Lexico\nCaracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_articulo(t):
    r'ARTICLE'
    t.type = reservadas.get(t.value,"articulo")
    return  t

def t_autor(t):
    r'author'
    t.type = reservadas.get(t.value,"autor")
    return t

def t_titulo(t):
    r'title'
    t.type = reservadas.get(t.value,"titulo")
    return t

def t_año(t):
    r'año'
    t.type = reservadas.get(t.value,"año")
    return t

def t_paginas(t):
    r'pages'
    t.type = reservadas.get(t.value,"paginas")
    return t

def t_notas(t):
    r'note'
    t.type = reservadas.get(t.value,"notas")
    return t

def t_volumen(t):
    r'volume'
    t.type = reservadas.get(t.value,"volumen")
    return t

def t_journal(t):
    r'journal'
    t.type = reservadas.get(t.value,"journal")
    return t

lex.lex()

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

def p_statement_arroba_assign(p):
    'statement : ARROBA ARTICLE'
    names[p[0]] = p[2]

def p_statement_title_assign(p):
    'titulo : TITLE EQUALS BLOQUE'
    names[p[1]] = p[3]

def p_statement_autor_assign(p):
    'autor : AUTOR EQUALS BLOQUE'
    names[p[1]] = p[3]

def p_statement_year_assing(p):
    'ano : YEAR EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_paginas_assign(p):
    'pagina : PAGE EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_note_assign(p):
    'nota : NOTE EQUALS BLOQUE'
    names[p[1]] = p[3]

def p_statement_volumen_assign(p):
    'volumen : VOLUMEN EQUALS NUMBER'
    names[p[1]] = p[3]

def p_statement_journal_assign(p):
    'journal : JOURNAL EQUALS BLOQUE'
    names[p[1]] = p[3]

def p_statement_number_assign(p):
    'numero : NUMERO EQUAL NUMBER'
    names[p[1]] = p[3]

def p_statement_mes_assign(p):
    'mes : MONTH EQUALS NUMBER'
    names[p[1]] = p[3]

def p_expression_name(p):
    'expression : ARROBA ARTICLE LLLAVE NAME COMMA'
    names[p[0]] = p[4]

def p_expression_number(p):
    'expression : NUMBER'

def p_estructura(p):
    '''articulo : ARROBA ARTICLE LLLAVE NAME COMMA autor COMMA titulo COMMA journal COMMA ano COMMA numero COMMA pagina COMMA mes COMMA nota COMMA volumen COMMA'''
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
