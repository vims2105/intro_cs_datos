###########################
#C O N T E N I D O S

#media aritmética: función "promedio"
#mediana: función "mediana"
#moda: función "moda"
#varianza: función "varianza"
#covarianza: función "cov"
#desviación estándar: función "desv_estd"
#rango: función "rango"
#desviación mediana absoluta: función "DMA"
#percentiles: función "percentil"
#rango intercuartílico: función "IQR"
#regla de freeman-diaconis: función "freeman_diaconis"
#coeficiente de correlación: función "r"
#bonus: mugi pastel

# # # # # # # # # # # # # # # # # # # # #
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠄⣀⡇⢸⣿⣿⣿⣿
#⠀⠄⠠⠀⠀⠀⢠⢰⠝⠀⠀⣰⠀⠀⠀⠀⡀⠀⠀⠀⡀⠀⠀⠈⢣⣸⣿⣿⣿⣿
#⠀⠄⠰⠄⠀⢰⡣⠋⠀⠀⡴⡉⠀⠀⠀⠀⠂⠀⢰⠀⠇⠀⠀⠀⠀⠹⣿⣿⣿⣿
#⣠⣄⣠⣄⣤⢢⠃⠀⠀⡸⡱⣽⠀⡄⠀⠀⢀⣧⠀⠇⡇⠀⠀⠆⡆⠀⢹⣿⣿⣿
#⣿⣿⣿⣿⡇⠌⠀⠀⢀⡿⢉⣨⠀⡁⠀⠀⢸⣌⠆⠰⡀⠀⠀⠀⡇⠀⢸⣿⣿⣿
#⣿⣿⣿⣿⡇⠀⠀⠀⡜⠁⠃⠚⢣⡷⠀⠀⢸⠂⠗⢆⣇⠀⠀⠀⠂⠀⢸⣿⣿⣿
#⣿⣿⣿⣿⡇⠀⠀⠀⠁⠀⠀⠀⠀⢁⢡⡀⠈⠀⠀⠈⠻⠀⠀⠀⠀⠰⢸⣿⣿⣿
#⣿⣿⣿⣿⣷⠘⡄⠘⠀⣀⣀⡀⠀⠀⠀⠳⢄⠀⠀⠀⠀⡄⢀⠆⠀⡌⣾⣿⣿⣿
#⣿⣿⣿⣿⣿⣶⡳⣀⠀⠉⠉⠙⠀⠀⠀⠀⠀⠛⠛⠛⠀⢁⡾⠀⢘⣧⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⢡⠸⠀⠀⣴⠄⠀⠀⠀⠀⠀⠀⢄⡀⠀⠜⠁⢧⡏⠘⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⡇⠈⡄⠇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠙⠁⢀⡟⠀⡤⠀⠀⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⡇⠀⢣⢸⣦⡀⠀⠀⠀⠠⡑⠀⠀⢀⣠⢾⠀⠀⡀⡀⠀⢹⣿⣿⣿
#⣿⣿⣿⣿⣿⠇⠀⠈⢘⢣⣭⣗⢤⠜⠀⠐⡠⢐⠟⣬⡄⠀⠀⣇⠡⠀⠘⣿⣿⣿
#⣿⣿⣿⣿⣃⡀⠀⠀⣿⣾⣯⣦⢳⠆⡠⢸⢊⠁⢠⣿⡁⠀⠀⣼⣦⣁⣱⢻⣿⣿
#⣿⣿⣿⣿⣿⠃⡠⠐⣩⣭⡿⠛⢱⠀⠀⠀⢃⣆⣿⣿⠰⠀⠀⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⠌⠀⠀⠄⠀⣸⣦⠴⠀⠀⠀⠀⣹⣿⡏⡈⢀⣾⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⡏⠀⠀⠀⢈⣩⣽⡿⠀⠀⢀⣠⣤⣿⣿⢱⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿
# # # # # # # # # # # # # # # # # # # # #

def promedio(data):
    """
    """
    return (sum(data) / len(data))

def mediana(data):
    """
    """
    data = sorted(data)
    n = len(data)

    if n % 2 == 0:
        return (data[int(n / 2 - 1)] + data[int(n / 2)]) / 2
    else:
        return data[int(n / 2)]

def moda(data):
    """
    """
    cuentas = {}
    
    for x in data:
        if x in cuentas:
            cuentas[x] += 1
        else:
            cuentas[x] = 1
    
    max_frecuencia = max(cuentas.values())
    
    modas = [elemento for elemento, frecuencia in cuentas.items() if frecuencia == max_frecuencia]
    
    return modas

def varianza(data):
    """
    """
    n = len(data)

    prom = promedio(data)

    return sum((data[i] - prom) ** 2 for i in range(n)) / n

def cov(x,y):
    """
    """
    n = len(y)
    promx = promedio(x)
    promy = promedio(y)
    
    return (1 / n) * sum((x[i] - promx) * (y[i] - promy) for i in range(n))

def desv_estd(data):
    """
    """
    return varianza(data) ** 0.5

def rango(data):
    """
    """
    data = sorted(data)

    return data[-1] - data[0]

def DMA(data):
    """
    """
    med = mediana(data)

    desvs = []
    for x in data:
        desvs.append(abs(x - med))

    return mediana(desvs)

def percentil(data, percentil):
    """
    """
    data=sorted(data)

    k = (len(data) - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < len(data):
        return data[f] + c * (data[f + 1] - data[f])
    else:
        return data[f]
    
def IQR(data):
    """
    """
    q1 = percentil(data, 25)
    q3 = percentil(data, 75)

    return q3 - q1

def freeman_diaconis(data):
    """
    """
    n = len(data)
    iqr = IQR(data)

    return 2 * iqr * (n ** (-1/3))

def r(x, y):
    """
    """
    return (cov(x,y) / (desv_estd(x) * desv_estd(y)))

def mugi_pastel():
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠄⣀⡇⢸⣿⣿⣿⣿
⠀⠄⠠⠀⠀⠀⢠⢰⠝⠀⠀⣰⠀⠀⠀⠀⡀⠀⠀⠀⡀⠀⠀⠈⢣⣸⣿⣿⣿⣿
⠀⠄⠰⠄⠀⢰⡣⠋⠀⠀⡴⡉⠀⠀⠀⠀⠂⠀⢰⠀⠇⠀⠀⠀⠀⠹⣿⣿⣿⣿
⣠⣄⣠⣄⣤⢢⠃⠀⠀⡸⡱⣽⠀⡄⠀⠀⢀⣧⠀⠇⡇⠀⠀⠆⡆⠀⢹⣿⣿⣿
⣿⣿⣿⣿⡇⠌⠀⠀⢀⡿⢉⣨⠀⡁⠀⠀⢸⣌⠆⠰⡀⠀⠀⠀⡇⠀⢸⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⡜⠁⠃⠚⢣⡷⠀⠀⢸⠂⠗⢆⣇⠀⠀⠀⠂⠀⢸⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠁⠀⠀⠀⠀⢁⢡⡀⠈⠀⠀⠈⠻⠀⠀⠀⠀⠰⢸⣿⣿⣿
⣿⣿⣿⣿⣷⠘⡄⠘⠀⣀⣀⡀⠀⠀⠀⠳⢄⠀⠀⠀⠀⡄⢀⠆⠀⡌⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣶⡳⣀⠀⠉⠉⠙⠀⠀⠀⠀⠀⠛⠛⠛⠀⢁⡾⠀⢘⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢡⠸⠀⠀⣴⠄⠀⠀⠀⠀⠀⠀⢄⡀⠀⠜⠁⢧⡏⠘⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠈⡄⠇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠙⠁⢀⡟⠀⡤⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠀⢣⢸⣦⡀⠀⠀⠀⠠⡑⠀⠀⢀⣠⢾⠀⠀⡀⡀⠀⢹⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⠈⢘⢣⣭⣗⢤⠜⠀⠐⡠⢐⠟⣬⡄⠀⠀⣇⠡⠀⠘⣿⣿⣿
⣿⣿⣿⣿⣃⡀⠀⠀⣿⣾⣯⣦⢳⠆⡠⢸⢊⠁⢠⣿⡁⠀⠀⣼⣦⣁⣱⢻⣿⣿
⣿⣿⣿⣿⣿⠃⡠⠐⣩⣭⡿⠛⢱⠀⠀⠀⢃⣆⣿⣿⠰⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠌⠀⠀⠄⠀⣸⣦⠴⠀⠀⠀⠀⣹⣿⡏⡈⢀⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠀⠀⠀⢈⣩⣽⡿⠀⠀⢀⣠⣤⣿⣿⢱⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿
''')