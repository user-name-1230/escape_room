# TODO
# Texte in der Einleitung langsamer machen
# Mehr Sätze
# Umlaute
# Ausrüstung / Kontrollrechner anschauen / benutzen / neustarten
# Inventar anschauen

# ventile / pumpenventile
# Mehr möglichkeiten
# Ventileingaben besser machen
# Brechstange wird automatisch benutzt

# Bild muss geschlossen werden
# Fotos / Pinnwand anschauen
# Hinweis auf L
# Hinweis auf Karte für Lösung
# "Benutze" öfter
# in raum gehen weglassen
# Spind öffnen
# haarnadel benutzen
# simslot öffnen
# pin eingeben
# Überleitung zu Raum 5

# exit in cmd
# ls richtig einrücken
# Überleitung in Raum 6
# NICHT STRG-C DRÜCKEN

# Hinweis zum Lückentext
# lower()
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import adventurelib
import sys
from room_1 import *
from room_2 import *
from room_3 import *
from room_4 import *
from room_5 import *
from room_6 import *



def no_command_matches(command):
    print(random.choice([
        "Das habe ich nicht verstanden.",
        f"Ich verstehe '{command}' leider nicht.",
        "Tur mir leid, diese Aktion scheint nicht zur Verfügung zu stehen.",
        f"Tut mir leid, die Aktion '{command}' scheint nicht zur Verfügung zu stehen."
    ]))

adventurelib.no_command_matches = no_command_matches



# Start #
print("cmds for debug: debugraum, debugitem")

# Einleitungsstory
say(
"""----------------------------------------------------------------------------------"""
)
say(
    """Einleitung: \n
Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste
eingeladen. Unter anderem das BMI und somit Ministerin Schrader. Du, als
technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten,
welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef Herr Solar
führt Ministerin Schrader, das Fernsehteam und dich durch die Anlage. Nach
einigen Minuten gelangt ihr in das Herzstück des AKWs – den Kontrollraum –
welches sich hinter einer meterdicken Sicherheitstür befindet."""
)
say("""""")
say(
    """Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt
Herr Solar den Countdown herunter. Die Journalisten außerhalb des Kraftwerks
lauschen gespannt mit. Ministerin Schrader hat bereits die Hand auf dem großen
roten Knopf. 5...4...3...2........plötzlich völlige Dunkelheit."""
)
say("""""")
say(
    """Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit
geht ein rot-pulsierendes Notlicht an und im Kontrollraum verhallt das
Warnsignal aus dem Maschinenraum. Die Sicherheitstür wird mit einem Knall
verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf
erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk
übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen
heruntergefahren.“"""
)
say("""""")
say("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""")
say("""""")
say(
    """„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von
100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“"""
)
say("""""")
say(
    """Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort
beschriftet ist. Na toll…Ransomware. Der Chef des Kraftwerks ist erschüttert und
erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze
kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er
vor Schreck in Ohnmacht. Ministerin Schrader greift sofort zum Telefon um den
Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen
Empfang. Die Wände des Kontrollraums sind zu dick. Das Fernsehteam steht ratlos
in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass
eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender
mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer
Lösung."""
)



# Inventar #
crowbar = Item("brecheisen")
smartphone = Item("smartphone")
hairpin = Item("haarnadel")
sim = Item("simkarte")
inventory = Bag()


@when("inventar")
@when("inventar zeigen")  # zeigen
@when("zeige inventar")
@when("inventar anzeigen")  # anzeigen
@when("anzeige vom inventar")
@when("öffne inventar")  # öffnen
@when("inventar öffnen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f"*{item}")

#Start
set_context("room1")
ueberleitung_room1()


# Debug #


@when("debugraum")
def debug():
    print("RAUMNAMEN GENAU EINGEBEN!")
    print("1,2,3,4,5,6")
    debug_input = input("In welchen Raum springen? ")
    if debug_input == "1":
        set_context("room1")
    elif debug_input == "2":
        set_context("room2")
    elif debug_input == "3":
        set_context("room3")
    elif debug_input == "4":
        set_context("room4")
    elif debug_input == "5":
        set_context("room5")
    elif debug_input == "6":
        set_context("room6")


@when("debugitem")
def debug2():
    print("ITEMNAMEN GENAU EINGEBEN!")
    print("brecheisen, smartphone, haarnadel, simkarte")
    debug_input = input("Welches ITEM hinzufügen: ")
    if debug_input == "brecheisen":
        inventory.add(crowbar)
    elif debug_input == "smartphone":
        inventory.add(smartphone)
    elif debug_input == "haarnadel":
        inventory.add(hairpin)
    elif debug_input == "simkarte":
        inventory.add(sim)


## start ###
start()
