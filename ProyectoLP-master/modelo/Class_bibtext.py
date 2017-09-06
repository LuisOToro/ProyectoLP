class Bibtex_Article:

    def __init__(self,nombreA,autor,titulo,journal,anio,numero,pagina,mes,nota,volumen):
        self.autor = autor
        self.titulo = titulo
        self.journal = journal
        self.anio = anio
        self.numero = numero
        self.pagina = pagina
        self.mes = mes
        self.nota = nota
        self.volumen = volumen
        self.nombreArticulo = nombreA


class Bibtex_Book:

    def __init__(self,nameLibro,autor,titulo,publisher,anio,volumen,series,direccion,edicion,mes,nota,isbn):
        self.nameBook = nameLibro
        self.autor = autor
        self.titulo = titulo
        self.publisher = publisher
        self.anio = anio
        self.volumen = volumen
        self.series = series
        self.direccion = direccion
        self.edicion = edicion
        self.mes = mes
        self.nota = nota
        self.isbn = isbn


class Bibtex_Conference:

    def __init__(self,nombreConf,autor,titulo,bookTitle,anio,editor,volumen,series,paginas,direccion,mes,organizacion,publisher,nota):
        self.nameConference = nombreConf
        self.autor = autor
        self.titulo = titulo
        self.booktitle = bookTitle
        self.anio = anio
        self.editor = editor
        self.volumen = volumen
        self.series = series
        self.paginas = paginas
        self.direccion = direccion
        self.mes = mes
        self.organizacion = organizacion
        self.publisher = publisher
        self.nota = nota


class Bibtex_Manual:

    def __init__(self,titulo,autor,organizacion,direccion,edicion,mes,anio,nota,nombre):
        self.titulo = titulo
        self.autor = autor
        self.organizacion = organizacion
        self.direccion = direccion
        self.nombre = nombre
        self.edicion = edicion
        self.mes = mes
        self.anio = anio
        self.nota = nota


class Bibtex_Publicacion:

    def __init__(self,nombre,autor,titulo,nota,mes,anio):
        self.nombre = nombre
        self.autor = autor
        self.titulo = titulo
        self.nota = nota
        self.mes = mes
        self.anio = anio