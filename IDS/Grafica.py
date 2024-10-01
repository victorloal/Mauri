import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import tempfile
from IDS import Pdf

# Definición de colores
def get_color(value):
    if value < 2:
        return 'rgb(255, 0, 0)'  # Rojo
    elif value < 4:
        return 'rgb(255, 165, 0)'  # Naranja
    elif value < 6:
        return 'rgb(255, 255, 0)'  # Amarillo
    elif value < 8:
        return 'rgb(93, 173, 226)'  # Azul
    else:
        return 'rgb(0, 255, 0)'  # Verde

# Clasificación del estado
def get_status(value):
    if value >= 8:
        return "Óptimo"
    elif value >= 6:
        return "Estable"
    elif value >= 4:
        return "Inestable"
    elif value >= 2:
        return "Crítico"
    else:
        return "Colapso"

class Grafica:
    def __init__(self, names, values, result_value):
        self.df = pd.DataFrame(dict(
            theta=names,
            r=values   
        ))
        self.result_value = result_value
        self.status = get_status(result_value)
        self.calculate_intervention()
        self.create_figures()

    def calculate_intervention(self):
        self.df['Diferencia'] = 10 - self.df['r']
        total_difference = self.df['Diferencia'].sum()

        if total_difference > 0:
            self.df['Intervención (%)'] = (self.df['Diferencia'] / total_difference) * 100
            self.df['Intervención (%)'] = self.df['Intervención (%)'].round(2)
        else:
            self.df['Intervención (%)'] = 0

        self.df.sort_values(by='r', ascending=True, inplace=True)

    def create_figures(self):
        self.fig = make_subplots(
            rows=1, cols=2,
            specs=[[{"type": "table"}, {"type": "scatterpolar"}]],
            column_widths=[0.4, 0.6]
        )

        # Colores para la tabla
        fill_colors_values = [get_color(val) for val in self.df['r']]
        fill_colors_intervention = ['lightgrey' for _ in self.df['Intervención (%)']]

        # Añadir la tabla
        self.fig.add_trace(go.Table(
            header=dict(
                values=['<b>Nombres</b>', '<b>Valores</b>', '<b>Intervención (%)</b>'],
                line_color='black',
                fill_color='white',
                align='center', font=dict(color='black', size=12)
            ),
            
            cells=dict(
                values=[self.df['theta'].tolist() + ['Resultado'], 
                        self.df['r'].tolist() + [self.result_value], 
                        self.df['Intervención (%)'].tolist() + [self.df['Intervención (%)'].sum()]],
                line_color='black',
                fill_color=[fill_colors_values + ['lightgrey'], 
                            fill_colors_values + ['lightgrey'], 
                            fill_colors_intervention + ['lightgrey']],
                align='center', font=dict(color='black', size=11)
            )
        ), row=1, col=1)

        # Añadir la gráfica de radar
        self.fig.add_trace(go.Scatterpolar(
            r=self.df['r'].tolist() + [self.df['r'].iloc[0]],  # Cerramos el ciclo
            theta=self.df['theta'].tolist() + [self.df['theta'].iloc[0]],
            fill='toself',
            name='Gráfica de Radar',
            line=dict(color=get_color(self.result_value))
        ), row=1, col=2)

        # Añadir el estado como anotación
        self.fig.add_annotation(
            text=self.status,
            showarrow=False,
            xref='paper', yref='paper',
            x=1, y=0,  # Colocamos la anotación debajo de la gráfica
            font=dict(size=16, color=get_color(self.result_value))
        )

        # Ajustar el tamaño de la figura
        self.fig.update_layout(
            width=1200,
            height=600,
            polar=dict(
                radialaxis=dict(range=[0, 10])
            )
        )

    def get_png(self):
        try:
            img_bytes = self.fig.to_image(format="png")
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_img:
                temp_img.write(img_bytes)
            return temp_img
        except Exception as e:
            pass

    def show(self):
        self.fig.show()

