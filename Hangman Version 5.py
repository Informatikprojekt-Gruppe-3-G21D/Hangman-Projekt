# Library "random" importieren, um ein zufälliges Wort aus der Liste auszusuchen (ansonsten nicht möglich)
import random 
  

# Wörterliste (Wörter, die gesucht sein könnten) 
Wörter = ["banane", "endoplasmatisch", "velostaender", "kakteen", "pausenbrot", "kaffeetasse", "liegestuhl", "xylophon", "teddybaer", "informatik", "fernseher", "millionaer", "wassertropfen", "nahrung", "lauch", "gurke", "zyklop", "rhythmus", "kaulquappe", "fischteich"]
 
# Zufälliges Wort aus der Liste wird ausgesucht  
GesuchtesWort = random.choice(Wörter) 


# Buchstabenliste wird mit den Buchstaben des gesuchten Wortes Erweitert  
BuchstabenListe = []
GesuchtesWort = str(GesuchtesWort)
for char in GesuchtesWort: 
    BuchstabenListe.append(char)

GerateneBuchstaben = []

# Start des visuellen Teils der Grafik: 

StricheFürBuchstaben = []
for char in BuchstabenListe: 
    StricheFürBuchstaben.append ("_ ")
    
print(*StricheFürBuchstaben)
Darstellungszahl = 0
chancen = 6

while (chancen > 0) and ("_ " in StricheFürBuchstaben):
    
    GeratenerBuchstabe = input("Rate einen Buchstaben: ") #Frage nach einer Eingabe
    
    if  ((GeratenerBuchstabe in BuchstabenListe) and (GeratenerBuchstabe not in GerateneBuchstaben)):
        print("richtig! Du darfst noch " + str(chancen) + " Fehler machen")
        i = [index for (index, letter) in enumerate(BuchstabenListe) if letter == GeratenerBuchstabe]
        for element in i: 
            StricheFürBuchstaben[element] = GeratenerBuchstabe
        print (*StricheFürBuchstaben)
        GerateneBuchstaben.append(GeratenerBuchstabe)

    elif GeratenerBuchstabe in GerateneBuchstaben: 
        print("Du hast diesen Buchstaben schon geraten! ") # Im Falle einer wiederholten Eingabe
        

    elif (GeratenerBuchstabe not in GerateneBuchstaben) and (GeratenerBuchstabe not in BuchstabenListe):
        chancen = chancen - 1
        #print("falsch, du darfst noch " + str(chancen) + " Fehler machen")
        Darstellungszahl = Darstellungszahl + 1
        if Darstellungszahl == 1: 
            print("-------------------")
            print(" ¦                 ¦")
            print(" ¦                 ¦")
            print(" ¦")
            print(" ¦")
            print(" ¦")
            print("--") 

        if Darstellungszahl == 2:
            print(" --------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦")
            print(" ¦                  O")
            print(" ¦")
            print(" ¦")
            print("---")
        
        if Darstellungszahl == 3: 
            print(" --------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦")
            print(" ¦                  O")
            print(" ¦                  I")
            print(" ¦                  I ")
            print("---")

        if Darstellungszahl == 4: 
            print(" --------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦") 
            print(" ¦                  O")
            print(" ¦                 /I\\")
            print(" ¦                  I")
            print("---")
            
        if Darstellungszahl == 5:
            print(" --------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦")
            print(" ¦                  O")
            print(" ¦                 /I\\") 
            print(" ¦                  I")
            print("---                / ")
        if Darstellungszahl == 6: 
            print(" --------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦")
            print(" ¦                  O")
            print(" ¦                 /I\\") 
            print(" ¦                  I")
            print("---                / \\")


    GerateneBuchstaben.append(GeratenerBuchstabe) # Erweiterung der Liste GerateneBuchstaben   

if chancen == 0 and ("_ " in StricheFürBuchstaben) :
    print("Keine Chancen übrig, du hast verloren! ")
    print(" --------------------")
    print(" ¦                  ¦")
    print(" ¦                  ¦")
    print(" ¦                  O")
    print("                  -----   Du bist tot!")
    print(" ¦                 /I\\") 
    print(" ¦                  I")
    print("---                / \\")
    
else: 
    print ("Du hast Gewonnen! Das gesuchte Wort war " + str(GesuchtesWort))
    
    
# MIT License: Copyright (c) [2022] [Larissa Carver, Michelle Koch, Sophie Germann]
