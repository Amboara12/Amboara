# Entrez la valeur de a
a = int(input("entrer la valeur de a"))
b = int(input("entrez la valeur de b"))
c = int(input("entrez la valeur de c "))
delta = (b*b)-(4*a*c)
print("delta=", delta)
racine = pow(delta, 1/2)
print("racine=" + str(racine))
if delta < 0:
    print("delta negative alors pas de solutoin dans R")
if delta > 0:
    print("delta positive alors deux solution distinct x1 et x2")
    x1 = (-b + int(pow(delta, 1/2))) / (2*a)
    print("x1=" + str(x1))
    x2 = (-b - int(pow(delta, 1/2))) / (2*a)
    print("x2=" + str(x2))
if delta == 0:
    print("delta egal 0 alors il existe une solution double x1=x2")
    x = (-b / (2*a))
    print("x=" + str(x))
