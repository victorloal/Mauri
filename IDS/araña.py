import numpy as np
import matplotlib.pyplot as plt

# Definir las categorías y los valores para cada categoría
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [4, 3, 2, 5, 4]

# Escalar los valores al rango de 0 a 10
valores = [(v * 10.0) / max(valores) for v in valores]

# Calcular el ángulo para cada categoría
num_categorias = len(categorias)
angulos = np.linspace(0, 2 * np.pi, num_categorias, endpoint=False).tolist()

# Añadir el primer ángulo al final para cerrar el gráfico
angulos += angulos[:1]

# Preparar los valores para cerrar el gráfico
valores += valores[:1]

# Crear la gráfica de araña
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(angulos, valores, color='skyblue', linewidth=3, linestyle='solid')

# Rellenar el área debajo de la línea
ax.fill(angulos, valores, color='skyblue', alpha=0.4)

# Añadir etiquetas a cada categoría
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(categorias)

# Establecer el rango de las etiquetas del eje radial de 0 a 10
ax.set_ylim(0, 10)

# Mostrar la gráfica
plt.show()
