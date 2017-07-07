from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak,CondPageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm
from reportlab.platypus.paragraph import TA_RIGHT, TA_CENTER, TA_JUSTIFY, TA_LEFT, _FK_BREAK
from reportlab.lib.styles import _baseFontNameB, _baseFontNameBI, _baseFontNameI
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet

class MyDocTemplate(BaseDocTemplate):
 def __init__(self, filename, **kw):
    self.allowSplitting = 0
    BaseDocTemplate.__init__(self, filename, **kw)
    template = PageTemplate('normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
    self.addPageTemplates(template)
 def afterFlowable(self, flowable):
    "Registers TOC entries."
    if flowable.__class__.__name__ == 'Paragraph':
        text = flowable.getPlainText()
        style = flowable.style.name
        if style == 'Heading1':
            self.notify('TOCEntry', (0, text, self.page))
        if style == 'Heading2':
            self.notify('TOCEntry', (1, text, self.page))
#Fuente: https://www.reportlab.com/docs/reportlab-userguide.pdf pag 28 para cursiva, pagina 72 para centralizar

h1 = PS(name = 'Heading1',
 fontSize = 14,
 leading = 16,
fontName=_baseFontNameBI
    )
h2 = PS(name = 'Heading2',
    fontSize = 12,
    leading = 14)

h3 = PS(name = 'titulo',fontSize = 20,leading = 22,alignment =  TA_CENTER,fontName=_baseFontNameBI)
h4 = PS(name = 'sub1', fontSize = 10,leading = 12)
h5 = PS(name = 'primeraPagina', fontSize = 16, leading = 18,alignment =  TA_CENTER)
h6 = PS(name = 'negritaCursiva', fontSize = 14,alignment =  TA_CENTER,fontName=_baseFontNameBI)
h7 = PS(name= 'cuerpo', fontSize = 12, alignment = TA_JUSTIFY, fontName=_baseFontNameB)
h8 = PS(name= 'cuerpo2', fontSize = 12, alignment = TA_JUSTIFY)
h9 = PS(name= 'cuerpo3', fontSize = 12, alignment = TA_JUSTIFY, fontName=_baseFontNameB, )

#con alignment puedes elegir su posicionamiento, son constantes y son: centrado( TA_CENTER), justificado(TA_JUSTIFY), por la derecha(TA_RIGHT) Y por
#la izquierda(TA_LEFT)
#En fontName puedes elegir entre negrita y cursiva(_baseFontNameBI), negrita(_baseFontNameB) o cursiva (_baseFontNameI)
# Build story.
story = []
toc = TableOfContents()
# For conciseness we use the same styles for headings and TOC entries
toc.levelStyles = [h1, h2]
story.append(toc)
story.append(PageBreak())
story.append(Paragraph('First heading', h1))
story.append(Paragraph('Text in first heading', PS('body')))
story.append(Paragraph('First sub heading', h2))
story.append(Paragraph('''Text in first sub heading,ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL
FACULTAD DE INGENIERÍA EN ELECTRICIDAD Y COMPUTACIÓN
SISTEMAS DE BASES DE DATOS I
PRIMERA EVALUACIÓN - II TÉRMINO 2015-2016
Nombre: _____________________________________________ Matrícula: _____________ Paralelo: _____
Sección 1 (20%):
Desarrolle el modelo conceptual del siguiente modelo de negocios.
A usted, como parte del grupo de desarrollo de la empresa MYSOFT, le han pedido que diseñe una base de datos para un cliente que se dedica a rentar villas vacacionales. Dentro de los requerimientos, el cliente ha pedido que sea una aplicación web y que cumpla con las siguientes características:
Villa: Cada villa tiene un nombre, un id único, una imagen, año de construcción, edad, y algunas características especiales de la siguiente lista: piscina, Jacuzzi, mesa de billar, juegos de mesa, permite mascotas. Una villa puede ser rentada por un precio que puede variar cada noche. Una villa tiene solo un propietario.
Usuario: Un usuario puede suscribirse al sitio web y alquilar villas. Un usuario tiene nombre, apellido, id único, email y DoB. Un usuario tiene asociada una lista de villas favoritas y él puede decidir después si reservarlas o no. Al rentar una villa, un usuario declara la fecha de inicio y fecha de fin de la reservación. El usuario ingresa a la villa en la fecha de inicio antes mencionada y deja la villa al medio día de la fecha de fin. Para completar la reservación online, un usuario tiene que hacer un depósito no reembolsable del 50% de el precio final calculado. El usuario debe pagar el saldo al dueño de la villa en el momento de ingreso a la villa.
Reseña: Un usuario puede escribir reseñas sobre las villas que ha rentado antes. Una reseña contiene un rating (1-5) donde 5 es el mejor rating y un comentario que describe la experiencia del usuario durante su estadía.
Propietario: Es un usuario, quien es dueño de una o más villas. Tiene un número celular asociado. El propietario como cualquier otro usuario puede reservar villas. Además el propietario puede eliminar y agregar villas a la lista de villas que posee. Para propósitos de auditoría, la fecha de cualquier modificación debe ser registrada en el sistema. Un propietario puede definir nuevas características y añadirlas a la lista de características de la villa. El propietario define el precio de estadía por noche para diferentes períodos de tiempo (definido por una fecha inicio y fecha fin)
NOTA:
 No olvide que en su modelo conceptual deben constar las entidades, atributos, cardinalidades de entidades y relaciones, relaciones y nombres de las relaciones.
 Utilice la información de la sección 3 para realizar el modelo conceptual.
Sección 2 (30%):
A partir del modelo conceptual de la sección 1, grafique el modelo lógico completamente normalizado.
NOTA:
● No olvide que en su modelo lógico normalizado deben constar las tablas, 
1
ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL
FACULTAD DE INGENIERÍA EN ELECTRICIDAD Y COMPUTACIÓN
SISTEMAS DE BASES DE DATOS I
PRIMERA EVALUACIÓN - II TÉRMINO 2015-2016
Nombre: _____________________________________________ Matrícula: _____________ Paralelo: _____
Sección 1 (20%):
Desarrolle el modelo conceptual del siguiente modelo de negocios.
A usted, como parte del grupo de desarrollo de la empresa MYSOFT, le han pedido que diseñe una base de datos para un cliente que se dedica a rentar villas vacacionales. Dentro de los requerimientos, el cliente ha pedido que sea una aplicación web y que cumpla con las siguientes características:
Villa: Cada villa tiene un nombre, un id único, una imagen, año de construcción, edad, y algunas características especiales de la siguiente lista: piscina, Jacuzzi, mesa de billar, juegos de mesa, permite mascotas. Una villa puede ser rentada por un precio que puede variar cada noche. Una villa tiene solo un propietario.
Usuario: Un usuario puede suscribirse al sitio web y alquilar villas. Un usuario tiene nombre, apellido, id único, email y DoB. Un usuario tiene asociada una lista de villas favoritas y él puede decidir después si reservarlas o no. Al rentar una villa, un usuario declara la fecha de inicio y fecha de fin de la reservación. El usuario ingresa a la villa en la fecha de inicio antes mencionada y deja la villa al medio día de la fecha de fin. Para completar la reservación online, un usuario tiene que hacer un depósito no reembolsable del 50% de el precio final calculado. El usuario debe pagar el saldo al dueño de la villa en el momento de ingreso a la villa.
Reseña: Un usuario puede escribir reseñas sobre las villas que ha rentado antes. Una reseña contiene un rating (1-5) donde 5 es el mejor rating y un comentario que describe la experiencia del usuario durante su estadía.
Propietario: Es un usuario, quien es dueño de una o más villas. Tiene un número celular asociado. El propietario como cualquier otro usuario puede reservar villas. Además el propietario puede eliminar y agregar villas a la lista de villas que posee. Para propósitos de auditoría, la fecha de cualquier modificación debe ser registrada en el sistema. Un propietario puede definir nuevas características y añadirlas a la lista de características de la villa. El propietario define el precio de estadía por noche para diferentes períodos de tiempo (definido por una fecha inicio y fecha fin)
NOTA:
 No olvide que en su modelo conceptual deben constar las entidades, atributos, cardinalidades de entidades y relaciones, relaciones y nombres de las relaciones.
 Utilice la información de la sección 3 para realizar el modelo conceptual.
Sección 2 (30%):
A partir del modelo conceptual de la sección 1, grafique el modelo lógico completamente normalizado.
NOTA:
● No olvide que en su modelo lógico normalizado deben constar las tablas, columnas, tipos de datos, claves primarias, claves foráneas, campos obligatorios, campos opcionales y''', PS('body')))
story.append(CondPageBreak(height=50))
story.append(PageBreak())
story.append(Paragraph('Second sub heading', h2))
story.append(Paragraph('Text in second sub heading', PS('body')))
story.append(Paragraph('Last heading', h1))
story.append(PageBreak())
story.append(Paragraph('Mi intento',h6))
doc = MyDocTemplate('mintoc.pdf')
doc.multiBuild(story)

def paperIee(nombreDocumento,resumenpdf,autores,autoresC,lugar,mail,intro,cuerpopdf,recomendaciones,conclusiones,referencias,titulo):
    mipaper = []
    mipaper.append(Paragraph(titulo, h3))
    mipaper.append(Paragraph(autores, h5))
    mipaper.append(Paragraph(autoresC, h5))
    mipaper.append(Paragraph(lugar, h5))
    mipaper.append(Paragraph(mail, h5))

    mipaper.append(Paragraph("Abstract",h1))
    for i in range(len(resumenpdf)):
        mipaper.append(Paragraph(resumenpdf[i],h7))


    mipaper.append(Paragraph("1.- Introduccion",h1))
    for i in range(len(intro)):
        mipaper.append(Paragraph(intro[i], h8))
    mipaper.append(PageBreak())

    mipaper.append(Paragraph("2.- Estado del arte", h1))
    for i in range(len(cuerpopdf)):
        mipaper.append(Paragraph(cuerpopdf[i], h8))

    mipaper.append(Paragraph("3.- Recomendaciones", h1))
    for i in range(len(recomendaciones)):
        mipaper.append(Paragraph(recomendaciones[i], h8))

    mipaper.append(Paragraph("4.- Conclusiones", h1))
    for i in range(len(conclusiones)):
        mipaper.append(Paragraph(conclusiones[i], h8))

    mipaper.append(Paragraph("5.- Referencias", h1))
    for i in range(len(referencias)):
        mipaper.append(Paragraph("["+str(i+1)+"] "+referencias[i],h8))

    doc = MyDocTemplate(nombreDocumento)
    doc.multiBuild(mipaper)


def paperApa(nombreDocumento,titulo,autores,autoresC,lugar,mail,resumenpdf,intro,cuerpopdf,recomendaciones,conclusiones,referencias):
    miPaperApa = []
    miPaperApa.append(Paragraph(titulo,h3))
    miPaperApa.append(Paragraph(autores,h5))
    miPaperApa.append(Paragraph(autoresC, h5))
    miPaperApa.append(Paragraph(lugar, h5))
    miPaperApa.append(Paragraph(mail, h5))
    miPaperApa.append(PageBreak())
    miPaperApa.append(toc)
    miPaperApa.append(PageBreak())
    miPaperApa.append(Paragraph("Abstract(Resumen).", h1))
    miPaperApa.append(Paragraph("    ",PS('body')))
    for i in range(len(resumenpdf)):
        miPaperApa.append(Paragraph(resumenpdf[i],h7))
    miPaperApa.append(PageBreak())
    miPaperApa.append(Paragraph("Introduccion", h1))
    for i in range(len(intro)):
        miPaperApa.append(Paragraph(intro[i], h8))
    miPaperApa.append(PageBreak())
    miPaperApa.append(Paragraph("Estado del arte", h1))
    for i in range(len(cuerpopdf)):
        miPaperApa.append(Paragraph(cuerpopdf[i], h8))

    miPaperApa.append(Paragraph("Recomendaciones", h1))
    for i in range(len(recomendaciones)):
        miPaperApa.append(Paragraph(recomendaciones[i], h8))

    miPaperApa.append(Paragraph("Conclusiones", h1))
    for i in range(len(conclusiones)):
        miPaperApa.append(Paragraph(conclusiones[i], h8))
    miPaperApa.append(PageBreak())
    miPaperApa.append(Paragraph("Referencias", h1))
    for i in range(len(referencias)):
        miPaperApa.append(Paragraph("["+str(i+1)+"] "+referencias[i],h8))
    doc = MyDocTemplate(nombreDocumento)
    doc.multiBuild(miPaperApa)

