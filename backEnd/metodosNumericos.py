from .openFile import OpenFile

class MetodosNumericos:
    def __init__(self, file,t0,tf):
        self.open_file = OpenFile(file)
        self.open_file.open()
        self.data = self.open_file.data()
        self.tiempo_inicial = t0
        self.tiempo_final = tf

    def solution(self):
        """
        Metodo principal sirve para llamar a los metodos que se necesiten para resolver el problema
        :return: Hace una llamada al metodo de mínimos cuadrados para resolver el problema de regresión lineal.
        """
        x = list(range(self.tiempo_inicial, self.tiempo_final+1)) # Indice evaluado en el tiempo como numero
        y = self.data[0][self.tiempo_inicial-1:self.tiempo_final] # Asumiendo que wla segunda columna es y es decir High
        return self.minimos_cuadrados(x, y, 5)

#METODO AGREGADO PARA USAR EULER YA ESTA BIEN AÑADIDA
    def solution_euler(self, x0):
        """
        Metodo para llamar el metodo de prediccion euler. Debemos considerar que vamos a trabajar con un X0 = tf
        que es valor inicial igual al valor final High o Low dado por el intervalo escogido dentro de la parte grafica
        del metodo de minimos cuadrados. (Trabajamos con prediccion en el mismo intervalo).
        X0: Dato del tiempo(Dias), EJMP: rango de [1,2200] el X0 sera 2200 y h en 1 tal que predice Y1 para X1=2201
        :return:
        """
        coeficientes, y_ajustada, error = self.solution()
        h= 1
        y1 = self.euler_met(coeficientes, x0, h)

        return   y1


    def resolver_ecuaciones(self, A, b):
        """
        Resolver un sistema de ecuaciones lineales Ax = b utilizando eliminación Gaussiana.
        :param A: Matriz de coeficientes.
        :param b: Vector de términos independientes.
        :return: Vector solución x.
        """
        n = len(b)
        for i in range(n):
            if A[i][i] == 0:
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        # Intercambiar filas si el pivote es cero
                        A[i], A[j] = A[j], A[i]
                        b[i], b[j] = b[j], b[i]
                        break
                    else:
                        print(
                            f"La variable x no participa directamente en la ecuacion, por lo tanto no se puede resolver el sistema de ecuaciones.")
            for j in range(i + 1, n):
                if A[j][i] != 0:  # Si elemento abajo del pivote es cero no lo tomamos en cuenta
                    factor = A[j][i] / A[i][i]
                    for k in range(i, n):
                        # Se multiplica por toda la fila, por eso el único elemento que cambia es k.
                        A[j][k] -= factor * A[i][k]
                    b[j] -= factor * b[i]

        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
        return x

    def minimos_cuadrados(self, x, y, grado):
        """
        Metodo para calcular la regresión lineal por el metodo de mínimos cuadrados se calcula el comportamiento de low
        dado high.

        :param x: Los valores independientes (High).
        :param y: Los valores dependientes (Low).
        :param grado: Grado con el que se espera trabajar.
        :return: Coeficientes, y_ajustada ajustada y error cuadrático medio.
        """
        n = len(x)
        A = [[x_i**j for j in range(grado + 1)] for x_i in x] # Matriz de diseño A: [1, x, x^2, ..., x^grado]


        AtA = [[sum(A[i][k] * A[i][j] for i in range(n)) for j in range(grado + 1)] for k in range(grado + 1)] # Calcular A^T * A
        AtY = [sum(A[i][j] * y[i] for i in range(n)) for j in range(grado + 1)] # Calcular A^T * y

        coeficientes = self.resolver_ecuaciones(AtA, AtY)

        # Calcular la y_ajustada ajustada
        y_ajustada = [sum(coeficientes[j] * (x_i ** j) for j in range(grado + 1)) for x_i in x]

        # Calcular el error cuadrático medio
        error = sum((y[i] - y_ajustada[i])**2 for i in range(n)) / n

        return coeficientes, y_ajustada, error


    def derivar(self, coef):
        """
        Metodo para calcular la derivada de un polinomio dado sus coeficientes.
        :param coef: Lista de coeficientes del polinomio.
        :return: Lista de coeficientes de la derivada del polinomio.
        """
        derivada =[j * coef[j] for j in range(1,len(coef))]
        return derivada

    def evaluarP(self, coe, x):
        """
        Evaluamos el polinomio en un punto x dado sus coeficientes.
        :param coe: Lista de coeficientes del polinomio
        :param x: x inicial
        :return: Polinomio evaluado en x
        """
        return sum(coe[j]*(x ** j) for j in range(len(coe)))


    def euler_met(self, coe, x0, h):
        """
        Metodo de Euler para aproximar la solución de una ecuación diferencial ordinaria.
        :param coe: Lista de coeficientes del polinomio.
        :param x0: Valor inicial ultimo valor dado por high.
        :param h: Numero de dias de la prediccion
        :return: Valor aproximado
        """
        derivada = self.derivar(coe)  # Obtenemos la derivada

        y0 = self.evaluarP(coe, x0)  # Obtenemos el polinomio evaluado en x0

        dydx = self.evaluarP(derivada, x0)  # Evaluamos respecto al valor de la derivada
        y1 = y0 + h * dydx  # Aplicamos el metodo de Euler

        return y1

    def calcular_variacion(self, open_values, close_values):
        """
        Calcula la variación diaria entre los valores de apertura y cierre.
        :param open_values: Lista de valores de apertura (Open).
        :param close_values: Lista de valores de cierre (Close).
        :return: Lista de variaciones diarias.
        """
        if len(open_values) != len(close_values):
            raise ValueError("Las listas de valores de apertura y cierre deben tener la misma longitud.")

        return [close - open for open, close in zip(open_values, close_values)]