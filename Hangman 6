# Library "random" importieren, um ein zufälliges Wort aus der Liste auszusuchen (ansonsten nicht möglich)
import random
from pygame import mixer

#Instantiate mixer
mixer.init()

#Load audio file

#Set preferred volume
mixer.music.set_volume(0.2)


# Wörterliste (Wörter, die gesucht sein könnten)
Wörter = ["banane", "endoplasmatisch", "velostaender", "kakteen", "pausenbrot", "kaffeetasse", "liegestuhl", "xylophon", "teddybaer", "informatik", "fernseher", "millionaer", "wassertropfen", "nahrung", "lauch", "gurke", "zyklop", "rhythmus", "kaulquappe", "fischteich"]

# Zufälliges Wort aus der Liste wird ausgesucht
GesuchtesWort = random.choice(Wörter)


# Buchstabenliste wird mit den Buchstaben des gesuchten Wortes Erweitert (als Liste, jeder Buchstabe ist ein einzelnes Element)
BuchstabenListe = []
GesuchtesWort = str(GesuchtesWort)
for char in GesuchtesWort:
    BuchstabenListe.append(char)

GerateneBuchstaben = []

# Start des visuellen Teils der Grafik: 

print("Du stehst auf dem Marktplatz, die Menschenmasse drängt sich um dich und den dir drohenden Galgen. Sie werfen Tomaten und faule Eier auf    dich, fluchen und spucken.")
print("Du fürchstest dich, hast mit deinem Leben bereits abgeschlossen. Doch nein, das darf nicht sein. Du bist        unschuldig, warst zur falschen Zeit am falschen Ort! Deine Willenskraft kehrt zurück: ")
print("")

print("Du: Bitte, lasst mich leben! – flehst du – ich bin unschuldig, bitte lasst mich gehen! ")
print("Henker: Nun gut, du hast eine Chance zu leben. Errätst du das von mir ausgedachte Wort mit weniger als sechs Fehlern, bleibst du am Leben. Das Spiel beginnt: ")
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
        mixer.music.load('kultur0408.wav')
        mixer.music.play()

    elif GeratenerBuchstabe in GerateneBuchstaben: 
        print("Du hast diesen Buchstaben schon geraten! ") # Im Falle einer wiederholten Eingabe
        print (*StricheFürBuchstaben)
        

    elif (GeratenerBuchstabe not in GerateneBuchstaben) and (GeratenerBuchstabe not in BuchstabenListe):
        chancen = chancen - 1
        print (*StricheFürBuchstaben)
        #Play the music
        mixer.music.load('boooo.wav')
        mixer.music.play()
        
        Darstellungszahl = Darstellungszahl + 1
        if Darstellungszahl == 1: 
            print("--------------------")
            print(" ¦                  ¦")
            print(" ¦                  ¦")
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
