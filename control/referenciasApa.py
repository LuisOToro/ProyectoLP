import re
#apa web
w1 = '(((([A-Z][a-zA-Z\s]+).(\s+)\(\d+\-\d+\)\.)(\s+)[A-Za-z\s]+)\:)(\s+)([A-Z][a-zA-Z\s]+)\.'
ciudad = '(\s[A-Za-z\s]+\,)'
ref2 = '(\s[A-Z]{2,}\.\:\s[A-Za-z0-9\s]+)\.'
url = '(\s+(Recuperado\sde\s(https?\:\/\/www\.[a-z]+((\.[a-zA-Z\-\_]+)?)+\.[a-z]{2,3})))'
Apa_Web = w1+ciudad+ref2+url
#Argosy Medical Animation. (2007-2009). Visible body: Discover human anatomy. New York, EU.: Argosy Publishing. Recuperado de http://www.visiblebody.com


#apa libro
exp_coma = '[(,)[ ]+]?'
apa_author= '[a-zA-Z\ ]+'
apa_inicial= '[A-Z](.)[ ]?'
apa_presidenteConferencia='(En )'+apa_inicial+apa_author+'[\(](Presidencia)[\)]'
apa_tituloConferencia = '[a-zA-Z0-9\ °]+'
apa_year= '([\(][0-9]+[\)]|[\(][a-zA-Z0-9\ ]+[\)]|[\(]([0-9]+(-)[0-9]+)[\)])[\.]?[ ]?'
apa_title = '([a-zA-Z\ ]+[\.]|[[a-zA-Z\ ]+(:)[a-zA-Z\ ]+]+)([\(]([a-zA-Z\ ]+)[\)](. ))?'
apa_cityCo= '([a-zA-Z\ ]+'+exp_coma+'[a-zA-Z\ ]+[\.]?[\:]?[[a-zA-Z\ ]+]?)?'
apa_editorial= '[a-zA-Z\ ]+[\.]?'
apa_nombreRevista= '[a-zA-Z\ ]+[\.]?'
apa_page = '(pp. )?(([0-9]+)(-)([0-9]+)|[0-9]+)[.]'
apa_volume = '[0-9]+( )[\(][0-9]+[\)]'
apa_website='((http://)|(https://))(www.)[[a-z\.]+[\/]?]+'#((http:\/\/)|(https:\/\/))(www.)[[a-z\.]+[\/]?]+

apaLibro=apa_author+exp_coma+apa_inicial+exp_coma+apa_year+exp_coma+apa_title+exp_coma+apa_cityCo+apa_editorial

#Hacyan, S., (2004), Fisica y metafisica en el espacio y el tiempo. La filosofia en el laboratorio, Mexico DF, Mexico: Fondo nacional de cultura economica.

#apa conferencia
p1 = '(([A-z][a-z]+)\,\s[A-Z]\.)'
p2 = '((\([A-Z][a-z]+\sde\s\d+\))\.)'
p3 = '((\s[a-zA-Z0-9\s\(\)\-\_]+)\.\sEn\s)'
p4 = '(([A-Z]\.\s[A-Z][a-zA-Z]+\s\([a-zA-Z]+\))\,)'
p5 = '(((\s[1-9][a-z]+)\s[A-Z][a-zA-Z\s]+)\.)'
p6 = '((\sCongreso\sllevado\sa\scabo\sen\s[A-Z][a-z]+)\,)'
p7 = '((\s[A-Z][a-z]+)\.)'

Apa_conferencia = p1+p2+p3+p4+p5+p6+p7

#Rojas, C.(Agosto de 2013). ABMS (Automatic BLAST for Massive Sequencing). En H. Castillo (Presidencia), 2do Congreso Colombiano de Biologia Computacional y Bioinformatica CCBCOL. Congreso llevado a cabo en Manizales, Colombia.


#Apa informe
#Departamento Administrativo Nacional de Estadisticas. (2012). Tecnologias de la informacion y las comunicaciones. Recuperado de: http://www.dane.gov.co
p1 = '(((([A-Z][a-zA-Z\s]+)\.)\s\(\d+\))\.\s+)'
p2 = '((([A-Z][a-zA-Z\s]+)\.)\s+)'
url = '((((Recuperado\s+de\:\s+)https?)\:\/\/www\.[a-z]+)((((\.[a-z]+))?)+)(\.[a-z]+))'

Apa_informe = p1+p2+url


#Apa Articulo

#Coruminas, M., Ronecro, C., Bruguca, E. (2007). Sistema dopaminergico y adicciones, Rev Mukuel, 44(1), 23-31.

p1 = '(([A-Z][a-z]+\,(\s+)?[A-Z]\.\,?\s)+)'
p2= '((\(\d+\)\.)\s+)'
p3 = '([A-Z][a-zA-Z\s\,]+)'
p4 = '((\d+\(\d\)\,\s+)(\d+\-\d+))\.'

Apa_Articulo = p1+p2+p3+p4

def addReferencia_Articulo_Regular(texto):
    if(re.match(Apa_Articulo,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Web_Regular(texto):
    if(re.match(Apa_Web,texto)):
        print("Referencia Agregada")
        return texto
    else:
        print("Referencia invalida")
        return ""

def addReferencia_Libro_Regular(texto):
    if(re.match(apaLibro,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Conferencia_Regular(texto):
    if(re.match(Apa_conferencia,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")

def addReferencia_Informe_Regular(texto):
    if(re.match(Apa_informe,texto)):
        print("Referencia Agregada")
        return texto
    else:
        return ""
        print("Referencia invalida")


"""addReferencia_Articulo_Regular("Coruminas, M., Ronecro, C., Bruguca, E. (2007). Sistema dopaminergico y adicciones, Rev Mukuel, 44(1), 23-31.")

addReferencia_Web_Regular("Argosy Medical Animation. (2007-2009). Visible body: Discover human anatomy. New York, EU.: Argosy Publishing. Recuperado de http://www.visiblebody.com")

addReferencia_Libro_Regular("Hacyan, S., (2004), Fisica y metafisica en el espacio y el tiempo. La filosofia en el laboratorio, Mexico DF, Mexico: Fondo nacional de cultura economica.")

addReferencia_Conferencia_Regular("Rojas, C.(Agosto de 2013). ABMS (Automatic BLAST for Massive Sequencing). En H. Castillo (Presidencia), 2do Congreso Colombiano de Biologia Computacional y Bioinformatica CCBCOL. Congreso llevado a cabo en Manizales, Colombia.")

addReferencia_Informe_Regular("Departamento Administrativo Nacional de Estadisticas. (2012). Tecnologias de la informacion y las comunicaciones. Recuperado de: http://www.dane.gov.co")"""




