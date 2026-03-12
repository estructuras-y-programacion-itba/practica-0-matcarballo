import random

def tirar_dados(cantidad_dados):
    resultados = []
    for i in range(cantidad_dados):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

def contar_dados(dados):
    conteo = {}
    for dado in dados:
        if dado in conteo:
            conteo[dado] += 1
        else:
            conteo[dado] = 1
    return conteo

def es_generala(dados):
    conteo = contar_dados(dados)
    for valor in conteo.values():
        if valor == 5:
            return True
    return False

def es_poker(dados):
    conteo = contar_dados(dados)
    for valor in conteo.values():
        if valor == 4:
            return True
    return False

def es_full(dados):
    conteo = contar_dados(dados)
    valores = sorted(conteo.values())
    return valores == [2,3]

def es_escalera(dados):
    valores = sorted(dados)
    return (valores == [1,2,3,4,5] or valores == [2,3,4,5,6])

planilla_j1 = {
    "E": None,
    "F": None,
    "P": None,
    "G": None,
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None
}

planilla_j2 = {
    "E": None,
    "F": None,
    "P": None,
    "G": None,
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None
}

def calcular_puntaje(dados, cat):
    if cat == "G" or cat == "g":
        if es_generala(dados):
            return 50
        else:
            return 0
    elif cat == "P" or cat == "p":
        if es_poker(dados):
            return 40
        else:
            return 0
    elif cat == "F" or cat == "f":
        if es_full(dados):
            return 30
        else:
            return 0
    elif cat == "E" or cat == "e":
        if es_escalera(dados):
            return 20
        else:
            return 0
    else:
        num = int(cat)
        suma = 0
        for dado in dados:
            if dado == num:
                suma += dado
        return suma

def turno(planilla):
    dados = tirar_dados(5)
    print(f"Dados: {dados[0]}, {dados[1]}, {dados[2]}, {dados[3]}, {dados[4]}")
    cant_relanz = 0
    relanz1 = input("Quiere relanzar? (S/N): ")
    if relanz1 == "S" or relanz1 == "s":
        cant_relanz += 1
        