
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
w, h = letter
c = canvas.Canvas("figuras.pdf", pagesize=letter)
c.drawString(30, h - 50, "Línea")
x = 120
y = h - 45
c.line(x, y, x + 100, y)
c.drawString(30, h - 100, "Rectángulo")
c.rect(x, h - 120, 100, 50)
c.drawString(30, h - 170, "Círculo")
c.circle(170, h - 165, 20)
c.drawString(30, h - 240, "Elipse")
c.ellipse(x, y - 170, x + 100, y - 220)
c.showPage()
c.save()