'''
Pide al usuario que ingrese un número y calcula su raíz cuadrada utilizando el método de aproximación de Newton.
'''

numero = float(input("Ingrese un número: "))
raiz_aproximada = numero / 2
for _ in range(10):
    raiz_aproximada = 0.5 * (raiz_aproximada + numero / raiz_aproximada)
print("La raíz cuadrada aproximada de", numero, "es:", raiz_aproximada)
