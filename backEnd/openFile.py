import pandas as pd

class OpenFile:
    def __init__(self, file):
        self.file = file
        self.dataframe = None

    def open(self):
        """
        Abre un archivo CSV y filtra las columnas 'High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap'.
        """
        try:
            columnas_filtradas = ['High', 'Low', 'Open', 'Close','Volume', 'Marketcap']
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
        :return: Lista de listas, donde cada sublista contiene los datos de una columna.
        """
        if self.dataframe is not None:
            return [self.dataframe[col].tolist() for col in self.dataframe.columns]
        else:
            print("No se han cargado datos.")
            return []