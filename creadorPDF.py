from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle,PropertySet
from reportlab.lib.enums import *
from reportlab.lib.colors import *
def Titulo(c,tit):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Forma',alignment = TA_CENTER,bulletAnchor = "start", bulletFontName = "Times-Roman",
    bulletFontSize = 10,fontName = "Times-Roman", fontSize = 16, spaceAfter = 30, spaceBefore = 0,))
    p = Paragraph(tit, styles["Forma"])
    aw = 550
    ah = 770
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(c, 0, ah)
        ah = ah - h
    else:
        raise ValueError
def Texto(str1,str2):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Forma1', alignment=TA_LEFT, bulletAnchor="start", bulletFontName="Times-Roman", bulletFontSize=10,
    firstLineIndent=35, fontName="Times-Roman", fontSize=12, leftIndent=30, spaceAfter=10, spaceBefore=5))
    p = Paragraph(str2, styles["Forma1"])
    aw = 500
    ah = 750 - p.getSpaceAfter()
    w, h = p.wrap(aw, ah)
    if w <= aw and h <= ah:
        p.drawOn(str1, 30, ah)
        ah = ah - h
    else:
        raise ValueError
def Generar(str1,str2,str3):
    # nombre del archivo sin .pdf, titulo, texto
    c = canvas.Canvas(str1 + ".pdf")
    Titulo(c,str2)
    Texto(c,str3)
    c.save()
