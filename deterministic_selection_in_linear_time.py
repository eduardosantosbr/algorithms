def Particionar(A, inicio, fim, k):
    A[k], A[fim] = A[fim], A[k] 
    pivo = A[fim]
    i = inicio-1
    for j in range(inicio, fim):
        if A[j] <= pivo:
            i += 1
            A[i], A[j] = A[j], A[i] 
    A[i+1], A[fim] = A[fim], A[i+1]
    return i+1 


def SelecaoDeterministica(A, inicio, fim, iesimo):

    if inicio == fim:
        return (A[inicio], inicio)
    
    # Mapa para identificar as posições originais
    mapa = {}
    for j in range(0, len(A)):
        mapa[A[j]] = j
    
    
    # Quebra a em m vetores de tamanho 5
    parts = [A[pos:min(pos + 5, fim)] for pos in range(inicio, fim+1, 5)]
    
    # Ordena cada um dos m vetores
    for part in parts:
        part.sort()
    
    # Cria um vetor com as medianas de cada um dos m vetores
    medianas = []
    for part in parts: 
        medianas.append(part[int(len(part)/2)])
    
    # Encontra a mediana das medianas
    (V, _) = SelecaoDeterministica(medianas, 0, len(medianas)-1, int(len(medianas)/2)+1)
    posicao = mapa[V]
    
    posicao = Particionar(A, inicio, fim, posicao)
    
    # Se a posição da mediana encontrada for igual ao i-esimo -1, significa que o número foi encontrado
    if iesimo-1 == posicao:
        return (A[posicao], posicao)
    else:
        # Senão, caso o número encontrado for maior que o iésimo, significa que o iésimo está em um intervalo abaixo
        if iesimo-1 < posicao:
            return SelecaoDeterministica(A, inicio, posicao-1, iesimo)
        # Se for menor, significa que o iésimo está em um intervalo acima
        else: 
            return SelecaoDeterministica(A, posicao+1, fim, iesimo)
            
    



#sequencia de exemplo
A = [8, 9, 82, 3, 12, 5, 67, 26, 84, 97, 13, 2, 1]
#se estivesse ordenada seria: [1, 2, 3, 5, 8, 9, 12, 13, 26, 67, 82, 84, 97]

copia_de_A = A[:]
iesimo_da_sequencia = 9
(V, _) = SelecaoDeterministica(A, 0, len(A)-1, iesimo_da_sequencia)

print("Dada a sequência "+str(copia_de_A)+",")
print("o "+str(iesimo_da_sequencia)+"° número da sequência é: "+str(V))