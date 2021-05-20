entrada = input().split(" ")
x = int (entrada[0])
y = int (entrada[1])

if x == 0:
  if y == 0:
    print("NO ALVO!",end="")

if x > 0:
  if y > 0:
    print("R1",end="")

if x < 0:
  if y > 0:
    print("R2",end="")

if x < 0:
  if y < 0:
    print("R3",end="")

if x > 0:
  if y < 0:
    print("R4",end="")