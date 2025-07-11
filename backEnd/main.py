import sys
import matplotlib.pyplot as plt
from metodosNumericos import MetodosNumericos

class Main:
    def __init__(self, file):
        self.file = file
        self.metodo = MetodosNumericos(file)


    def run(self):
        datos = self.metodo.open_file.data()
        try:
            coeficientes, y_ajustada, error = self.metodo.solution()
            x = datos[0]
            y = datos[1]
            # x_sorted, y_sorted = zip(*sorted(zip(x, y_ajustada))) no es necesario usar pero si hay problemas si.

            # Graficar los datos originales
            plt.figure(figsize=(10, 6))
            plt.scatter(x, y, color='blue', label='Datos originales')
            plt.plot(x, y_ajustada, color='red', label='Curva ajustada', linewidth=2)
            plt.title('Regresión por mínimos cuadrados')
            plt.xlabel('High')
            plt.ylabel('Low')
            plt.legend()
            plt.grid()
            plt.show()

            print("Coeficientes:", coeficientes)
            print("Error cuadrático medio:", error)
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
    else:
        file = sys.argv[1]
        app = Main(file)
        app.run()