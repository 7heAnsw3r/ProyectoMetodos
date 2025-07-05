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

    def test(self):
        print(f'Datos: {self.datos}')

impresion = OpenFile(sys.argv[1])
impresion.open()
impresion.test()


