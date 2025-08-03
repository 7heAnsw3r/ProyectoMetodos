# 📈 Proyecto de Métodos Numéricos

## 🧠 Descripción

Este proyecto tiene como objetivo aplicar métodos numéricos clásicos para analizar y estimar el comportamiento de precios en criptomonedas, utilizando datos históricos.

Se enfoca en demostrar cómo herramientas matemáticas como la **regresión por mínimos cuadrados** y la **resolución de sistemas de ecuaciones lineales** pueden ser utilizadas para modelar y predecir tendencias de precios en un entorno práctico y actual.

> ⚠️ **Nota:** Este proyecto es de carácter educativo. No debe considerarse una herramienta de análisis financiero ni de inversión.

---

## ⚙️ Paquetes Utilizados

- `pandas` – Manipulación y análisis de datos.
- `matplotlib` – Visualización gráfica de los resultados.
- `numpy` – (opcional, si se usa) Cálculo numérico eficiente.
- `mplfinance` – Visualización de gráficos financieros (opcional).
- `tkinter` – Interfaz gráfica para la selección de archivos.

---

## 📁 Estructura del Proyecto

```bash
.
├── main.py                # Script principal del proyecto
├── backEnd/                
│   └── __init__.py         
│   └── metodosNumericos.py       
│   └── openFile.py      
├── frontEnd/                  
│   └── __init__.py          
│   └── graficos.py         
│   └── interfaz          
├── Archivos/                 
│   └── Informes.pdfs         
├── coin_Ethereum.csv      # Datos históricos de Ethereum
└── README.md              # Este archivo
```

## 📊 Ejemplo de Uso

Ya sea desde la terminal de linux o Windows puedes ejecutar el script principal:

```bash
python main.py
```
Esto abrirá una ventana para seleccionar el archivo CSV con los datos históricos de precios de criptomonedas. 
Una vez seleccionado, se generarán gráficos y análisis basados en los métodos numéricos implementados.