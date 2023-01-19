import random
Wörter = ["b a n a n e", "f u c h s", "g r o s s m u t t e r", "e n d o p l a s m a t i s c h", "c h l o r o p l a s t e n", "w o l k e n k r a t z e r", "d r a c h e", "m i c k e y", "a b f a l l e i m e r", "d r a c u l a", "v a m p i e r", "g u r k e", "h a s e","a p f e l","h o n o l u l u","w e i h n a c h t s m a n n"]
BuchstabenListe = []
GesuchtesWort = random.choice(Wörter)
print(GesuchtesWort)

# Folgende Zeile zählt die Anzahl Buchstaben vom gesuchten Wort (GesuchtesWort) und stellt diese graphisch dar (Zeile 14)
for element in GesuchtesWort:
    print("_ ")
#StricheFürBuchstaben = "_ "* len(GesuchtesWort)
#print(StricheFürBuchstaben)

# Anzal Buchstaben des gesuchten Wortes werden als Striche wiedergegeben
BuchstabenListe.append(GesuchtesWort)
    #Frage = input("Rate einen Buchstaben: ")

    #if Frage ==