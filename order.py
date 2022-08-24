import math

def order(vetorL, vetorR):
    
    vetor = [0] * (len(vetorL)+len(vetorR))

    vetorL.append(math.inf)
    vetorR.append(math.inf)

    i = 0
    j = 0
    for k in range (len(vetor)):
        if vetorL[i] <= vetorR[j]:
            vetor[k] = vetorL[i]
            i += 1
        else:
            vetor[k] = vetorR[j]
            j += 1
    
    return vetor

def main():
    A = [1,9,11,44] 
    B = [1,3,10,40]
    X = order(A, B)
    print(X)
    
if __name__ == "__main__":
    main() 