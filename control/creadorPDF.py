from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle,PropertySet
from reportlab.lib.enums import *
from reportlab.lib.colors import *
from reportlab.lib.pagesizes import A4
from reportlab.platypus.flowables import *

def IdPost(StrID,canvas):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='aligment-left', alignment=TA_LEFT,fontName = "Times-Roman", fontSize = 10))
    p = Paragraph(StrID, styles["aligment-left"])
    p.wrap(550,820)
    p.drawOn(canvas, 30, 810)

def Autor (Strauto,canvas,altura):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='autort', alignment=TA_CENTER, fontName="Times-Roman", fontSize=10))
    p = Paragraph(Strauto, styles["autort"])
    aw = 550
    ah = altura-20 - p.getSpaceAfter()
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(canvas, 0, ah)
        ah = ah - h
    else:
        raise ValueError
    return ah

def Mail(correo,canvas,altura):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='correo', alignment=TA_CENTER, bulletAnchor="start", bulletFontName="Times-Roman",
                              bulletFontSize=10, fontName="Times-Roman", fontSize=10, spaceAfter=30, spaceBefore=0, ))
    p = Paragraph(correo, styles["correo"])
    aw = 550
    ah = altura+20 - p.getSpaceAfter()
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(canvas, 0, ah)
        ah = ah - h
    else:
        raise ValueError
    return ah


def Titulo(canvas,titulo):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Forma',alignment = TA_CENTER,bulletAnchor = "start", bulletFontName = "Times-Roman",
    bulletFontSize = 10,fontName = "Times-Roman", fontSize = 16, spaceAfter = 30, spaceBefore = 0,))
    p = Paragraph(titulo, styles["Forma"])
    aw = 550
    ah = 820 - p.getSpaceAfter()
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(canvas, 0, ah)
        ah = ah - h
    else:
        raise ValueError
    return ah

def Texto(canvas,texto,altura):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Forma1', alignment=TA_LEFT, bulletAnchor="start", bulletFontName="Times-Roman", bulletFontSize=10,
    firstLineIndent=35, fontName="Times-Roman", fontSize=12, leftIndent=30, spaceAfter=10, spaceBefore=5))
    p = Paragraph(texto, styles["Forma1"])
    aw = 550
    ah = altura - p.getSpaceAfter()
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(canvas, 0, ah)
        ah = ah - h
    else:
        raise ValueError




def Generar(idPost,title,texto1,mail,autor,nombrePost):
    # nombre del archivo sin .pdf, titulo, texto
    c = canvas.Canvas(nombrePost + ".pdf")
    IdPost(idPost, c)
    ahT = Titulo(c,title)
    ahA = Autor(autor,c,ahT)
    ahM = Mail(mail,c,ahA)
    Texto(c,texto1,ahM)

    c.save()

#Generar("pdfdeprueba","titulo principal","este es el texto del cuerpo")
Generar("mi ide","este es mi titulo",'''1
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
● No olvide que en su modelo lógico normalizado deben constar las tablas, columnas, tipos de datos, claves primarias, claves foráneas, campos obligatorios, campos opcionales y''',"jiquinta@espol.edu.ec","Jonathan Quintana","mipost")
