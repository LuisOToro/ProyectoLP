from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle,PropertySet
from reportlab.lib.enums import *
from reportlab.lib.colors import *
from reportlab.lib.pagesizes import A4

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
Generar("mi ide","este es mi titulo","este es el tetxo del cuerpo","jiquinta@espol.edu.ec","Jonathan Quintana","mipost")
