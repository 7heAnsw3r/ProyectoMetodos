from openFile import OpenFile

class MetodosNumericos:
    def __init__(self, file):
        self.open_file = OpenFile(file)
        self.open_file.open()
        self.data = self.open_file.data()

    def solution(self):
        """
        Metodo principal sirve para llamar a los metodos que se necesiten para resolver el problema
        :return: Hace una llamada al metodo de mínimos cuadrados para resolver el problema de regresión lineal.
        """
        x = self.data[0] # Asumiendo que la primera columna es x es decir High
        y = self.data[1] # Asumiendo que la segunda columna es y es decir Low
        return self.minimos_cuadrados(x, y, 4)

    def resolver_ecuaciones(self, A, b):
        """
        Resolver un sistema de ecuaciones lineales Ax = b utilizando eliminacion Gaussiana
        :param A: Matriz de coeficientes.
        :param b: Vector de términos independientes.
        :return: Vector solución x.
        """
        n = len(b)
        for i in range(n):
            for j in range(i+1,n):
                if A[j][i] != 0: # Elemento que se encuentra debajo del pivote
                    factor = A[j][i] / A[i][i] # Factor por el cual se multiplicara la fila i
                    for k in range(i, n):
                        """
                        Se multiplica por toda la fila por eso el unico elemento que cambia es k.
                        """
                        A[j][k] -= factor * A[i][k]
                    b[j] -= factor * b[i]

        x = [0] * n # Vector de soluciones la variable se puede llamar x, soluciones o lo que sea.
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
        return x


    def minimos_cuadrados(self, x, y, grado):
        """
        Método para calcular la regresión lineal por el método de mínimos cuadrados se calcula el comportamiento de low
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