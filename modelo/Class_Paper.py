
class Paper:
    titulo = ""
    autores = []
    aoutCorpo = []
    pais = ""
    ciudad = ""
    correo = ""
    resumen = ""
    abstract = ""
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
        pass

    def addResumen(self,resumen):
        pass

    def addAbstract (self,abstrac):
        pass

    def addIntro(self,intro):
        pass

    def addPalabraClaves(self,palabras):
        pass

    def addKeyWorks(self,palabras):
        pass

    def addCuerpo(self,cuerpo):
        pass

    def addSubtitulo(self,subtitulo):
        pass

    def addConclusiones(self,texto):
        pass

    def addRecomendaciones(self,texto):
        pass
