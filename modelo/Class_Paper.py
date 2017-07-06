def unirArray(lista):
    salida2 = ""
    for i in range(len(lista)):
        salida2 = salida2 + lista[i]
    return salida2

def unirArraySalto(lista):
    salida3 = ""
    for i in range(len(lista)):
        salida3 = salida3 + "\n" +lista[i]
    return salida3

def unirArrayKeys(lista):
    salida4 = ""
    for i in range(len(lista)):
        salida4 = salida4 + ", " +lista[i]
    return salida4

class Paper:
    titulo = ""
    autores = []
    aoutCorpo = []
    pais = ""
    ciudad = ""
    correo = ""
    resumen = ""
    abstract = []
    introduccion = []
    palabrasClaves =[]
    keyWorks = []
    cuerpo = []
    subtitulo = ""
    recomendaciones = []
    conclusiones = []




    def __init__(self,title,pais,ciudad,correo):
        self.titulo = title
        self.pais = pais
        self.ciudad = ciudad
        self.correo = correo


    def addAutor(self,autor):
        self.autores.append(autor)

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

