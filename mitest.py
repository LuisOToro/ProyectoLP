from modelo import Class_Bibtex_Book,Class_Tokens,Class_Bibtex_conference

reservadas = {"articulo": "ARTICULO", "autor": "AUTOR", "titulo": "TITLE", "anio": "YEAR", "paginas": "PAGE",
                      "notas": "NOTE", "volumen": "VOLUMEN", "journal": "JOURNAL", "numero": "NUMERO",
                      "mes": "MONTH", "publicado": "PUBLISHER", "series": "SERIES", "direccion": "ADDRESS",
                      "isbn": "ISBN",
                      "bookTitle": "BOOKTITLE", "editor": "EDITOR",
                      "organization": "ONGANIZATION", "book": "BOOK",
                      "edition": "EDITION", "conference": "CONFERENCE", "manual": "MANUAL",
                      "unpublisher": "UNPUBLISHED"}

tokens = ['LLLAVE', 'RLLAVE', 'EQUALS', 'COMMA', 'NUMBER', 'ARROBA', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                  'STRING'] + list(reservadas.values())

text = "@conference{mis conference,  author       = {Peter Draper},   title        = {The title of the work},  booktitle    = {The title of the book},  year         = 1993,  editor       = {The editor},  volume       = 4,  series       = 5,  pages        = 213,  address      = {The address of the publisher},  month        = 7,  organization = {The organization},  publisher    = {The publisher},  note         = {An optional note}  }"

lexer = Class_Tokens.AnalizadorLexico(tokens,reservadas)

sintac = Class_Bibtex_conference.A_sintactico_conference(tokens)
sintac.build()
lexer.build()
lexer.tokenize(text)
lexer.print_tokens(True)


sintac.parse(text,debug=0)
if sintac.bandera == 0:
    print(0)
elif sintac.bandera == 1:
    print(255)
    print(sintac.conference.anio)

