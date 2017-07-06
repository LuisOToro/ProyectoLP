from modelo import Class_Paper
from control import crearPaginas

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
         9: "Septiembre",
         10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

class Paper_Apa(Class_Paper.Paper):


    def __init__(self,title,pais,ciudad):
        Class_Paper.Paper(title, pais, ciudad)
        self.refencias = []

    def addReferenciaArticle(self, Bibtex_articulo):
        salida = Bibtex_articulo.autor+ ".("+meses[Bibtex_articulo.mes]+", "+str(Bibtex_articulo.anio)+"). "+Bibtex_articulo.titulo+". "+Bibtex_articulo.journal+", "+str(Bibtex_articulo.volumen)+", "+Bibtex_articulo.pagina
        self.refencias.append(salida)

    def addReferenciaBook(self,Bibtex_Book,paginas,editorial):
        salida = Bibtex_Book.autor + ". ("+meses[Bibtex_Book.mes]+", "+str(Bibtex_Book.anio)+"). "+Bibtex_Book.publisher+". En "+ Bibtex_Book.titulo+"(pp. "+paginas+"). "+Bibtex_Book.direccion+": "+editorial
        self.refencias.append(salida)

    def addReferenciaManual(self,Bibtex_Manual):
        salida = Bibtex_Manual.autor + ". ("+meses[Bibtex_Manual.mes]+", "+str(Bibtex_Manual.anio)+"). "+ Bibtex_Manual.titulo+". "+Bibtex_Manual.organizacion+". "+Bibtex_Manual.direccion+"."
        self.refencias.append(salida)

    def addReferenciaPubliacion(self,Bibtex_Publicacion):
        salida= Bibtex_Publicacion.autor + ". ("+meses[Bibtex_Publicacion.mes]+", "+str(Bibtex_Publicacion.anio)+"). "+Bibtex_Publicacion.titulo+". "+Bibtex_Publicacion.nombre
        self.refencias.append(salida)

    def addReferenciaConference(self, Bibtex_conference,pais):
        print(Bibtex_conference.mes)
        salida = Bibtex_conference.autor+". ("+meses[Bibtex_conference.mes]+", "+str(Bibtex_conference.anio)+"). "+Bibtex_conference.titulo+". "+Bibtex_conference.organizacion+". "+Bibtex_conference.nameConference+". Congreso llevado a cabo en "+Bibtex_conference.organizacion+", "+pais
        self.refencias.append(salida)

    def crearPdf(self,nombrePaper,titulo):
        resumenpdf = "Resumen --" + Class_Paper.unirArraySalto(
            self.resumen) + "\nPalabras claves: " + Class_Paper.unirArrayKeys(self.palabrasClaves) \
                     + "\nAbstract --" + Class_Paper.unirArraySalto(
            self.abstract) + "\nKeyworks: " + Class_Paper.unirArrayKeys(self.keyWorks)

        autores = Class_Paper.unirArrayKeys(self.autores)
        autoresC = Class_Paper.unirArraySalto(self.aoutCorpo)
        TotalAuto = autores + "\n" + autoresC
        lugar = self.ciudad + " " + self.pais
        mail = lugar + "\n" + self.correo

        primeraPagina = "\n" + TotalAuto + "\n" + mail

        intro = "1.     Introducción\n" + Class_Paper.unirArraySalto(self.introduccion)
        cuerpopdf = "2.     Cuerpo\n" + Class_Paper.unirArraySalto(self.cuerpo)
        recomendaciones = "3.       Recomendaciones\n" + Class_Paper.unirArraySalto(self.recomendaciones)
        conclusiones = "4.      Conclusiones\n" + Class_Paper.unirArraySalto(self.conclusiones)
        referencias = "5.       Referencias\n" + Class_Paper.unirArraySalto(self.referencias)

        crearPaginas.paperApa(nombrePaper,titulo,primeraPagina,resumenpdf,intro,cuerpopdf,recomendaciones,conclusiones,referencias)




