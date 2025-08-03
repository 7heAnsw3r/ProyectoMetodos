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
        self.root.geometry("900x700")

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
        coeficientes, y_ajustada, _, error = metodo.solution()
        if not coeficientes or not y_ajustada:
            tk.messagebox.showerror("Error", "No se pudo calcular la solución. Verifique los datos.")
            return
        if error:
            tk.messagebox.showerror("Error", "No se pudo calcular la solución. Verifique los datos.")
            return
        x = list(range(self.start_time.get(), self.end_time.get() + 1))
        y = datos[0][self.start_time.get() - 1:self.end_time.get()]
        x0 = self.end_time.get() - 1
        y1 = metodo.euler_met(coeficientes, x0, 1)
        if isinstance(y1, tuple):
            y1 = y1[0]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label="Datos Originales")
        plt.plot(x, y_ajustada, label="Curva Ajustada", color="red")
        plt.title("Gráfica de Métodos")
        plt.xlabel("Tiempo")
        plt.ylabel("High")
        plt.legend()
        plt.text(x[-1], y1, f'Predicción: {y1:.2f}', fontsize=10, color='blue', ha='center', va='center')

        self.mostrar_grafica(plt)

    def graficar_velas(self):
        if not self.file_path.get():
            tk.messagebox.showerror("Error", "Por favor, carga un archivo primero.")
            return

        # Lógica para graficar velas
        graficos = Graficos(self.file_path.get(), self.start_time.get(), self.end_time.get())
        graficos.dibujar_velas()

    def mostrar_grafica(self, fig):
        for widget in self.frame_plot.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig.gcf(), master=self.frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        plt.close(fig.gcf())