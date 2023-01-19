# Library "random" importieren, um ein zufälliges Wort aus der Liste auszusuchen (ansonsten nicht möglich)
import random
# Library "mixer" importieren, um das Abspielen von Audiodateien zu ermöglichen (Library in Pygame)
from pygame import mixer
from time import sleep

# Mixer instantiieren (Instanziierung ist der Prozess des Lesens oder Angebens von Informationen, beispielsweise des Speichertyps und der Werte für ein Datenfeld. - https://www.ibm.com)
mixer.init()

# Lautstärke der Audiodateien definieren
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
print("Du fürchstest dich, hast mit deinem Leben bereits abgeschlossen. Doch nein, das darf nicht sein. Du bist unschuldig, warst zur falschen    Zeit am falschen Ort! Deine Willenskraft kehrt zurück: ")
print("")

print("Du: Bitte, lasst mich leben! – flehst du – ich bin unschuldig, bitte lasst mich gehen! ")
print("Henker: Nun gut, du hast eine Chance zu leben. Errätst du das von mir ausgedachte Wort mit weniger als sechs Fehlern, bleibst du am Leben. Das Spiel beginnt: ")

# Darstellung jedes Buchstabens des gesuchten Wortes als "_ "
StricheFürBuchstaben = []
for char in BuchstabenListe: 
    StricheFürBuchstaben.append ("_ ")
    
print(*StricheFürBuchstaben) # Die Striche werden abgedruckt, damit der Spieler weiss, wie viele Buchstaben das Wort hat
Darstellungszahl = 0 # Zahl, die angibt, welche Zeichnung bei einem Fehler abgedruckt werden sollte
chancen = 6 # Anzahl Chancen, die der Spieler zu Beginn hat


# While-Schlaufe, solange der Spieler noch Chancen zur Verfügung hat und noch nicht alle Buchstaben erraten hat
while (chancen > 0) and ("_ " in StricheFürBuchstaben):
    
    GeratenerBuchstabe = input("Rate einen Buchstaben: ") #Frage nach einer Buchstabeneingabe
    
    if  ((GeratenerBuchstabe in BuchstabenListe) and (GeratenerBuchstabe not in GerateneBuchstaben)): # Wenn der geratene Buchstaben noch nicht geraten wurde und im gesuchten Wort vorhanden ist
        print("richtig! Du darfst noch " + str(chancen) + " Fehler machen")
        
        # Stelle(n), wo der geratene Buchstaben im gesuchten Wort vorhanden ist
        i = [index for (index, letter) in enumerate(BuchstabenListe) if letter == GeratenerBuchstabe]
        
        # Jene Striche in der StricheFürBuchstaben-Liste, welche für den geratenen Buchstaben stehen, werden durch diesen ersetzt
        for element in i: 
            StricheFürBuchstaben[element] = GeratenerBuchstabe
            
        # StricheFürBuchstaben abdrucken (mit den bereits erratenen Buchstaben)
        print (*StricheFürBuchstaben)
        
        # Geratener Buchstabe zur Liste aller geratenen Buchstaben hinzufügen
        GerateneBuchstaben.append(GeratenerBuchstabe)
        
        # Audiodatei: klatschende Menge laden und abspielen
        mixer.music.load('crowd cheering.wav')
        mixer.music.play()

    elif GeratenerBuchstabe in GerateneBuchstaben: # Bereits geratene Buchstaben
        print("Du hast diesen Buchstaben schon geraten! ") # Im Falle einer wiederholten Eingabe
        print (*StricheFürBuchstaben) # StricheFürBuchstaben werden erneut gedruckt
        

    elif (GeratenerBuchstabe not in GerateneBuchstaben) and (GeratenerBuchstabe not in BuchstabenListe): # Wenn der Buchstabe noch nicht geraten wurde, aber auch nicht im gesuchten Wort vorhanden ist
        chancen = chancen - 1 # Chance wird abgezogen
        print (*StricheFürBuchstaben) #StricheFürBuchstaben wird erneut abgedruckt
        # Audiodatei: buhende Menge wird geladen und abgespielt
        mixer.music.load('crowd booing.wav')
        mixer.music.play()
        
        #Im Fall des zweiten Elif (falscher Buchstabe, noch nicht geraten) wird die Darstellungszahl um eines erhöht und die entsprechende Darstellung abgedruckt
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
            
            

    # Geratener Buchstabe wird zur Liste aller geratenen Buchstaben hinzugefügt
    GerateneBuchstaben.append(GeratenerBuchstabe) # Erweiterung der Liste GerateneBuchstaben

if chancen == 0 and ("_ " in StricheFürBuchstaben) : # Wenn alle Chancen aufgebraucht sind und das gesuchte Wort nicht vollständig erraten ist:
    print("Keine Chancen übrig, du hast verloren! ")
    print(" --------------------")
    print(" ¦                  ¦")
    print(" ¦                  ¦")
    print(" ¦                  O")
    print("                  -----   Du bist tot!")
    print(" ¦                 /I\\") 
    print(" ¦                  I")
    print("---                / \\")
    mixer.init()

    # Lautstärke der Audiodateien definieren
    mixer.music.set_volume(0.2)
    mixer.music.load('crowd laughing.wav')
    mixer.music.play()
    sleep(10)

    
    
    
else: # Wenn keine Striche mehr in der BuchstabenListe voranden sind (also alle Buchstaben erraten sind) -> Ausgabe: Du hast gewonnen. Das gesuchte Wort war z. B. Banane
    # Mixer instantiieren (Instanziierung ist der Prozess des Lesens oder Angebens von Informationen, beispielsweise des Speichertyps und der Werte für ein Datenfeld. - https://www.ibm.com)
    mixer.init()

    # Lautstärke der Audiodateien definieren
    mixer.music.set_volume(0.2)
    print ("Du hast Gewonnen! Das gesuchte Wort war " + str(GesuchtesWort))
    mixer.music.load('crowd cheering.wav')
    mixer.music.play()
    sleep(10)
    
    # Copyright (c) [2022] [Michelle Koch, Sophie Germann, Larissa Carver]
    
