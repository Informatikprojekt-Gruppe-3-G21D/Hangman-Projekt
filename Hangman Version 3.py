# Library "random" importieren, um ein zufälliges Wort aus der Liste auszusuchen (ansonsten nicht möglich)
import random


# Wörterliste (Wörter, die das Programm aussuchen kann)
Wörter = ["banane", "endoplasmatisch", "velostaender", "kakteen", "pausenbrot", "kaffeetasse", "liegestuhl", "xylophon", "teddybaer", "informatik", "fernseher", "millionaer", "wassertropfen", "nahrung", "lauch", "gurke", "zyklop", "rhythmus", "kaulquappe", "fischteich"]

# Zufälliges Wort aus der Liste wird ausgesucht
GesuchtesWort = random.choice(Wörter)


# Die Buchstaben des gesuchten Wortes werden zur Buchstabenliste hinzugefügt
BuchstabenListe = []
GesuchtesWort = str(GesuchtesWort)
for char in GesuchtesWort:
    BuchstabenListe.append(char)

GerateneBuchstaben = []



chancen = 6

while (chancen > 0): 
    
    GeratenerBuchstabe = input("Rate einen Buchstaben: ") #Frage nach einer Eingabe
    
    if  ((GeratenerBuchstabe not in GerateneBuchstaben) and (GeratenerBuchstabe in BuchstabenListe)):
        print("richtig! Du darfst noch " + str(chancen) + " Fehler machen")
        GerateneBuchstaben.append(GeratenerBuchstabe)

    elif GeratenerBuchstabe in GerateneBuchstaben: 
        print("Du hast diesen Buchstaben schon geraten! ") # Im Falle einer wiederholten Eingabe
        

    elif (GeratenerBuchstabe not in GerateneBuchstaben) and (GeratenerBuchstabe not in BuchstabenListe):
        chancen = chancen - 1
        print("falsch, du darfst noch " + str(chancen) + " Fehler machen")
      

    GerateneBuchstaben.append(GeratenerBuchstabe) # Erweiterung der Liste GerateneBuchstaben

if chancen == 0:
    print("Keine Chancen übrig, du hast verloren! Das gesuchte Wort war " + str(GesuchtesWort))

else: 
    print ("Du hast Gewonnen! Das gesuchte Wort war " + str(GesuchtesWort))
    


# MIT License: Copyright (c) [2022] [Larissa Carver, Michelle Koch, Sophie Germann]
