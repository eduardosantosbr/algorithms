import math

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
    A = [10,9,8,7,6,5,4,3,2,1] 
    mergesort(A, 0, len(A)-1)
    print(A)
    
if __name__ == "__main__":
    main() 