from datetime import datetime

def gerador_var (num):
    a = 9
    b = 7
    m = 2^30
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
        valor = valor/(m-1)
        var[i] = valor
        i += 1
    var.pop(0)
    return var
lista = gerador_var(3)
print(lista)