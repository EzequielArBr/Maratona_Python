linhas = int(input())

resultados = []

for i in range(0, linhas):
    resultados.append(input())

for n in range(0, len(resultados)):
    resultado = list(map(int, resultados[n].split()))
    print(min(resultado), end=" ")
    print(max(resultado))
    if len(set(resultado)) == 1:
        print("S", end="" if n == len(resultados) - 1 else "\n")
    else:
        print("N", end="" if n == len(resultados) - 1 else "\n")
    