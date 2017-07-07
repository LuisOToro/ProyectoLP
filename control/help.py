def referencias_Bibtex_posibles():
    print("La referencia se la debe agregar toda en una sola linea\n\n\n")
    print("<--------Bibtex_Article-------->")
    print("""@article{article,
  author  = {Peter Adams}, 
  title   = {The title of the work},
  journal = {The name of the journal},
  year    = 1993,
  number  = 2,
  pages   = {201-213},
  month   = 7,
  note    = {An optional note}, 
  volume  = 4
}""")

    print("\n\n<--------Bibtex_Book-------->\n\n")
    print("""@book{book,
  author    = {Peter Babington}, 
  title     = {The title of the work},
  publisher = {The name of the publisher},
  year      = 1993,
  volume    = 4,
  series    = 10,
  address   = {The address},
  edition   = 3,
  month     = 7,
  note      = {An optional note},
  isbn      = {3257227892}
}""")

    print("\n\n<--------Bibtex_Conference-------->\n\n")
    print("""@conference{conference,
  author       = {Peter Draper}, 
  title        = {The title of the work},
  booktitle    = {The title of the book},
  year         = 1993,
  editor       = {The editor},
  volume       = 4,
  series       = 5,
  pages        = 213,
  address      = {The address of the publisher},
  month        = 7,
  organization = {The organization},
  publisher    = {The publisher},
  note         = {An optional note}  
}""")

    print("\n\n<--------Bibtex_Manual-------->\n\n")
    print("""@manual{manual,
  title        = {The title of the work},
  author       = {Peter Gainsford}, 
  organization = {The organization},
  address      = {The address of the publisher},
  edition      = 3,
  month        = 7,
  year         = 1993,
  note         = {An optional note}
}""")

    print("\n\n<--------Bibtex_Publicacion-------->\n\n")
    print("""@unpublished{unpublished,
  author       = {Peter Marcheford}, 
  title        = {The title of the work},
  note         = {An optional note},
  month        = 7,
  year         = 1993
}
 """)

referencias_Bibtex_posibles()