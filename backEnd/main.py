import sys
import matplotlib.pyplot as plt
from metodosNumericos import MetodosNumericos
from metodoEuler import MetodoEuler

class Main:
    def __init__(self, file):
        self.file = file
        self.metodo = MetodosNumericos(file)
        self.euler = MetodoEuler(file) #AGREGAMOS LA INSTANCIA


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
            #PARTE PARA EULER (PARECE QUE TEDRE QUE AGREGAR UNA NUEVA FUNCION SOLUTION) #ULTIMA MODIFICACION NATTYRD
            h = 1 #Este es el numero de dias para la prediccion
            x0 = x[-1] #Ultimo valor dado en el High
            predice = self.euler.euler_met(coeficientes, x0, h) #IMPORTANTE: Aun no verifico que este cogiendo bien los datos
            print(f"Prediccion para el siguiente dia LOW es: {predice:.4f}") #Salida del resultado
            #TERMINA AQUI LA MODIFICACION
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
    else:
        file = sys.argv[1]
        app = Main(file)
        app.run()