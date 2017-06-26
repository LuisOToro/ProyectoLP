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