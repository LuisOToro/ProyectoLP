from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak,CondPageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm
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
h1 = PS(name = 'Heading1',
 fontSize = 14,
 leading = 16)
h2 = PS(name = 'Heading2',
    fontSize = 12,
    leading = 14)
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
doc = MyDocTemplate('mintoc.pdf')
doc.multiBuild(story)
