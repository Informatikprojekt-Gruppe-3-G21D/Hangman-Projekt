# Library "random" importieren, um ein zufälliges Wort aus der Liste auszusuchen (sonst nicht möglich)
import random


# Wörterliste (Alle Wörter, die gesucht sein könnten)
Wörter = ["banane"]

# Zufälliges Wort aus der Liste wird ausgesucht
GesuchtesWort = random.choice(Wörter)
BuchstabenListe = []
for char in GesuchtesWort:
    BuchstabenListe.append(char) 

GeratenerBuchstabe = input("Rate einen Buchstaben: ") #Frage nach Eingabe
if GeratenerBuchstabe in BuchstabenListe: 
    print("richtig")
else: 
    print("falsch")
    
# MIT License: Copyright (c) [2022] [Larissa Carver, Michelle Koch, Sophie Germann]