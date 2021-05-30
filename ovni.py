T = int(input())
for t in range(T):
  linha = input().split(" ")
  somatoria = int(linha[0]) + int(linha[1])
  if somatoria <= int(linha[2]):
    print ('CABE!', end="" if t == T - 1 else "\n")
  elif somatoria >= int(linha[2]):
    print ('NAO CABE!', end="" if t == T - 1 else "\n")