# file per provare cicli e condizioni
print("programma per provare i cicli e e le condizioni")
number=input("digitare un numero")
colour=input("digitare il colore tra rosso o qualcos'altro")
number= float(number)

if (number<10 and colour=="rosso"):
    print("il numero che hai digitato è minore di 10 ed è rosso")
elif(number>=10 and colour=="rosso"):
    print("il numero che hai digitato è maggiore-uguale di 10 ed è rosso")
elif(number<10 and colour!="rosso"):
    print("il numero che hai digitato è minore di 10 ma non è rosso")
else:print("il numero che hai digitato è maggiore-uguale di 10 e non è rosso")

#mi raccomando ai due punti dopo le condizioni elif e nelle altre in generale