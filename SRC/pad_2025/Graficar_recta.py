import numpy as np
import matplotlib.pyplot as plt

def graficar_rectas(*polinomios, colores=None, rango=(-5, 5), num_puntos=500, limite_y=(-20, 20)):
    x = np.linspace(rango[0], rango[1], num_puntos)
    plt.figure(figsize=(8, 6))

    if colores is None:
        colores = ['b', 'r', 'g', 'm', 'c', 'y', 'k']  

    for i, (a, n) in enumerate(polinomios):
        color = colores[i % len(colores)]  
        y = a * x**n
        plt.plot(x, y, label=f'$f(x) = {a}x^{n}$', color=color, linewidth=2)

    # Configuración de ejes y cuadrícula
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráficar_rectas')

    # Definir los intervalos del eje X e Y
    plt.xticks(np.arange(rango[0], rango[1] + 1, 1))  
    plt.yticks(np.arange(limite_y[0], limite_y[1] + 1, 5))  
    plt.ylim(limite_y)  
    plt.show()

colores_personalizados = ['red', 'blue', 'green', 'purple']
graficar_rectas((4, 2), (-3, 2), (0.5, 5), (2, 1), colores=colores_personalizados, limite_y=(-20, 20))
