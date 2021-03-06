from control import crearPaginas
from modelo import Class_Paper
import re
mes = {1: "Ene.",2: "Feb.",3 : "Mar.",4: "Abr.",5: "May.", 6: "Jun.", 7: "Jul.", 8: "Ago.",9: "Sept.", 10: "Oct.", 11: "Nov.", 12: "Dic."}

class Paper_Ieee(Class_Paper.Paper):


    def __init__(self,title,pais,ciudad):
        Class_Paper.Paper.__init__(self,title, pais, ciudad)
        self.referencias = []


    def addReferenciaArticle(self,bibtex_Article):
        salida = bibtex_Article.autor + ", "+ "\" "+ bibtex_Article.titulo+",\" "+bibtex_Article.journal+ ", vol. "+str(bibtex_Article.volumen)+", pp. "+bibtex_Article.pagina+", "+str(bibtex_Article.mes)+", "+str(bibtex_Article.anio)
        self.referencias.append(salida)


    def addReferenciaBook_Ieee(self,ciudad,estado,pais,paginas,bibTex_Book):
        salida = bibTex_Book.autor+", \""+bibTex_Book.publisher+",\" "+bibTex_Book.titulo+", "+str(bibTex_Book.edicion)+" ed., vol. "+str(bibTex_Book.volumen)+", "+ciudad+", "+estado+", "+pais+", "+str(bibTex_Book.anio)+"pp. "+str(paginas)+"."
        self.referencias.append(salida)

    def addReferenciaManual(self,Bibtex_Manual):
        #titulo,autor,organizacion,direccion,edicion,mes,anio,nota,nombre
        salida = Bibtex_Manual.autor + ", \" " + Bibtex_Manual.titulo +",\" "+ Bibtex_Manual.organizacion+", " + Bibtex_Manual.direccion+ ", Tech. Rep. TR-0200" + Bibtex_Manual.edicion+ ", "+ mes[Bibtex_Manual.mes] + str(Bibtex_Manual.anio)
        self.referencias.append(salida)

    def addReferenciaPubliacion(self,Bibtex_publicacion):
        salida = Bibtex_publicacion.autor + ", \" "+Bibtex_publicacion.titulo+", \""+mes[Bibtex_publicacion.mes]+ str(Bibtex_publicacion.anio)
        self.referencias.append(salida)


    def addReferenciaConference(self,Bibtext_conference,ciudad,estado,pais):
        salida = Bibtext_conference.autor+", \" "+Bibtext_conference.titulo +",\" "+ciudad+", "+estado+", "+pais+", "+str(Bibtext_conference.anio)
        self.referencias.append(salida)


    def crearPdf(self,nombrepdf,titulo):
        resumenpdf = []
        resumenpdf.append("Resumen -- " + self.resumen + ".")
        resumenpdf.append("Palabras claves: " + Class_Paper.unirArrayKeys(self.palabrasClaves) + ".")
        resumenpdf.append("Abstract --" + Class_Paper.unirArraySalto(self.abstract) + ".")
        resumenpdf.append("Keyworks: " + Class_Paper.unirArrayKeys(self.keyWorks) + ".")

        autores = Class_Paper.unirArrayKeys(self.autores)
        autoresC = Class_Paper.unirArraySalto(self.aoutCorpo)
        TotalAuto = autores + "\n" + autoresC
        lugar = self.ciudad + ", " + self.pais
        mail = self.correo

        intro = self.introduccion
        cuerpopdf = self.cuerpo
        recomendaciones = self.recomendaciones
        conclusiones = self.conclusiones
        referencias = self.referencias

        name_EXt = nombrepdf+".pdf"

        crearPaginas.paperIee(name_EXt,resumenpdf,autores,autoresC,lugar,mail,intro,cuerpopdf,recomendaciones,conclusiones,referencias,titulo)



