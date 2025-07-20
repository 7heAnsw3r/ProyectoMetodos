import tkinter as tk
from tkinter import filedialog, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from backEnd import MetodosNumericos
from frontEnd.graficos import Graficos

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz Gráfica - Proyecto")
        self.root.geometry("900x600")

        # Variables
        self.file_path = tk.StringVar()
        self.start_time = tk.IntVar(value=1)
        self.end_time = tk.IntVar(value=2160)

        # Selector de archivo
        frame_file = tk.Frame(root)
        frame_file.pack(pady=10)
        tk.Label(frame_file, text="Archivo CSV:").pack(side=tk.LEFT, padx=5)
        tk.Entry(frame_file, textvariable=self.file_path, width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_file, text="Cargar", command=self.cargar_archivo).pack(side=tk.LEFT, padx=5)

        # Intervalo de tiempo
        frame_interval = tk.Frame(root)
        frame_interval.pack(pady=10)
        tk.Label(frame_interval, text="Intervalo de tiempo:").pack(side=tk.LEFT, padx=5)
        tk.Entry(frame_interval, textvariable=self.start_time, width=10).pack(side=tk.LEFT, padx=5)
        tk.Label(frame_interval, text="a").pack(side=tk.LEFT)
        tk.Entry(frame_interval, textvariable=self.end_time, width=10).pack(side=tk.LEFT, padx=5)

        # Botones de acción
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="Generar Gráfica de Métodos", command=self.graficar_metodos).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="Generar Gráfico de Velas", command=self.graficar_velas).pack(side=tk.LEFT, padx=10)

        # Área de gráficos
        self.frame_plot = tk.Frame(root)
        self.frame_plot.pack(fill=tk.BOTH, expand=True)

    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            self.file_path.set(file_path)
            tk.messagebox.showinfo("Archivo Cargado", f"Archivo cargado: {file_path}")

    def graficar_metodos(self):
        if not self.file_path.get():
            tk.messagebox.showerror("Error", "Por favor, carga un archivo primero.")
            return

        # Lógica para graficar con métodos
        metodo = MetodosNumericos(self.file_path.get(),self.start_time.get(),self.end_time.get())
        datos = metodo.open_file.data()
        coeficientes, y_ajustada, _ = metodo.solution()
        x = list(range(self.start_time.get(), self.end_time.get() + 1))
        y = datos[0][self.start_time.get() - 1:self.end_time.get()]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label="Datos Originales")
        plt.plot(x, y_ajustada, label="Curva Ajustada", color="red")
        plt.title("Gráfica de Métodos")
        plt.xlabel("Tiempo")
        plt.ylabel("Valores")
        plt.legend()

        self.mostrar_grafica(plt)

    def graficar_velas(self):
        if not self.file_path.get():
            tk.messagebox.showerror("Error", "Por favor, carga un archivo primero.")
            return

        # Lógica para graficar velas
        graficos = Graficos(self.file_path.get(), self.start_time.get(), self.end_time.get())
        graficos.dibujar_velas()

    def mostrar_grafica(self, plt_figure):
        for widget in self.frame_plot.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(plt_figure.gcf(), master=self.frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        plt.close(plt_figure)  # Cerrar la figura para liberar memoria
