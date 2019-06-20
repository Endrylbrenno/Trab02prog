num = input("Digite um numero a ser criptografado: ")
n = str(num)
n1 = ((int(n[0]))+6)%10
n2 = ((int(n[1]))+6)%10
n3 = ((int(n[2]))+6)%10
n4 = ((int(n[3]))+6)%10
aux=n1
n1=n3
n3=aux
aux=n2
n2=n4
n4=aux
print("Número criptografado: {0}{1}{2}{3}".format(n1,n2,n3,n4))
num = input("Digite um numero a ser descriptografado: ")
n = str(num)
n1 = int(n[0])
if  n1 <= 9 and n1 >= 6:
    n1 = n1 - 6
else:
    if (n1 <= 5) and (n1 >= 0):
        n1 = n1 + 4
n2 = int(n[1])
if n2 <= 9 and n2 >= 6:
    n2 = n2 - 6
else:
    if n2 <= 5 and n2 >= 0:
        n2 = n2 + 4
n3 = int(n[2])
if n3 <= 9 and n3 >= 6:
    n3 = n3 - 6
else:
    if n3 <= 5 and n3 >= 0:
        n3 = n3 + 4
n4 = int(n[3])
if n4 <= 9 and n4 >= 6:
    n4 = n4 - 6
else:
    if n4 <= 5 and n4 >= 0:
        n4 = n4 + 4
aux=n1
n1=n3
n3=aux
aux=n2
n2=n4
n4=aux
print("Número descriptografado: {0}{1}{2}{3}".format(n1,n2,n3,n4))
