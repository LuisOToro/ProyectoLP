import re

#referencia book
#G. O. Young, \"Synthetic structure of industrial plastics,\" in Plastics, 2nd ed., vol. 3, J. Peters, Ed. New York, NY, USA: McGraw-Hill, 1964, pp. 15-64.

iniciales = '(([A-Z]\.)\s([A-Z]\.))'
apellido = '(\s[A-Z][a-z]+\,)'
tituloPubli = '(\s\"[A-Z][a-z0-9\-\_\s]+\,\")'
published = '([\sa-zA-Z0-9]+\,)'
edicion = '(\s[1-9]+[a-z]{2,}\sed\.\,)'
volumen = '(\svol\.\s[1-9]+\,)'
segundoA = '(\s[A-Z]\.\s[A-Z][a-z]+\,)'
ciudad = '(\sEd.(\s[A-Z][a-z]+\s[A-Z][a-z]+)\,)'
pais = '(\s[A-Z]+\:)'
estado = '(\s[A-Z]+\,)'
organizacion = '(\s[A-Z][a-z]+([A-Z][a-z]+)?\-?([A-Z][a-z]+)?\,)'
anio = '(\s[0-9]+\,)'
pagina = '((\spp\.\s([1-9][0-9]+)\-([1-9][0-9]+))\.)'

Ieee_Book= iniciales+apellido+tituloPubli+published+edicion+volumen+segundoA+ciudad+estado+pais+organizacion+anio+pagina


#ieee nopublicado
#B. Smith, "An approach to graphs of linear forms," unpublished.
exp_author = '((([A-Z][.][ ]+)+[a-zA-Z]+)(, ))*(and )?([A-Z][.][ ]+)+[a-zA-Z]+'
exp_coma = '[(,)[ ]+]?'
exp_title = '(((")[a-zA-Z ]+(,")( in )([a-zA-Z ]+))?|([a-zA-Z ]+)|((")[a-zA-Z]+(")))'
noPublicado = exp_author+exp_coma+exp_title+'( unpublished.)?'


#ieee conferencia

p1 = '(([A-Z]\.\s[A-Z][a-z]+\,)\s+)'
p2 = '(\"[A-Z][a-zA-Z0-9\s\-\_]+\,\")'
p3 = '(((\s+in\sProc\.\s+)[A-Z]{4}\-[A-Z]{4})\,)'
p4 = '((\s[A-Z][a-z]+)\,\s+[A-Z]+\,\s+[A-Z]+\,)'
p5 = '(\s+((((\d+\,\s+)pp\.\s+)(\d+\-\d+))\.))'

Ieee_conferencia = p1+p2+p3+p4+p5


#Ieee informe
#Departamento Administrativo Nacional de Estadisticas. (2012). Tecnologias de la informacion y las comunicaciones. Recuperado de: http://www.dane.gov.co
p1 = '(((([A-Z][a-zA-Z\s]+)\.)\s\(\d+\))\.\s+)'
p2 = '((([A-Z][a-zA-Z\s]+)\.)\s+)'
url = '((((Recuperado\s+de\:\s+)https?)\:\/\/www\.[a-z]+)((((\.[a-z]+))?)+)(\.[a-z]+))'

Ieee_informe = p1+p2+url



#Ieee web
w1 = '(((([A-Z][a-zA-Z\s]+).(\s+)\(\d+\-\d+\)\.)(\s+)[A-Za-z\s]+)\:)(\s+)([A-Z][a-zA-Z\s]+)\.'
ciudad = '(\s[A-Za-z\s]+\,)'
ref2 = '(\s[A-Z]{2,}\.\:\s[A-Za-z0-9\s]+)\.'
url = '(\s+(Recuperado\sde\s(https?\:\/\/www\.[a-z]+((\.[a-zA-Z\-\_]+)?)+\.[a-z]{2,3})))'
Ieee_Web = w1+ciudad+ref2+url
#Argosy Medical Animation. (2007-2009). Visible body: Discover human anatomy. New York, EU.: Argosy Publishing. Recuperado de http://www.visiblebody.com






# aqui funciones

def addReferencia_NoPublicado_Regular(texto):
    if(re.match(noPublicado,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Web_Regular(texto):
    if(re.match(Ieee_Web,texto)):
        print("Referencia Agregada")
        return texto
    else:
        print("Referencia invalida")
        return ""

def addReferencia_Libro_Regular(texto):
    if(re.match(Ieee_Book,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Conferencia_Regular(texto):
    if(re.match(Ieee_conferencia,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Informe_Regular(texto):
    if(re.match(Ieee_informe,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")


