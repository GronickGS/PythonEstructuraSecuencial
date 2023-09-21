'''
Encuentra y muestra los pares de números primos gemelos más pequeños hasta un límite dado.
'''

limite = int(input("Ingrese un límite para encontrar pares de números primos gemelos: "))

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

pares_primos_gemelos = []
for numero in range(2, limite):
    if es_primo(numero) and es_primo(numero + 2):
        pares_primos_gemelos.append((numero, numero + 2))

print("Pares de números primos gemelos hasta", limite, "son:", pares_primos_gemelos)
