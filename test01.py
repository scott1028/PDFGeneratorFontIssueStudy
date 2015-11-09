#!/usr/bin/env python
# coding:utf-8
"Make some simple multipage pdf files."

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('test', 'test.ttf'))
# pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSansCondensed.ttf'))

from reportlab.pdfgen import canvas
from sys import argv

# canvas.setFont('Vera', 32)
# canvas.drawString(10, 150, "Some text encoded in UTF-8")
# canvas.drawString(10, 100, "In the Vera TT Font!")

# from __future__ import print_function


point = 1
inch = 72

TEXT = """%s    page %d of %d
測試ñAä장あ张張
created with Sample_Code/makesimple.py"""


def make_pdf_file(output_filename, np):
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    c.setFont('test', 32)
    c.drawString(10, 150, "Some text encoded in UTF-8")
    c.drawString(10, 100, "In the Vera TT Font!")

    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12 * point)
    for pn in range(1, np + 1):
        v = 10 * inch
        for subtline in (TEXT % (output_filename, pn, np)).split( '\n' ):
            c.drawString( 1 * inch, v, subtline.decode('utf-8') )
            v -= 12 * point
        c.showPage()
    c.save()

if __name__ == "__main__":
    nps = [None, 5, 11, 17]
    for i, np in enumerate(nps):
        if np:
            filename = "test01_%d.pdf" % i
            make_pdf_file(filename, np)
            print ("Wrote", filename)
