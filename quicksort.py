import time
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import *

'''
Autores: Eduardo Nunes Santos e Glaucia de Pádua da Silva

O algoritmo Quicksort utiliza o paradigma de programação conhecido como Dividir para Conquistar. 
Esse algoritmo usa uma abordagem recursiva, em que a entrada é ramificada várias vezes com o objetivo de quebrar o problema em partes menores.
A técnica de dividir para conquistar utilizada, tem como principal objetivo melhorar a performance sem a utilização de recurso computacional adicional.

O processo de ordenação se baseia em um elemento chamado pivô e nesse algoritmo selecionamos o último item da lista como pivô, mas é possível selecionar outros elementos também.
'''

def quick_sort(arr_entrada, inicio=0, fim=None):
    '''
    Implementação de algoritmo de ordenação quick_sort.
    
    Parameters
        arr_entrada (array): array para ser ordenado
        inicio (int): início do array
        fim (int): fim do array
    '''
                                                                                                    #Custo                      Pior caso
    if fim is None:                                                                                 # C1                        * 1
        fim = len(arr_entrada)                                                                      # C2                        * 1
    
    if inicio < fim:                                                                                # C3                        * 1
        parte = particao(arr_entrada, inicio, fim)                                                  # C4                        * P(n) = n
        quick_sort(arr_entrada, inicio, parte)                                                      # C5                        * T(1) 
        quick_sort(arr_entrada, parte + 1, fim)                                                     # C6                        * T(n-1)
    return arr_entrada                                                                              # C7                        * 1

def particao(arr_entrada, inicio, fim):
    pivo = arr_entrada[fim - 1]                                                                     # C8                        * 1
    iteracoes = range(inicio, fim)                                                                  # C9                        * 1
    
    for i in iteracoes:                                                                             # C10                       * (n + 1)
        if arr_entrada[i] <= pivo:                                                                  # C11                       * n
            inicio += 1                                                                             # C12                       * n
            arr_entrada[i], arr_entrada[inicio - 1] = arr_entrada[inicio - 1], arr_entrada[i]       # C13                       * n
            
    return inicio - 1                                                                               # C14                       * 1
                                                                                                    # P(n) = 3 * C + 4 * n
                                                                                                    # P(n) => O(n)

def merge(vetor, p, q, r):
    n1 = q-p+1
    n2 = r-q
    vetorL = [0] * (n1+1) 
    vetorR = [0] * (n2+1) 

    for i in range (n1):
        vetorL[i] = vetor[p+i]

    for i in range (n2):
        vetorR[i] = vetor[q+i+1]

    vetorL[n1] = math.inf 
    vetorR[n2] = math.inf

    i = 0
    j = 0

    for k in range (p, r+1):
        if vetorL[i] <= vetorR[j]:
            vetor[k] = vetorL[i]
            i += 1
        else:
            vetor[k] = vetorR[j]
            j += 1
    
    return vetor

def mergesort(vetor, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(vetor, p, q)
        mergesort(vetor, q+1, r)
        merge(vetor, p, q, r)                                                                                                                                                                                

def main():
    a = list(np.random.randint(1,100,2000))

    print("Array original: " + str(a))

    antes_quick_sort = time.process_time()
    arr_ordenado_qs = quick_sort(a)    
    depois_quick_sort = time.process_time()

    antes_merge_sort = time.process_time()
    mergesort(a, 0, len(a)-1)    
    depois_merge_sort = time.process_time()

    tempo_qs = depois_quick_sort - antes_quick_sort
    tempo_ms = depois_merge_sort - antes_merge_sort

    print("\nTempo de execução do quick sort: "+str(tempo_qs))
    print("Tempo de execução do merge sort: "+str(tempo_ms))

    print("\nArray ordenado do quick sort: " + str(arr_ordenado_qs))
    print("Array ordenado do merge sort: " + str(a))

if __name__ == "__main__":
    main() 