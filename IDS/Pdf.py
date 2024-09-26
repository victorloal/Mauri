from reportlab.lib.pagesizes import * 
from reportlab.pdfgen import canvas
from reportlab.lib import colors



class PDF:
    def __init__(self, formato=A4, titulo="Nuevo PDF1", marca_agua=False):
        self.formato = formato
        self.marca_agua = marca_agua
        self.pdf_path = f"{titulo}.pdf"
        self.pdf_width, self.pdf_height = landscape(self.formato)   
        self.c = canvas.Canvas(self.pdf_path, pagesize=landscape(self.formato))
        
    def crear_pagina(self,titulo,grafico,tabla):
        self.c.setTitle(titulo)
        titulo_x = self.pdf_width / 2 
        titulo_y = self.pdf_height - 50
        self.c.setFont("Helvetica-Bold", 26)
        self.c.drawCentredString(titulo_x, titulo_y, titulo)
        # Agregar la figura de Matplotlib al PDF
        self.c.drawImage(grafico.name, titulo_x-300, ((self.pdf_height/2)-225), width=600, height=450 ,  showBoundary=False , preserveAspectRatio=True)
        # Agregar una tabla con los datos debajo de la gráfica
        table = tabla
        table.setStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightcoral),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        
        # Obtener el ancho de la tabla
        table_width, _ = table.wrap(0, 0)
        x = (self.pdf_width - table_width) / 2

        # Dibujar la tabla en el PDF
        table.wrapOn(self.c, 500, 500)
        table.drawOn(self.c, x, 50)
        # Guardar la página
        self.c.showPage()
        
    def guardar_pdf(self):
        self.c.save()
        print(f"PDF guardado en {self.pdf_path}")
