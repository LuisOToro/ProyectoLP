from control import  paperDirector
paperIeee = paperDirector.paperDirector(2,"mi titulo","pais","ciudad")

texto = "@article{mi article,  author  = {Peter Adams},   title   = {The title of the work},  journal = {The name of the journal},  year    = 1993,  number  = 2,  pages   = {201-213},  month   = 7,  note    = {An optional note},   volume  = 4}"

texto2 = "@conference{mis conference,  author       = {Peter Draper},   title        = {The title of the work},  booktitle    = {The title of the book},  year         = 1993,  editor       = {The editor},  volume       = 4,  series       = 5,  pages        = 213,  address      = {The address of the publisher},  month        = 7,  organization = {The organization},  publisher    = {The publisher},  note         = {An optional note}  }"

texto3 = "@book{mi book,  author    = {Peter Babington},   title     = {The title of the work},  publisher = {The name of the publisher},  year      = 1993,  volume    = 4,  series    = 10,  address   = {The address},  edition   = 3,  month     = 7,  note      = {An optional note},  isbn      = {3257227892}}"

texto4 = "@manual{mi manual,  title        = {The title of the work},  author       = {Peter Gainsford},   organization = {The organization},  address      = {The address of the publisher},  edition      = 3,  month        = 7,  year         = 1993,  note         = {An optional note}}"

texto5 = "@unpublished{mi unpublished,  author       = {Peter Marcheford},   title        = {The title of the work},  note         = {An optional note},  month        = 7,  year         = 1993}"


paperIeee.iniciarBibtex_compiler_add_referencias(5,texto5)
paperIeee.iniciarBibtex_compiler_add_referencias(4,texto4)
paperIeee.iniciarBibtex_compiler_add_referencias(3,texto2)
paperIeee.iniciarBibtex_compiler_add_referencias(2,texto3)
paperIeee.iniciarBibtex_compiler_add_referencias(1,texto)
