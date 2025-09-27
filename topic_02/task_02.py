def plus(a,b):
  return a+b

def minus(a,b):
  return a-b

def multi(a,b):
  return a*b

def dil(a, b):
  if b == 0:
      return "Помилка: ділення на нуль!"
  return a / b

dia = input("Привіт, вибери дію серед запропонованих:  + - * /  ")
a = int(input("Перше число:"))
b = int(input("Друге число:"))

if dia == "+":
  print(plus(a,b))
elif dia == "-":
  print(minus(a,b))
elif dia == "*":
  print(multi(a,b))
elif dia == "/":
  print(dil(a,b))