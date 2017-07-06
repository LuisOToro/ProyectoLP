from control import creadorPDF
from modelo import Class_Paper


class Paper_Ieee(Class_Paper.Paper):
    referencias = []

    def __init__(self,title,pais,ciudad,correo):
        Class_Paper.Paper(title, pais, ciudad, correo)

    def addReferenciaArticle(self, exp_author,exp_title,exp_volume ,exp_number,exp_month, exp_year,exp_articleNumber):
        salida = exp_author + exp_title + exp_volume + exp_number
        salida = salida + exp_month + exp_year + exp_articleNumber
        self.referencias.append(salida)

    def addReferenciaBook(self,autor,titulo,ciudad,estado,año,pais,publisher,paginas,edicion,volumen):
        #bibtex tiene: autor,titulo,publisher, edicion,volumen,,año,
        salida = autor+", \""+publisher+",\" "+titulo+", "+edicion+" ed., vol. "+volumen+", "+ciudad+", "+estado+", "+pais+", "+año+"pp. "+paginas+"."

        self.referencias.append(salida)

    def addReferenciaManual(self,exp_author,exp_title,exp_city,exp_state,exp_country,exp_year):
        salida = exp_author+exp_title+exp_city+exp_state+exp_country+exp_year
        self.referencias.append(salida)

    def addReferenciaPubliacion(self, exp_author,exp_title,exp_pages):
        salida = exp_author+exp_title+exp_pages
        self.referencias.append(salida)

    def addReferenciaConference(self, exp_author,exp_title,exp_city,exp_state,exp_country,exp_year):
        salida = exp_author+exp_title+exp_city+exp_state+exp_country+exp_year
        self.referencias.append(salida)

    def crearPdf(self,idPaper,nombrePaper):
        resumenpdf = "Resumen --"+Class_Paper.unirArraySalto(self.resumen) + "\nPalabras claves: " + Class_Paper.unirArrayKeys(self.palabrasClaves)\
                     + "\nAbstract --" + Class_Paper.unirArraySalto(self.abstract) + "\nKeyworks: " + Class_Paper.unirArrayKeys(self.keyWorks)
        autores = Class_Paper.unirArrayKeys(self.autores)
        autoresC = Class_Paper.unirArraySalto(self.aoutCorpo)
        TotalAuto = autores + "\n"+autoresC
        lugar = self.ciudad +" "+self.pais
        mail = lugar+"\n"+self.correo
        intro = "1.     Introducción\n" + Class_Paper.unirArraySalto(self.introduccion)
        cuerpopdf = "2.     Cuerpo\n" + Class_Paper.unirArraySalto(self.cuerpo)
        recomendaciones = "3.       Recomendaciones\n" + Class_Paper.unirArraySalto(self.recomendaciones)
        conclusiones = "4.      Conclusiones\n" + Class_Paper.unirArraySalto(self.conclusiones)
        referencias = "5.       Referencias\n" + Class_Paper.unirArraySalto(self.referencias)
        texto = intro + "\n" + cuerpopdf + "\n" + recomendaciones + "\n" + conclusiones + "\n" + referencias
        creadorPDF.Generar(idPaper,self.titulo,texto,mail,TotalAuto,nombrePaper)
