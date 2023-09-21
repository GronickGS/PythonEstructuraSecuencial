'''
Solicita al usuario que ingrese el monto principal, la tasa de interés anual
y el número de veces que se capitaliza el interés por año. Calcula y muestra
el monto total después de un período de inversión en años.
'''

principal = float(input("Ingrese el monto principal: "))
tasa_anual = float(input("Ingrese la tasa de interés anual (como decimal): "))
capitalizaciones_anuales = int(input("Ingrese el número de capitalizaciones anuales: "))
años = int(input("Ingrese el número de años de inversión: "))

interes_compuesto = principal * ((1 + tasa_anual / capitalizaciones_anuales) ** (capitalizaciones_anuales * años)) - principal
print("El monto total después de", años, "años es:", principal + interes_compuesto)
