from reportlab.lib.pagesizes import *
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

class PDF:
    def __init__(self, formato=A4, titulo="Nuevo PDF1", marca_agua=False, ruta="./"):
        self.formato = formato
        self.marca_agua = marca_agua
        self.pdf_path = os.path.join(ruta, f"{titulo}.pdf")  # Combina la ruta y el título
        self.pdf_width, self.pdf_height = landscape(self.formato)   
        self.c = canvas.Canvas(self.pdf_path, pagesize=landscape(self.formato))

    def crear_pagina(self, titulo, grafico):
        self.c.setTitle(titulo)
        
        # Establecer el título
        titulo_x = self.pdf_width / 2
        titulo_y = self.pdf_height - 50
        self.c.setFont("Helvetica-Bold", 26)
        self.c.drawCentredString(titulo_x, titulo_y, titulo)
        
        # Ajustar el gráfico para que ocupe toda la página
        self.c.drawImage(grafico.name, 0, 0, width=self.pdf_width, height=self.pdf_height - 50, showBoundary=False, preserveAspectRatio=True)

        # Guardar la página
        self.c.showPage()
        
    def guardar_pdf(self):
        self.c.save()
        print(f"PDF guardado en {self.pdf_path}")
