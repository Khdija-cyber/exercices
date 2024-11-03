#donner à saisir :
#var   T1=[],T2=[], T=[] , n :entier
#Début:
   #Ecrire("donner la valeur de T1,T2")
   #pour i=0 à n-1 faire
      #T[i]<---T1[i]+T2[I]
    #Finpour 
   #Ecrire(T[i])
#FIN
T1=[1,2,3,4,5]
T2=[6,7,8,9,10]
T = []
for i in range(len(T1)):
        T.append(T1[i] + T2[i])
print("T'est la somme de T1 et T2 :", T)
