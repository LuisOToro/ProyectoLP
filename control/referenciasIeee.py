import re

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
cadena = "G. O. Young, \"Synthetic structure of industrial plastics,\" in Plastics, 2nd ed., vol. 3, J. Peters, Ed. New York, NY, USA: McGraw-Hill, 1964, pp. 15-64."


if (re.match(Ieee_Book,cadena)) != None:
    print(5)