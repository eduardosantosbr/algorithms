# greedy algorithm from intervals
def maximoIntervalos(R, s, f):  
  L = R.copy()
  L = sorted(L, key = lambda x: f[x]) 
  
  A = []
  i = 0
  while i < len(L):
    A.append(L[i])
    j = i + 1
    while j < len(L) and s[L[j]] <= f[L[i]]:
      j+=1
    i=j
  
  return A

def main():
    R = ["a", "b", "c", "d", "e"]
    s = {"a": 1,  "b": 2, "c": 4, "d": 6, "e": 8}
    f = {"a": 10, "b": 3, "c": 5, "d": 7, "e": 9}
    A = maximoIntervalos(R, s, f)
    print("Máximo de "+str(len(A))+": "+str(A))
   
if __name__ == "__main__":
    main() 
