def busca_binaria(lista, valor):
    min = 0
    max = len(lista) - 1
    while min <= max:
        med = (min + max) // 2
        if lista[med] == valor:
            return med
        elif lista[med] > valor:
            max = med - 1
        else:
            min = med + 1
    return -1

def busca_binaria_recursiva(lista, valor, min=0, max=None):
    if not max:
        max = len(lista)-1
    if max >= min:
        med = (max + min)//2
        if lista[med] == valor:
            return med
        elif lista[med] > valor:
            return busca_binaria_recursiva(lista, valor, min=min, max=med-1)
        else:
            return busca_binaria_recursiva(lista, valor, min=med+1, max=max)
    else:
        return -1