'''
Genera una contraseña segura con una longitud específica, que incluye letras mayúsculas, minúsculas, dígitos y caracteres especiales.
'''

import random
import string

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

print("Contraseña generada:", contraseña)
