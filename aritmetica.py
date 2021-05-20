numero = int (input())
simbolo = input()
numero1 = int (input())
simbolo1 = input()
numero2 = int (input())

if simbolo == "+":
  if simbolo1 == "+":
    conta = numero + numero1 + numero2
  elif simbolo1 == "-":
      conta = numero + numero1 - numero2
  elif simbolo1 == "*":
      conta = numero + numero1 * numero2
  elif simbolo1 == "/":
      conta = numero + numero1 // numero2

if simbolo == "-":
  if simbolo1 == "+":
    conta = numero - numero1 + numero2
  elif simbolo1 == "-":
      conta = numero - numero1 - numero2
  elif simbolo1 == "*":
      conta = numero - numero1 * numero2
  elif simbolo1 == "/":
      conta = numero - numero1 // numero2

if simbolo == "*":
  if simbolo1 == "+":
    conta = numero * numero1 + numero2
  elif simbolo1 == "-":
      conta = numero * numero1 - numero2
  elif simbolo1 == "*":
      conta = numero * numero1 * numero2
  elif simbolo1 == "/":
      conta = numero * numero1 // numero2

if simbolo == "/":
  if simbolo1 == "+":
    conta = numero / numero1 + numero2
  elif simbolo1 == "-":
      conta = numero / numero1 - numero2
  elif simbolo1 == "*":
      conta = numero / numero1 * numero2
  elif simbolo1 == "/":
      conta = numero / numero1 // numero2

print(conta,end="")