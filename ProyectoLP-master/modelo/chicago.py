import re

exp_coma = '[(,)[ ]+]?'
ch_author='[[a-zA-Z]+'+exp_coma+']*[a-zA-Z]+'
exp_punto = '[. ]?'
ch_fecha = '([0-9]{,4}|([0-9]+(-)[0-9]+))'
ch_title = '([a-zA-Z\ ]+(:)[a-zA-Z\ ]+)?'
ch_edi = '([a-zA-Z\ ]+(:)[a-zA-Z\/\ ]+)?'
prueba = ch_author+exp_punto+ch_fecha+exp_punto+ch_title+exp_coma+ch_fecha+exp_punto+ch_edi+exp_punto
texto = 'Shepsle, Kenneth y Mark Bonchek. 2005. Las formulas de la política: instituciones, racionalidad y comportamiento. Mexico: Taurus/Centro de Investigación y Docencia Economicas.'
if(re.match(prueba,texto)):
        print("Referencia Agregada")
else:
        print("Referencia invalida")


from modelo import Class_Bibtex_Book,Class_Tokens
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
lexer = Class_Tokens.AnalizadorLexico(tokens, reservadas)
texto3 = "@book{mi book,  author    = {Peter Babington},   title     = {The title of the work},  publisher = {The name of the publisher},  year      = 1993,  volume    = 4,  series    = 10,  address   = {The address},  edition   = 3,  month     = 7,  note      = {An optional note},  isbn      = {3257227892}}"
sintac = Class_Bibtex_Book.A_sintactico_book(tokens)
sintac.build()
sintac.parse(texto3, debug=0)
paginas = input("Ingrese la pagina: ")
editorial = input("Ingrese la editorial: ")
mostrarRefe(sintac.book, paginas, editorial)

def mostrarRefe(Bibtex_Book,paginas,editorial):
    salida1 = Bibtex_Book.autor + ". " + str(Bibtex_Book.anio) + ". " + Bibtex_Book.titulo + ". " + Bibtex_Book.edicion+". "+Bibtex_Book.direccion+": "+Bibtex_Book.publisher
    print(salida1)