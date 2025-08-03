import tkinter as tk
from frontEnd.interfaz import InterfazGrafica
import time

class MainApp:
    def __init__(self):
        root = tk.Tk()
        self.interfaz = InterfazGrafica(root)

    def run(self):
        start_time = time.time()
        self.interfaz.root.mainloop()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tiempo de Ejecución {execution_time:.2f} seconds")

if __name__ == "__main__":
    app = MainApp()
    app.run()