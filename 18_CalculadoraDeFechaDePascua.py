'''
Solicita al usuario que ingrese un año y calcula la fecha de Pascua para ese año utilizando el algoritmo de Gauss.

'''
año = int(input("Ingrese un año para calcular la fecha de Pascua: "))

a = año % 19
b = año // 100
c = año % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
mes = (h + l - 7 * m + 114) // 31
dia = ((h + l - 7 * m + 114) % 31) + 1

print("La fecha de Pascua en el año", año, "es el", dia, "de", "marzo" if mes == 3 else "abril")
