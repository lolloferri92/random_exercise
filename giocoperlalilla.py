age=0
while True:
    age=input("questo giochino è per la lilla, ti prego lilla dimmi quanti anni hai")
    print(age)
    if int(age)!=27:
        print("hai detto " +str(age) +"........ sei sucura?\ndobbiamo ricominiciare federicaaaaaa, muoviti ")
        continue
    else:
        print("brava lilla sei veciaaaaa!!!!!!!!!!")
        break
print("il giochino finisce qua")
