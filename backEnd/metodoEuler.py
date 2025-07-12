from openFile import OpenFile
import math
class MetodoEuler:
    def __init__(self, file):
        self.open_file = OpenFile(file)
        self.open_file.open()
        self.data = self.open_file.data()

def derivar(self, coef): #Obtenemos la derivada con los coef de nuestro polinomio.
    derivada =[j * coef[j] for j in range(1,len(coef))]
    return derivada

def evaluarP(self, coe, x): # Le vamos a evaluar el polinomio segun un punto X especifico.
    return sum(coe[j]*(x ** j) for j in range(len(coe)))

def eulermetodo(self, coe, x0, h): #Aplicamos el metodo euler al polinomio obtenido.
    derivada = self.derivar(coe) #Obtenemos la derivada

    y0= self.evaluarP(coe, x0) #Obtenemos el polinomio evaluado en x0

    dydx = self.evaluarP(derivada, x0) # Evaluamos respecto al valor de la derivada
    y1= y0 +  h * dydx # Aplicamos el metodo de Euler

    return y1

# Esta es la logica basica que aplicamos  directamente a euler