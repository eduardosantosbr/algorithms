import math
import matplotlib.pyplot as plt

#distância euclidiana
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 ) 

def main():
  #Mapa dos colegas (coordenadas)
  Colegas = {"Ana", "Afonso", "José", "Carla", "Mario", "Luiza", "Diana", "Lúcio", \
     "Anita", "Marcela", "Amanda", "João", "Laura", "Luciana", "Marta", \
     "Luana", "Marcos", "Betania", "Bruna", "Sebastião", "Lucas", "Carolina"}
  Coor = {
      "Ana":            (38,54), \
      "Afonso":         (35,48), \
      "José":           (32,54), \
      "Carla":          (29, 7), \
      "Mario":          (28,12), \
      "Luiza":          (27, 7), \
      "Diana":          (27,54), \
      "Lúcio":          (22, 1), \
      "Anita":          (22,34), \
      "Marcela":        (22,42), \
      "Amanda":         (21, 3), \
      "João":           (20,36), \
      "Laura":          (18,36), \
      "Luciana":        (13,45), \
      "Marta":          (11,45), \
      "Luana":          ( 9, 2), \
      "Marcos":         ( 9, 4), \
      "Betania":        ( 7, 3),\
      "Bruna":          ( 5,24),\
      "Sebastião":      ( 4,26),\
      "Lucas":          ( 3,21),\
      "Carolina":       ( 2,24)
  }

  #criando tradutores: rótulos para id e id para rótulos
  id = 0
  idPRot = [None]
  rotPid = {}
  for col in Colegas:
    id+=1
    idPRot.append(col)
    rotPid[col] = id
  
  #criando distância entre os pares
  E = []
  for c1 in Colegas:
    u = rotPid[c1]
    for c2 in Colegas:
      v = rotPid[c2]
      if u<v:
        E.append([u, v,  dist(Coor[c1], Coor[c2])])
  
  #exibindo pontos
  X = []
  Y = []
  for v in idPRot:
    if v!=None:
      X.append(Coor[v][0])
      Y.append(Coor[v][1])

  plt.scatter(X, Y, c='red')
  plt.show()

  #encontrar Grupos
  k = 7 # número de grupos
  A = kruskal_clustering(len(Colegas), E, k)
  print(A)

  #exibindo grupos como árvores
  g = nx.Graph(A)
  nx.draw_networkx(g, labels={rotPid[v]:v for v in rotPid},   with_labels=True, pos={rotPid[v]:Coor[v] for v in rotPid}) 
 
if __name__ == "__main__":
  main()