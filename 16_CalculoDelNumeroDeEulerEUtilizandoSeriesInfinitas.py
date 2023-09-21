'''
Calcula una aproximación del número de Euler (e) utilizando la fórmula de la serie infinita de Euler.
'''
n = int(input("Ingrese el número de términos para la aproximación de e: "))
e_aproximado = 1
factorial = 1
for i in range(1, n):
    factorial *= i
    e_aproximado += 1 / factorial

print("El valor aproximado de e con", n, "términos es:", e_aproximado)
