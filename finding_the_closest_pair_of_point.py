import matplotlib.pyplot as plt
import numpy as np
import math
import copy
import random

import time

def merge_set(vetor, inicio, meio, fim, pos):
    n1 = meio-inicio+1
    n2 = fim-meio
    esquerda = [0] * (n1+1) 
    direita = [0] * (n2+1) 

    for i in range (n1):
        esquerda[i] = vetor[inicio+i]

    for i in range (n2):
        direita[i] = vetor[meio+i+1]

    esquerda[n1] = (math.inf, math.inf)
    direita[n2] = (math.inf, math.inf)

    topoEsquerda = 0
    topoDireita = 0

    for k in range (inicio, fim+1):
        if esquerda[topoEsquerda][pos] <= direita[topoDireita][pos]:
            vetor[k] = esquerda[topoEsquerda]
            topoEsquerda += 1
        else:
            vetor[k] = direita[topoDireita]
            topoDireita += 1
    
    return vetor

def mergesort_set(vetor, inicio, fim, pos):
    if inicio < fim:
        meio = (inicio+fim)//2
        mergesort_set(vetor, inicio, meio, pos)
        mergesort_set(vetor, meio+1, fim, pos)
        merge_set(vetor, inicio, meio, fim, pos)

# Distância euclidiana de dois pontos
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 ) 
  
# Algoritmo que procura cada par de pontos
def menorDistanciaIterativoKT(P):
    min = math.inf
    d1, d2 = None, None
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if dist(P[i], P[j]) < min:
                min = dist(P[i], P[j])
                d1, d2 = P[i], P[j]
  
    return (min, d1, d2)

def parMaisProximoKT_DQ(Px, Py):
  # Se o sub problema for pequeno o suficiente, resolver diretamente
  if len(Px) <= 3:
    return menorDistanciaIterativoKT(Px) 
  else:
    meio = len(Px)//2

    xEsquerda = Px[:meio+1]
    yEsquerda = Py[:meio+1]
    xDireita = Px[meio+1:]
    yDireita = Py[meio+1:]
    
    (distancia_q, q0, q1) = parMaisProximoKT_DQ(xEsquerda, yEsquerda)
    (distancia_r, r0, r1) = parMaisProximoKT_DQ(xDireita, yDireita)

    menorDistancia = min(distancia_q, distancia_r)
    x_star = xEsquerda[len(xEsquerda)-1]
    S = []
    for p in Py:
      if dist(p, x_star) <= menorDistancia:
        S.append(p)

    # Encontrar os pares que cruzam a linha do meio
    distancia_s, s0, z0 = math.inf, None, None
    for i in range(len(S)):
      ponto_s = S[i]
      for j in range(i+1, min(len(S),15)):
        ponto_z = S[j]
        distancia_sz = dist(ponto_s, ponto_z)
        
        if distancia_sz < distancia_s:
          distancia_s, s0, z0 = distancia_sz, ponto_s, ponto_z

    if distancia_s < menorDistancia:
      return (distancia_s, s0, z0)
    else:
      if menorDistancia >= distancia_q:
        return (distancia_q, q0, q1)
      else:
        return (distancia_r, r0, r1)

def parMaisProximoKT(P):
    Px = P.copy()
    Py = P.copy()

    # Ordena pela coordenada x
    mergesort_set(Px, 0, len(Px)-1, 0)
    # Ordena pela coordenada y
    mergesort_set(Py, 0, len(Py)-1, 1)
     
    #chama a busca pela divisão e conquista
    return parMaisProximoKT_DQ(Px, Py)

n=1000

# Driver code
#pontos = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pontos = [(random.randint(-1000, 1000),random.randint(-1000, 1000)) for i in range(n)]

plt.scatter([x for (x,y) in pontos], [y for (x,y) in pontos], c='grey')

antes_kt = time.process_time()
mais = parMaisProximoKT(pontos)
print(mais)
depois_kt = time.process_time()

plt.scatter([mais[1][0]], [mais[1][1]], c='green')
plt.scatter([mais[2][0]], [mais[2][1]], c='red')
plt.show()

tempo_kt = depois_kt - antes_kt

print("KT:   "+str(tempo_kt))