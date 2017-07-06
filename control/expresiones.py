import re
#Book IEEE
exp_pages = '(pp. )(([0-9]+)(-)([0-9]+)|[0-9]+)[.]'
exp_author = '^(([A-Z](. )){,2}[a-zA-Z]+|[a-zA-Z ]+)'
exp_coma = '[(,)([ ]+)]?'
exp_title = '((")[a-zA-Z ]+(,")( in )?[a-zA-Z ]+|[a-zA-Z ]+|(")[\w]+("))'
exp_year = '[0-9]+'
exp_chapter = '(ch. )[0-9]+'
exp_section = '(sec. )[0-9]+'
exp_edition = '[0-9]+[a-z]+[ ](ed;)'
exp_volume = '(vol. )[0-9]+'
exp_city='[a-zA-Z ]+'
exp_country = '[a-zA-Z ]+(:)[a-zA-Z ]+'
exp_state = '[A-Z]+'
exp_number = '(no. )[0-9]+'
exp_month = '[a-zA-Z]+(.)?[ ][0-9]+'
exp_articleNumber = '(Art. no. )[0-9]+'
libro = exp_author+exp_coma+exp_title+exp_coma+exp_city+exp_coma+exp_state+exp_coma+exp_country+exp_year+exp_coma+exp_chapter+exp_coma+exp_section+exp_pages
articulo = exp_author+exp_coma+exp_title+exp_coma+exp_volume+exp_coma+exp_number+exp_coma+exp_month+exp_year+exp_coma+exp_articleNumber
manual = exp_author+exp_coma+exp_title+exp_coma+exp_city+exp_coma+exp_state+exp_coma+exp_country+exp_coma+exp_year
conferencia = exp_author+exp_coma+exp_title+exp_coma+exp_city+exp_coma+exp_state+exp_coma+exp_country+exp_coma+exp_year
publicacion = exp_author+exp_coma+exp_title+exp_coma+exp_pages
#APA
apa_author= '[a-zA-Z]+'
apa_inicial= '[A-Z](.)'
apa_presidenteConferencia='(En )'+apa_inicial+'( )'+apa_author+'( )[\(](Presidenca)[\)]'
apa_tituloConferencia = '[a-zA-Z0-9\t]+'
apa_year= '[\(]([0-9]+[\)]|[a-zA-Z0-9\t]+)[\.]?'
apa_title = '[a-zA-Z\t]+[\.]?'
apa_cityCo= '[a-zA-Z\t]+'+exp_coma+'[a-zA-Z\t]+[:]'
apa_editorial= '[a-zA-Z\t]+[\.]?'
apa_nombreRevista= '[a-zA-Z\t]+[\.]?'
apa_page = '(pp. )(([0-9]+)(-)([0-9]+)|[0-9]+)[.]'
apa_volume = '([0-9]+)( )[\(][0-9]+[\)]'
apaLibro=apa_author+exp_coma+apa_inicial+exp_coma+apa_year+exp_coma+apa_title+exp_coma+apa_cityCo+apa_editorial
apaManual=
apaConferencia=apa_author+exp_coma+apa_inicial+apa_year+apa_title+exp_coma+apa_presidenteConferencia+apa_tituloConferencia+'((Simposio llevado a cabo en )|(Conferencia llevado a cabo en ))'+exp_coma+apa_cityCo
apaArticulo= '['+apa_author+exp_coma+apa_inicial+exp_coma+']*'+'(y )?'+apa_author+exp_coma+apa_inicial+exp_coma+apa_year+apa_title+apa_nombreRevista+exp_coma+apa_volume+exp_coma+apa_page
apaPublicacion=
#Ejemplo conferencia
#Rojas, C., & Vera, N. (Agosto de 2013). ABMS (Automatic BLAST for Massive Sequencing). En H. Castillo (Presidencia), 2° Congreso Colombiano de Biologia Computacional y Bioinformática CCBCOL. Congreso llevado a cabo en Manizales, Colombia.
#Ejemplo libro
#Hacyan, S., (2004), Física y metafísica en el espacio y el tiempo. La filosofía en el laboratorio, México DF, México: Fondo nacional de cultura económica.
#Ejemplo articulo
#Coruminas, M., Ronecro, C., Bruguca, E., y Casas, M. (2007). Sistema dopaminérgico y adicciones, Rev Mukuel, 44(1), 23-31.