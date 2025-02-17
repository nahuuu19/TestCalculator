
"""Reglas básicas: No importe ningún otro paquete además de los que ya han sido importados.
Siga las interfaces que se han preparado para usted, no las modifiquen.
Realice la inicialización de clase en la configuración.
El puntaje de pase de tarea es de 100.
Nota importante: el mensaje de error de éxito inesperado significa que probablemente esté modificados
archivos de plantilla modificados que se supone que no debía modificar.
Consulte con la descripción de la tarea una vez más."""

#1-Open the file tasks/calculator.py
#2-Create and add in file calculator.py test case for the function test_sum:
#3-Create and add in the file calculator.py the test case for the function test_multiply
#4-Create and add in the file calculator.py the test case for the function test_subtract
#5-Create and add in the file calculator.py the test case for the function test_divide:
#6-Create and add in the file calculator.py the test case for the function test_sqrt
#7-Create and add in the file calculator.py the test case for the function test_pi:
#8-Add and change docstrings whereever needed.

import math

class Calculator:
    """ Clase que implementa una calculadora con operaciones básicas.

    Métodos:
        sum(a, b): Retorna la suma de a y b.
        multiply(a, b): Retorna el producto de a y b.
        subtract(a, b): Retorna la diferencia entre a y b.
        divide(a, b): Retorna el cociente entero de a y b.
        sqrt(a): Retorna la raíz cuadrada de un valor.
        calculate_pi(): Retorna el valor de la constante matemática pi."""
    #inicializacion
    def __init__(self):
        pass
    #Point 1
    def sum(self, a, b):
        """En esta función, pasamos como parámetro dos valores, y retornamos la suma de estos valores"""
        return a + b
    #Point 2
    def multiply(self, a, b):
        """En esta función, pasamos como parámetro dos valores, y retornamos la multiplicación de estos valores"""
        return a * b
    #Point 3
    def subtract(self, a, b):
        """En esta función, pasamos como parámetro dos valores, y retornamos la resta de estos valores"""
        return a - b
    #Point 4
    def divide(self, a, b):
        """En esta función, pasamos como parámetro dos valores, y retornamos la división de estos valores.
        Y validamos que si el segundo parametro es igual a 0. Se produzca una exception con el mensaje detallando el error"""
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por 0")
        return a // b
    #Point 5
    def sqrt(self, a):
        """En esta función, pasamos como parámetro un valor, y retornamos la raiz cuadrada de este mismo.
        Usamos el metodo float para que retorne el valor numerico con decimales incluidos"""
        return float(math.sqrt(a))
    #Point 6
    def calculate_pi(self):
        """Esta función utiliza  math, donde se obtiene el valor de pi"""
        return math.pi

