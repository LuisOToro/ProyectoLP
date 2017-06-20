import ply.lex as lex
#analizador lexico

reservadas = {"articulo": "ARTICULO","autor": "AUTOR","titulo" : "TITLE", "anio": "YEAR", "paginas": "PAGE",
              "notas" : "NOTE", "volumen" : "VOLUMEN", "journal": "JOURNAL", "name" : "NAME", "numero" : "NUMERO",
              "mes" : "MONTH", "publicado" : "PUBLISHER", "series" : "SERIES","direccion" : "ADDRESS", "edicion" : "EDITION",
              "isbn" : "ISBN", "bookTitle" : "BOOKTITLE", "editor" : "EDITOR", "organization":"ONGANIZATION", "book":"BOOK",
              "edition":"EDITION", "conference":"CONFERENCE","manual":"MANUAL","unpublisher":"UNPUBLISHED"}

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


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Error Lexico\nCaracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)





lex.lex()
