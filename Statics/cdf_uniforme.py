import matplotlib.pyplot as plt
from datetime import datetime

def gerarar_var (num):
    a = 9
    b =7
    m = 2^34
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

def uniforme_cdf (maior, menor):
    pdf = uniforme_pdf(maior, menor)
    cdf = list()
    i = 0
    for valor in pdf:
        valor = (valor-maior)/(menor-maior)
        cdf.append(valor)
        i += 1 
    pdf.append(1)
    cdf.append(0)
    pdf.append(4)
    cdf.append(0)
    pdf.append(12)
    cdf.append(1)
    pdf.append(1)
    cdf.append(0)
    pdf.append(15)
    cdf.append(1)
    pdf.append(15)
    cdf.append(1)
    cdf = sorted(cdf)
    pdf = sorted(pdf)
    plt.plot(pdf,cdf)
    plt.show()


lista = uniforme_pdf(12,4)

plt.hist(lista,32, rwidth=0.9)
plt.show()
