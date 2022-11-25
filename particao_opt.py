import math

def particao_opt(S, n, k):
  #casos base
  if k == 1:
    return sum(S[:n+1])
  if n == 0: 
    return S[0]
  minimum = math.inf

  lstIteracao = range(0, n)
  for i in lstIteracao:
    particao = particao_opt(S, i, k-1)
    restante = sum(S[i+1:n+1])
    val = max(particao, restante)
    minimum = min(minimum, val)

    minimum = min(minimum, max(particao, restante))

  return minimum

def main():
  S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  k = 3
  print(particao_opt(S, len(S)-1, k))

if __name__ == "__main__":
  main()