troco = int (input())
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0


while troco >= 100:
  troco -= 100
  c100 += 1

while troco >= 50:
  troco -= 50
  c50 += 1

while troco >= 20:
  troco -= 20
  c20 += 1

while troco >= 10:
  troco -= 10
  c10 += 1

while troco >= 5:
  troco -= 5
  c5 += 1

while troco >= 2:
  troco -= 2
  c2 += 1

while troco >= 1:
  troco -= 1
  c1 += 1

print (f'{c100} nota(s) de R$ 100')
print (f'{c50} nota(s) de R$ 50')
print (f'{c20} nota(s) de R$ 20')
print (f'{c10} nota(s) de R$ 10')
print (f'{c5} nota(s) de R$ 5')
print (f'{c2} nota(s) de R$ 2')
print (f'{c1} nota(s) de R$ 1',end="")