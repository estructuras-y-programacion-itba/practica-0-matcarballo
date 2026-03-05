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
    