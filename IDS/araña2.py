import plotly.graph_objects as go
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
import tempfile
import os

# Configuración de la tabla
headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

# Crear la figura con la tabla
fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>EXPENSES</b>', '<b>Q1</b>', '<b>Q2</b>', '<b>Q3</b>', '<b>Q4</b>'],
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left', 'center'],
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[
            ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
            [1200000, 20000, 80000, 2000, 12120000],
            [1300000, 20000, 70000, 2000, 130902000],
            [1300000, 20000, 120000, 2000, 131222000],
            [1400000, 20000, 90000, 2000, 14102000]
        ],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor] * 5],
        align=['left', 'center'],
        font=dict(color='darkslategray', size=11)
    ))
])

# Guardar la figura como imagen temporal
temp_img_path = tempfile.mktemp(suffix='.png')
fig.write_image(temp_img_path)

# Crear un documento PDF
pdf_path = "tabla.pdf"
c = canvas.Canvas(pdf_path, pagesize=landscape(letter))
c.setTitle("Tabla de gastos")

# Dimensiones del PDF
pdf_width, pdf_height = landscape(letter)

# Tamaño de la imagen
img_width, img_height = 600, 400

# Coordenadas para centrar la imagen en el PDF
img_x = (pdf_width - img_width) / 2
img_y = (pdf_height - img_height) / 2

# Dibujar la imagen en el PDF
c.drawImage(temp_img_path, img_x, img_y, width=img_width, height=img_height)

# Guardar el PDF
c.save()

# Eliminar el archivo temporal de la imagen
os.remove(temp_img_path)

print(f"PDF guardado en {pdf_path}")
