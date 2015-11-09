# coding: utf-8


from reportlab.pdfgen import canvas

# regis font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('TestFont', 'unifont.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont', 'NotoSans-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont', 'ARIALUNI.TTF'))
# addMapping('TestFont', 0, 0, 'TestFont')


# start to gen pdf
pdf = canvas.Canvas("test04.pdf")
pdf.setFont('TestFont', 14)


pdf.drawString(10, 100, 'nglish: Hello World') # func(x, y, text)
pdf.drawString(10, 120, 'reek: Γειά σου κόσμος')
pdf.drawString(10, 140, 'olish: Witaj świecie')
pdf.drawString(10, 160, 'ortuguese: Olá mundo')
pdf.drawString(10, 180, 'ussian: Здравствуй, Мир')
pdf.drawString(10, 200, 'ietnamese: Xin chào thế giới')
pdf.drawString(10, 220, 'rabic: مرحبا العالم')
pdf.drawString(10, 240, 'ebrew: שלום עולם')
pdf.drawString(10, 260, 'ix: 測試ñAä장あ张張')
pdf.save()
