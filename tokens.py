import ply.lex as lex
#analizador lexico
reservadas = {"articulo": "ARTICULO","autor": "AUTOR","titulo" : "TITLE", "anio": "YEAR", "paginas": "PAGE",
              "notas" : "NOTE", "volumen" : "VOLUMEN", "journal": "JOURNAL","numero" : "NUMERO",
              "mes" : "MONTH", "publicado" : "PUBLISHER", "series" : "SERIES","direccion" : "ADDRESS", "isbn" : "ISBN",
              "bookTitle" : "BOOKTITLE", "editor" : "EDITOR",
              "organization":"ONGANIZATION", "book":"BOOK",
              "edition":"EDITION", "conference":"CONFERENCE","manual":"MANUAL","unpublisher":"UNPUBLISHED"}

tokens = ['LLLAVE','RLLAVE','EQUALS','COMMA','NUMBER','ARROBA','PLUS','MINUS','TIMES','DIVIDE','STRING'] +  list(reservadas.values())

t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_EQUALS = r'\='
t_COMMA = r','
t_ARROBA = r'\@'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ignore = " \t+"
t_STRING = r'([a-zA-Z0-9][a-zA-Z0-9 ]+)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Error Lexico\nCaracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ARTICULO(t):
    r'article'
    return t

def t_AUTOR(t):
    r'author'
    return t

def t_TITLE(t):
    r'title'
    return t

def t_JOURNAL(t):
    r'journal'
    return t

def t_YEAR(t):
    r'year'
    return t

def t_NUMERO(t):
    r'number'
    return t

def t_PAGE(t):
    r'pages'
    return t

def t_MONTH(t):
    r'month'
    return t

def t_NOTE(t):
    r'note'
    return t

def t_VOLUMEN(t):
    r'volume'
    return t

def t_PUBLISHER(t):
    r'publisher'
    return t

def t_SERIES(t):
    r'series'
    return t

def t_ADDRESS(t):
    r'address'
    return t

def t_EDITION(t):
    r'edition'
    return t

def t_ISBN(t):
    r'isbn'
    return t

def t_BOOKTITLE(t):
    r'booktitle'
    return t

def t_EDITOR(t):
    r'editor'
    return t

def t_ONGANIZATION(t):
    r'organization'
    return t

def t_BOOK(t):
    r'book'
    return t

def t_CONFERENCE(t):
    r'conference'
    return t

def t_MANUAL(t):
    r'manual'
    return t

def t_UNPUBLISHED(t):
    r'unpublished'
    return t


lex.lex()
