'''
Solicita al usuario que ingrese los dos primeros términos y la longitud deseada de la secuencia de Fibonacci. Luego, genera la secuencia completa.
'''
term1 = int(input("Ingrese el primer término: "))
term2 = int(input("Ingrese el segundo término: "))
longitud = int(input("Ingrese la longitud de la secuencia de Fibonacci: "))

fibonacci = [term1, term2]
while len(fibonacci) < longitud:
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

print("La secuencia de Fibonacci es:", fibonacci)
