import numpy as np
from openFile import OpenFile

class MetodosNumericos:
    def __init__(self, file):
        self.open_file = OpenFile(file)
        self.open_file.open()
        self.data = self.open_file.data()

    def metodo_minimos_cuadrados(self, datos, min_datos=20, grado=2):
        if len(datos) < min_datos:
            print(f"Se requieren al menos {min_datos} datos para graficar correctamente.")
            return None

        datos_20 = datos[:min_datos]
        x = np.arange(min_datos)

        try:
            ap = np.array([dato[0] for dato in datos_20])  # Apertura
            cie = np.array([dato[1] for dato in datos_20])  # Cierre
            high = np.array([dato[2] for dato in datos_20])  # Máximo
            low = np.array([dato[3] for dato in datos_20])  # Mínimo
        except ValueError as e:
            print(f"Error de conversión: {e}")
            return None

        """
        Metodos de numpy que son utilizados como prueba, el metodo de minimos cuadrados sera realizados por nosotros
        esto es para ver como va funcionando.
        
        
        coef = np.polyfit(x, cie, grado)
        polinomio = np.poly1d(coef)
        ciede_ajuste = polinomio(x)
        
        
        """
        return ciede_ajuste
