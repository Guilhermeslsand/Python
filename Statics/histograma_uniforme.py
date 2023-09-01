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

def histograma (num, maior, menor):
    pdf = uniforme_pdf(maior, menor)
    variacao = (maior - menor)/ num
    vetor_var = list()
    intervalo = menor + variacao
    while intervalo <= maior:
        vetor_var.append(intervalo)
        intervalo = intervalo + variacao
    vetor_var.append(maior) 
    i = 0
    freq = list()
    while i < num:
        freq.append(0)
        i += 1
    i = 0
    while i < num:
        for valor in pdf:
            if valor < vetor_var[i]:
                freq[i] += 1
        i += 1
    print(freq)
    print(vetor_var)
    
def uniforme_cdf (maior, menor):
    pdf = uniforme_pdf(maior, menor)
    cdf = list()
    i = 0
    for valor in pdf:
        valor = (valor-maior)/(menor-maior)
        cdf.append(valor)
        i += 1 
    print(pdf)

histograma(10,12,4)