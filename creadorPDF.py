from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle,PropertySet
from reportlab.lib.enums import *
from reportlab.lib.colors import *
def Titulo(c,tit):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Forma',alignment = TA_CENTER,
allowOrphans = 0,
allowWidows = 1,
backColor = None,
borderColor = None,
borderPadding = 0,
borderRadius = None,
borderWidth = 0,
bulletAnchor = "start",
bulletFontName = "Times-Roman",
bulletFontSize = 10,
bulletIndent = 0,
endDots = None,
firstLineIndent = 0,
fontName = "Times-Roman",
fontSize = 16,
justifyBreaks = 0,
justifyLastLine = 0,
leading = 12,
leftIndent = 0,
rightIndent = 0,
spaceAfter = 30,
spaceBefore = 0,
spaceShrinkage = 0.05,
splitLongWords = 1,
textColor = black,
textTransform = None,
underlineProportion = 0.0,
wordWrap = None))
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
    styles.add(ParagraphStyle(name='Forma1', alignment=TA_LEFT,
                              allowOrphans=0,
                              allowWidows=1,
                              backColor=None,
                              borderColor=None,
                              borderPadding=0,
                              borderRadius=None,
                              borderWidth=0,
                              bulletAnchor="start",
                              bulletFontName="Times-Roman",
                              bulletFontSize=10,
                              bulletIndent=0,
                              endDots=None,
                              firstLineIndent=40,
                              fontName="Times-Roman",
                              fontSize=12,
                              justifyBreaks=0,
                              justifyLastLine=0,
                              leading=12,
                              leftIndent=30,
                              rightIndent=0,
                              spaceAfter=10,
                              spaceBefore=5,
                              spaceShrinkage=0.05,
                              splitLongWords=1,
                              textColor=black,
                              textTransform=None,
                              underlineProportion=0.0,
                              wordWrap=None))
    p = Paragraph(str2, styles["Forma1"])
    aw = 550
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
