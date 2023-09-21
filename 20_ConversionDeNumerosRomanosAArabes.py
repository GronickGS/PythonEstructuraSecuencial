'''
Lee un número romano y lo convierte a su equivalente en números arábigos.
'''
def romano_a_arabe(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabe = 0
    prev_valor = 0
    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < prev_valor:
            arabe -= valor
        else:
            arabe += valor
        prev_valor = valor
    return arabe

numero_romano = input("Ingrese un número romano: ")
numero_arabe = romano_a_arabe(numero_romano)
print("El equivalente en números arábigos es:", numero_arabe)
