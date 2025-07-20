import tkinter as tk
from frontEnd.interfaz import InterfazGrafica

class MainApp:
    def __init__(self):
        root = tk.Tk()

        self.interfaz = InterfazGrafica(root)

    def run(self):
        self.interfaz.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()