from modelo import Class_Paper_Apa,Class_Paper_Ieee,Class_Bibtex_conference,Class_Bibtex_Book,Class_Bibtex_Article,Class_Bibtex_manual,Class_Bibtex_publicacion,Class_Tokens,Class_Paper
from control import help

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

class paperDirector:
    def __init__(self,tipo,titulo,pais,ciudad):
        self.tipoPaper = tipo
        if tipo == 1:
            self.paper = Class_Paper_Apa.Paper_Apa(titulo,pais,ciudad)
        elif tipo == 2:
            self.paper = Class_Paper_Ieee.Paper_Ieee(titulo,pais,ciudad)
        else:
            print("El formato seleccionado no es valido, no existe el modelo de paper en la libreria")
            self.paper = None



    def iniciarBibtex_compiler_add_referencias(self,tipo,textoValidar):
        #tipo = 1 para apa =2 IEEE
        lexer.build()
        lexer.tokenize(textoValidar)
        lexer.print_tokens(True)
        if tipo == 1:
            sintac = Class_Bibtex_Article.A_sintactico_article(tokens)
            sintac.build()
            sintac.parse(textoValidar, debug=0)
            if sintac.bandera == 1:
                if self.tipoPaper == 1:
                    self.paper.addReferenciaArticle(sintac.articulo)
                    print("Referencia Agregada")
                elif self.tipoPaper == 2:
                    self.paper.addReferenciaArticle(sintac.articulo)
                    print("Referencia Agregada")
                else:
                    print("Tipo de paper invalido")
            else:
                print("Formato bibtex invalido")
        elif tipo == 2:
            sintac = Class_Bibtex_Book.A_sintactico_book(tokens)
            sintac.build()
            sintac.parse(textoValidar, debug=0)
            if sintac.bandera == 1:
                paginas = input("Ingrese la pagina: ")
                if self.tipoPaper == 1:
                    editorial = input("Ingrese la editorial: ")
                    self.paper.addReferenciaBook(sintac.book,paginas,editorial)
                    print("Referencia Agregada")
                elif self.tipoPaper == 2:
                    ciudad = input("Ingrese la ciudad: ")
                    estado = input("Ingrese el estado: ")
                    pais = input("Ingrese el pais: ")
                    self.paper.addReferenciaBook_Ieee(ciudad,estado,pais,paginas,sintac.book)
                    print("Referencia Agregada")
                else:
                    print("Tipo de paper invalido")
            else:
                print("Formato bibtex invalido")

        elif tipo == 3:
            sintac = Class_Bibtex_conference.A_sintactico_conference(tokens)
            sintac.build()
            sintac.parse(textoValidar, debug=0)
            if sintac.bandera == 1:
                pais = input("Ingrese el pais: ")
                if self.tipoPaper == 1:
                    self.paper.addReferenciaConference(sintac.conference,pais)
                    print("Referencia Agregada")
                elif self.tipoPaper == 2:
                    ciudad = input("Ingrese la ciudad: ")
                    estado = input("Ingrese el estado: ")
                    self.paper.addReferenciaConference(sintac.conference,ciudad,estado,pais)
                    print("Referencia Agregada")
                else:
                    print("Tipo de paper invalido")
            else:
                print("Formato bibtex invalido")

        elif tipo == 4 :
            sintac = Class_Bibtex_manual.A_sintactico_manual(tokens)
            sintac.build()
            sintac.parse(textoValidar, debug=0)
            if sintac.bandera == 1:
                if self.tipoPaper == 1:
                    self.paper.addReferenciaManual(sintac.manual)
                    print("Referencia Agregada")
                elif self.tipoPaper == 2:
                    self.paper.addReferenciaManual(sintac.manual)
                    print("Referencia Agregada")
                else:
                    print("Tipo de paper invalido")
            else:
                print("Formato bibtex invalido")

        elif tipo == 5 :
            sintac = Class_Bibtex_publicacion.A_sintactico_publicacion(tokens)
            sintac.build()
            sintac.parse(textoValidar, debug=0)
            if sintac.bandera == 1:
                if self.tipoPaper == 1:
                    self.paper.addReferenciaPubliacion(sintac.publicacion)
                    print("Referencia Agregada")
                elif self.tipoPaper == 2:
                    self.paper.addReferenciaPubliacion(sintac.publicacion)
                    print("Referencia Agregada")
                else:
                    print("Tipo de paper invalido")
            else:
                print("Formato bibtex invalido")

        else:
            print("Referencia Bibtex invalida")
            print("No se agrego la referencia")


    def help(self):
        help.referencias_Bibtex_posibles()



