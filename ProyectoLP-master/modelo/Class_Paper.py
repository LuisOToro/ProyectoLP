import re
def unirArray(lista):
    salida2 = ""
    if len(lista)>1:
        for i in range(len(lista)):
            salida2 = salida2 + lista[i]
        return salida2
    else:
        return lista[0]


def unirArraySalto(lista):
    salida3 = ""
    if len(lista)>1:
        for i in range(len(lista)):
            salida3 = salida3 + "\n" + lista[i]
        return salida3
    else:
        return lista[0]


def unirArrayKeys(lista):
    salida4 = ""
    if len(lista)>1:
        for i in range(len(lista)):
            salida4 = salida4 + ", " + lista[i]
        return salida4
    else:
        return lista[0]


class Paper:

    def __init__(self,title,pais,ciudad):
        self.titulo = title
        self.pais = pais
        self.ciudad = ciudad
        self.autores = []
        self.aoutCorpo = []
        self.resumen = ""
        self.abstract = []
        self.introduccion = []
        self.palabrasClaves = []
        self.keyWorks = []
        self.cuerpo = []
        self.subtitulo = ""
        self.recomendaciones = []
        self.conclusiones = []
        self.correo = ""


    def addAutor(self,autor):
        self.autores.append(autor)

    def addMail(self,mail):
        if ( re.match('^[a-zA-Z]([0-9a-zA-Z\-\_]+)\@([a-z\-]+)\.([a-z]{2,3})((\.[a-z]+)?)+$',mail)) != None:
           self.correo = mail
        else:
            print("correo invalido ingrese un correo valido")

    def addAutorCorporativo(self,autorc):
        self.aoutCorpo.append(autorc)

    def addResumen(self,resumen):
        self.resumen = resumen

    def addAbstract (self,abstrac):
        self.abstract.append(abstrac)

    def addIntro(self,intro):
        self.introduccion.append(intro)

    def addPalabraClaves(self,palabras):
        self.palabrasClaves.append(palabras)

    def addKeyWorks(self,palabras):
        self.keyWorks.append(palabras)

    def addCuerpo(self,cuerpo):
        self.cuerpo.append(cuerpo)

    def addSubtitulo(self,subtitulo):
        self.subtitulo = subtitulo

    def addConclusiones(self,texto):
        self.conclusiones.append(texto)

    def addRecomendaciones(self,texto):
        self.recomendaciones.append(texto)


