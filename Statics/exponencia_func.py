import matplotlib.pyplot as plt
from datetime import datetime
import math
import numpy

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

def exponencial_pdf (l):
    pdf = gerarar_var(10000)
    i = 0
    for valor in pdf:
        valor =  -l * numpy.log(1-valor)
        pdf[i] = valor
        i += 1
    return pdf
    
def exponencial_cdf (l):
    var = gerarar_var(10000)
    cdf = list()
    i = 0
    for valor in var:
        valor = 1 - math.exp(-l*valor)
        cdf.append(valor)
        i += 1
    var = sorted(var)
    cdf = sorted(cdf)
    plt.plot(var,cdf)
    plt.show()

exponencial_cdf(3)
#plt.hist (lista, 15, rwidth=0.9)
#plt.show ()