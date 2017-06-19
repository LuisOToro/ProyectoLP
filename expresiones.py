import re
#Book IEEE
exp_pages = '(pp. )(([0-9]+)(-)([0-9]+)|[0-9]+)'
exp_author = '^([A-Z](. )){,2}[a-zA-Z]+'
exp_coma = '[,][ ]+'
exp_title = '((")[a-zA-Z ]+(,")( in )[a-zA-Z ]+|[a-zA-Z ]+)'
exp_year = '[0-9]+'
exp_chapter = '(ch. )[0-9]+'
exp_section = '(sec. )[0-9]+'
exp_edition = '[0-9]+[a-z]+[ ](ed)'
exp_volume = '(vol. )[0-9]+'
exp_city='[a-zA-Z ]+'
exp_country = '[a-zA-Z ]+(: )[a-zA-Z]+'
exp_state = '[A-Z]+'

