import sys
import csv

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
            print(f"Error al abrir el archivo: {e}")

    def data(self):
        columnas = ['High', 'Low', 'Open', 'Close']
        listas_separadas = [[] for _ in columnas]
        for key, value in self.datos.items():
            for i, col in enumerate(columnas):
                try:
                    if col in value:
                        listas_separadas[i].append(float(value[col]))
                except ValueError:
                    print(f"No se pudo transformar '{value[col]}' a número de la columna '{col}'. Por lo que se va a omitir.")

        return listas_separadas

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        open_file = OpenFile(file_path)
        open_file.open()
        open_file.data()
    else:
        print("Por favor, proporciona la ruta del archivo CSV como argumento.")
