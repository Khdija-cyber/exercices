U1 = []
L = []
U2 = [0]*8
for i in range(8):
    n= int(input("entrer un nombre:"))
    U1.append(n)
for i in range(8):
    while True:
        x = int(input("entrer une valeur 1 ou 0 seulement:"))
        if (x==0) or (x==1):
            L.append(x)
            break
for i in range(8):
    if L[i] == 1:
        U2[i] = U1[i]
print(U1)
print(L)
print(U2)