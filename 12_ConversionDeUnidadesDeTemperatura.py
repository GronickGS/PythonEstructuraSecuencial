'''
Convertir de Celsius a Kelvin
'''
# Solicita al usuario que ingrese una temperatura en grados Celsius
celsius = float(input("Ingrese una temperatura en grados Celsius: "))

# Convierte la temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convierte la temperatura a Kelvin
kelvin = celsius + 273.15

# Muestra los resultados
print("Temperatura en grados Fahrenheit:", fahrenheit)
print("Temperatura en Kelvin:", kelvin)
