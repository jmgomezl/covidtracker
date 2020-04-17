import random
from collections import defaultdict

n = 100

def lista_aleatorios(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = round(random.random()*100)
    return lista

l1 = lista_aleatorios(n)
l2 = lista_aleatorios(n)

matriz = [l1,l2]

def indices(lista):
    aux = defaultdict(list)
    for index, item in enumerate(l1):
        aux[item].append(index)
    return {item: indexs for item, indexs in aux.items() if len(indexs) > 1}

def niveles_superiores(dict_result,nivel):
    list_keys_n1 = list(dict_result.keys())
    for n in range(1,nivel):
        number_level = "nivel_" + str(n+1)
        previous_level = "nivel_" + str(n)
        for key in range(len(list_keys_n1)):
            level = []
            values = dict_result[list_keys_n1[key]][previous_level]
            for v in range(len(values)):
                if values[v] in dict_result:
                    level += dict_result[values[v]]["nivel_1"]
            level = list(set(level))
            dict_result[list_keys_n1[key]][number_level] = level
    return dict_result

def niveles(matriz, nivel =1):
    l1 = matriz[:][0]
    l2 = matriz[:][1]
    dict_result = {}
    index_l1  = indices(l1)
    list_keys = list(index_l1.keys())
    for key in range(len(list_keys)):
        dict_result[list_keys[key]] = {}
        n1 = []
        values = index_l1[list_keys[key]]
        for v in range(len(values)):
            n1.append(l2[values[v]])
        n1 = list(set(n1))
        dict_result[list_keys[key]]["nivel_1"]=n1
    if nivel > 1:
        dict_result = niveles_superiores(dict_result,nivel)
    return dict_result

# Prueba de los resultados a 4 niveles
print(niveles(matriz,4))
