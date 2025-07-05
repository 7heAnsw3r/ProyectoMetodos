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
        lista =[]
        for key, value in self.datos.items():
            for col, val in value.items():
                lista.append(float(val))
        print(lista)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        open_file = OpenFile(file_path)
        open_file.open()
        open_file.data()
    else:
        print("Por favor, proporciona la ruta del archivo CSV como argumento.")
