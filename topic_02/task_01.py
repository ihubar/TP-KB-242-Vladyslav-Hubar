import math

def discr(a,b,c):

  return b*b-4*a*c

a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))
  
def solve(a, b, c):
    D = discr(a,b,c)
    
    if D < 0:
        print("Коренів немає")
    elif D == 0:
        result = -b / (2*a)
        print("Один корінь:", result)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Два корені:","x1=",x1,"x2=",x2)

solve(a, b, c)