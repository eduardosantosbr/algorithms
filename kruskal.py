def kruskal(g):
  #define uma árvore para cada vértice (S[v] contém os nodos da árvore)
  S = [{v} for v in range(len(g.vertices)+1)]
  #critério: pelo menor peso
  L = sorted(g.arestas, key=lambda x: g.pesoAresta(x[0], x[1]))
  #define a estrutura da solução
  A = []
  for [u, v] in L:
    #se as árvores forem diferentes, {u, v} é uma aresta segura
    if S[u] != S[v]:
      #adiciona aresta à solução
      A.append([u, v])
      #atualiza árvores
      x = S[u].union(S[v])
      for z in  x:
        S[z] = x
  #retorna a solução (conjunto de arestas)
  return A

  
def main():
  arquivo = "/content/gdrive/My Drive/instancias/agm_tiny.net"
  
  g1 = Grafo(arquivo)
  A = kruskal(g1)
  print(A)
  print('Soma: ', sum([g1.pesoAresta(u, v) for [u, v] in A]))

  #exibindo árvore
  g = nx.Graph(A)
  nx.draw_networkx(g,  with_labels=True, labels=g1.vertices) 

if __name__ == "__main__":
  main()
