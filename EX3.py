T1 = []
T2 = []
T=[]
# Remplissage du tableau T1
for i in range(5):  # Vous pouvez changer la taille ici
    n = input(f"Entrez la valeur pour T1[{i}] : ")
    if n.isdigit():
        T1.append(int(n))
    else:
        break

# Remplissage du tableau T2
for i in range(5):
    v = input(f"Entrez la valeur pour T2[{i}] : ")
    if v.isdigit():
        T2.append(int(v))
    else:
        break
T = []
for i in range(len(T1)):  # On suppose que T1 et T2 ont la même longueur
    T.append(T1[i])
    T.append(T2[i])
print( "T1 :", T1)
print(" T2 :", T2)
print(" T  :", T)