import sys
import pandas as pd

class OpenFile:
    def __init__(self, file):
        self.file = file
        self.dataframe = None

    def open(self):
        """
        Abre un archivo CSV y filtra las columnas 'High', 'Low', 'Open', 'Close'.
        """
        try:
            columnas_filtradas = ['High', 'Low', 'Open', 'Close']
            self.dataframe = pd.read_csv(self.file, usecols=columnas_filtradas)
            # Convertir las columnas a tipo numérico, ignorando errores
            self.dataframe = self.dataframe.apply(pd.to_numeric, errors='coerce')

            # Eliminar filas con valores NaN que se generaron al convertir a numérico
            self.dataframe.dropna(inplace=True)
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def data(self):
        """"
        Creamos una lista que contenga los datos de cada columna del DataFrame.
        """
        if self.dataframe is not None:
            return [self.dataframe[col].tolist() for col in self.dataframe.columns]
        else:
            print("No se han cargado datos.")
            return []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        open_file = OpenFile(file_path)
        open_file.open()
        print(open_file.data())
    else:
        print("Por favor, proporciona la ruta del archivo CSV como argumento.")
