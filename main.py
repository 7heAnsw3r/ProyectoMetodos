import sys
import matplotlib.pyplot as plt
from backEnd import MetodosNumericos

class Main:
    def __init__(self, file):
        self.file = file
        self.metodo = MetodosNumericos(file)


    def run(self):
        datos = self.metodo.open_file.data()
        try:
            # Mínimos cuadrados
            coeficientes, y_ajustada, error = self.metodo.solution()
            x = datos[0]
            y = datos[1]

            # Predicción con Euler
            h = 2  # Número de días para la predicción
            x0 = x[-1]  # Último valor dado en el High
            predice = self.metodo.euler_met(coeficientes, x0, h)

            plt.figure(figsize=(10, 6))
            plt.scatter(x, y, color='blue', label='Datos originales')
            plt.plot(x, y_ajustada, color='red', label='Curva ajustada', linewidth=2)
            plt.scatter([x0 + h], [predice], color='green', label='Predicción (Euler)', s=100)
            plt.title('Predicción con método de Euler')
            plt.xlabel('High')
            plt.ylabel('Low')
            plt.legend()
            plt.grid()
            plt.show()

            print("Coeficientes:", coeficientes)
            print("Error cuadrático medio:", error)
            print(f"Predicción para el siguiente día LOW es: {predice:.4f}")

        except Exception as e:
            print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usar: python main.py <filename>")
    else:
        file = sys.argv[1]
        app = Main(file)
        app.run()