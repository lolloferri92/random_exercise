#programma per fare i cicli while e for comparati
print("lista con ciclo while")
i=0
while i<10:
    print (i)
    i+=1
print("lista con ciclo for")
for counter in range(10):
    print(counter)

#programma per fare i cicli while e for comparati con intervallo di 3 e partendo da 2 e finendo a 15
print ("programma per fare i cicli while e for comparati con intervallo di 3 e partendo da 2 e finendo a 15")
i=3
while i<=15:
    print(i)
    i+=2

for u in range(3,16,2):
    print(u)

def paricheck(x):
    if x%2==0:
        return True
    else:
        return False
print ("lista con ciclo while break e continue")
#esempio di ciclo infinito con breack e continue
i=0
while True:
    if i==26:
        break
    elif paricheck(i)!=True:
        i+=1
        continue
    else:
        print("infinite" + str(i))
        i+=1
