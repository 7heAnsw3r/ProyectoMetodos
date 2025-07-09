import sys
import matplotlib.pyplot as plt
from metodosNumericos import MetodosNumericos
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("Por favor usar de la siguiente forma: python main.py <filename>")
        sys.exit(1)
    file = sys.argv[1]

    metodo = MetodosNumericos(file)
    metodo.open_file.open()

    try:
        coeficientes, curva, error = metodo.solution()
        x = metodo.data[0]  # Valores independientes (High)
        y = metodo.data[1]  # Valores dependientes (Low)

        # Ordenar x y curva para graficar línea suave
        orden = np.argsort(x)
        x_ordenado = np.array(x)[orden]

        # Graficar datos originales
        plt.scatter(x, y, color='blue', label='Datos originales', alpha=0.6, s=20)

        # Graficar curva ajustada (línea continua)
        plt.plot(x_ordenado, curva, color='red', label='Curva ajustada', linewidth=2)

        # Ajustar límites para que no quede tan disperso
        plt.xlim(min(x) * 0.95, max(x) * 1.05)
        plt.ylim(min(y) * 0.95, max(y) * 1.05)

        # Configurar ticks más legibles, por ejemplo 10 ticks en X y Y
        plt.xticks(np.linspace(min(x), max(x), 10))
        plt.yticks(np.linspace(min(y), max(y), 10))

        plt.title('Regresión por mínimos cuadrados')
        plt.xlabel('High')
        plt.ylabel('Low')
        plt.legend()
        plt.grid(True)

        plt.show()

        print("Coeficientes:", coeficientes)
        print("Error cuadrático medio:", error)

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

main()
