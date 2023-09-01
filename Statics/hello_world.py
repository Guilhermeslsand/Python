import matplotlib.pyplot as plt
from datetime import datetime

def gerarar_var (num):
    a = 9
    b =23
    m = 2^46
    var = list()
    cont = 1
    x = 0
    data_hora = datetime.now()
    seed = data_hora.second
    var.append(seed)
    while cont<num+1:
        x = (a*var[-1]+b) % m
        var.append(x) 
        cont += 1
    i = 0
    for valor in var:
        valor = valor/(m+1)
        var[i] = valor
        i += 1
    var.pop(0)
    return var

def uniforme_pdf (maior, menor):
    pdf = gerarar_var(10000)
    i = 0
    for valor in pdf:
        valor = menor + (maior-menor) * valor
        pdf[i] = valor
        i += 1
    return pdf

lista = uniforme_pdf(4,12)

plt.hist(lista, 9,  rwidth=0.8)
plt.show()