from backEnd import MetodosNumericos
import pandas as pd
import mplfinance as mpf
import sys

class Graficos:
    def __init__(self, file):
        self.metodo = MetodosNumericos(file)
        self.df = self.metodo.open_file.dataframe

    def dibujar_velas(self):

        self.df.index = pd.date_range(
            start='2015-08-08',
            periods=len(self.df),
            freq='D'
        )

        mpf.plot(
            self.df[['Open', 'High', 'Low', 'Close']],
            type='candle',
            style='charles',
            title='Velas OHLC',
            ylabel='Precio'
        )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usar: python frontEnd.graficos <filename>")
    else:
        file = sys.argv[1]
        graficos = Graficos(file)
        graficos.dibujar_velas()