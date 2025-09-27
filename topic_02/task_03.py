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

match dia:
    case "+":
      print(plus(a,b))
    case "-":
      print(minus(a,b))
    case "*":
      print(multi(a,b))        
    case "/":
      print(dil(a,b))
    case _:
      print("Неправильна дія")