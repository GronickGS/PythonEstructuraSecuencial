'''
Lee los coeficientes de un sistema de dos ecuaciones lineales con dos incógnitas y resuelve para encontrar los valores de las incógnitas.
'''

a = float(input("Coeficiente 'a' de la primera ecuación: "))
b = float(input("Coeficiente 'b' de la primera ecuación: "))
c = float(input("Coeficiente 'c' de la segunda ecuación: "))
d = float(input("Coeficiente 'd' de la segunda ecuación: "))
e = float(input("Resultado de la primera ecuación: "))
f = float(input("Resultado de la segunda ecuación: "))

det = a * d - b * c
if det == 0:
    print("El sistema no tiene una solución única.")
else:
    x = (e * d - b * f) / det
    y = (a * f - c * e) / det
    print("La solución del sistema es: x =", x, "y =", y)
