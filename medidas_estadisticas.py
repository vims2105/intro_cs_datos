import numpy as np

def media_aritmetica(data):
    return (sum(data) / len(data))
    pass

def mediana(data):
    data = sorted(data)
    if len(data)%2 == 0:
        return (data[int(len(data) / 2)] + data[int((len(data) / 2) + 1)]) / 2
    else:
        return data[int(len(data) / 2)]
    pass

def moda(data):
    cuentas = []
    for c in categorias:
        n = 0
        for x in data:
            if x == c:
                n = n + 1
        cuentas.append(n)
    pass