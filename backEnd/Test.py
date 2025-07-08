import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

class OpenFile:
    def __init__(self, file):
        self.file = file
        self.datos = {}

    def open(self):
        try:
            with open(self.file, newline='') as file_csv:
                read = csv.DictReader(file_csv)
                columnas_filtradas = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']
                for i,row in enumerate(read):
                    self.datos[i]={col: row[col] for col in columnas_filtradas if col in row}
        except Exception as e:
            print(f"Error al intentar abrir  el archivo: {e}")

    def data(self):
        lista =[]
        for key, value in self.datos.items():
            for col, val in value.items():
                try:
                    lista.append(float(val))
                except ValueError:
                    print(f" No se pudo tranformar '{val}' a número de la columna '{col}'. Por lo que se va a omitir.")
                    print(lista)
#Aqui esta el metodo a medias todavia, aun estoy probandolo para poder ajustarlo al modelo. Tiene aun a tener ciertas fallas
#Tambien aun no hemos definido un criterio de aceptacion hablando respecto al error que vamos a permitir.
#Obviamente dicho error NO va aqui, ya que el modelo predice, no busca aproximar a un valor ya conocido.
    def MetodoMinimosCuadrados(self):
        min = 20
        if len(self.datos) < min: #Verificamos si hay al menos 20 datos, pero podemos ajustarlo para menos datos
            print(f"Se requieren el minimo de '{min}' datos para graficar correctamente")
            return


        datos_20 = list(self.datos.items())[:20] #Solo voy a tomar 20 datos pa entender como funcionara
        x = np.arange(20)
      #Organizamos los datos para poder trabajar con ellos de manera correcta.
        try:
            ap = np.array([float(dato['Open']) for _, dato in datos_20]) #apertura
            cie = np.array([float(dato['Close']) for _, dato in datos_20]) #cierre
            high = np.array([float(dato['High']) for _, dato in datos_20])
            low = np.array([float(dato['Low']) for _, dato in datos_20])
        except ValueError as e:
            print(f"Error de conversion : {e}")
            return

        coef = np.polyfit(x, cie, 2) #Aplico la libreria usando los 20 datos tomados  y el precio de cierre.
        polinomio = np.poly1d(coef) #Aqui le mando para el coef para poder obtener el polinomio
        ciedeAjuste= polinomio(x)

        #Aqui practicamente es solo para graficar el polinomio, use matplotlib.
        plt.figure(figsize=(12, 6))
        plt.plot(x, ciedeAjuste, color='black', label='Modelo para el ajuste cuadrático (con cie)')
        plt.scatter(x, ap, color='blue', label='Open')
        plt.scatter(x, cie, color='green', label='Close')
        plt.scatter(x, high, color='red', label='High', marker='^')
        plt.scatter(x, low, color='orange', label='Low', marker='v')
        plt.title("Modelo Cuadrático del Precio de Cierre")
        plt.xlabel("Índice por dia")
        plt.ylabel("Precio De la moneda")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = "coin.csv"
        open_file = OpenFile(file_path)
        open_file.open()
        open_file.data()
    else:
        print("Por favor, dame la ruta del archivo CSV como argumento.")

