from modelo import Class_Paper
class Paper_Ieee(Class_Paper.Paper):

    def __init__(self,title,pais,ciudad,correo):
        Class_Paper.Paper(title,pais,ciudad,correo)

    def addReferenciaArticle(self, **kwargs):
        pass

    def addReferenciaBook(self, **kwargs):
        pass

    def addReferenciaManual(self, **kwargs):
        pass

    def addReferenciaPubliacion(self, **kwargs):
        pass

    def addReferenciaConference(self, **kwargs):
        pass