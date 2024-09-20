import plotly.express as px
import pandas as pd
import tempfile
import Pdf

from reportlab.platypus import Table

class Grafica:
    def __init__(self, names, values,color):
        self.df = pd.DataFrame(dict(
            theta=names,
            r=values   
        ))
        # Creación de la gráfica de radar con Plotly Express
        self.fig = px.line_polar(self.df, r='r', theta='theta', line_close=True, range_r=[0, 10])
        # Establecer el relleno y color de la línea
        self.fig.update_traces(line_color=color, fill='toself', fillcolor='rgba(255, 0, 0, 0.15)')  

    def get_png(self):
        mpl_fig = self.fig.to_image(format="png", scale=3)
        # Guardar la imagen en un archivo temporal
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_img:
            temp_img.write(mpl_fig)
        return temp_img
    
    def get_tabla(self):
        df_transposed = self.df.transpose()

        # Agregar una tabla con los datos debajo de la gráfica
        data = df_transposed.values.tolist()
        table = Table(data)
        return table


grafica = Grafica(["valor 1","valor 2","valor","valor 4","valor 5","valor 6","valor 7","valor 8","valor 9","valor 10","valor 11","valor 12","valor 13","valor 14","valor 15","valor 16"],[1, 2, 2, 2, 2.5, 9, 5, 5, 5,2,2,2,2,2,2,2],'red')
pdf = Pdf.PDF()
img = grafica.get_png()
pdf.crear_pagina("Titulo probicional de la gráfica de radar",img,grafica.get_tabla())
pdf.crear_pagina("Titulo probicional de ",img,grafica.get_tabla())
pdf.guardar_pdf()