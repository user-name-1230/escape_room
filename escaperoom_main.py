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
from termcolor import colored
import random
from adventurelib import when, say, start, set_context
import adventurelib
# from inventory import *
# from room_1 import *
# from room_2 import *
# from room_3 import *
# from room_4 import *
# from room_5 import *
# from room_6 import *


import inventory
import room_1

print(colored("Test", "red"))
say(colored("""Test say \n
            test""", "yellow"))

def no_command_matches(command):
    print(colored(random.choice([
        "Das habe ich nicht verstanden.",
        f"Ich verstehe '{command}' leider nicht.",
        "Tur mir leid, diese Aktion scheint nicht zur Verfügung zu stehen.",
        f"Tut mir leid, die Aktion '{command}' scheint nicht zur Verfügung zu stehen."
    ]), "red"))

adventurelib.no_command_matches = no_command_matches



# Start #
print(colored("cmds for debug: debugraum, debugitem", "cyan"))

# Einleitungsstory
say(colored("""----------------------------------------------------------------------------------""", "yellow"))
say(colored("""Einleitung: \n
    Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste
    eingeladen. Unter anderem das BMI und somit Ministerin Schrader. Du, als
    technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten,
    welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef Herr Solar
    führt Ministerin Schrader, das Fernsehteam und dich durch die Anlage. Nach
    einigen Minuten gelangt ihr in das Herzstück des AKWs – den Kontrollraum –
    welches sich hinter einer meterdicken Sicherheitstür befindet.""", "yellow"
))
say("""""")
say(colored("""Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt
    Herr Solar den Countdown herunter. Die Journalisten außerhalb des Kraftwerks
    lauschen gespannt mit. Ministerin Schrader hat bereits die Hand auf dem großen
    roten Knopf. 5...4...3...2........plötzlich völlige Dunkelheit.""", "yellow"
))
say("""""")
say(colored("""Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit
    geht ein rot-pulsierendes Notlicht an und im Kontrollraum verhallt das
    Warnsignal aus dem Maschinenraum. Die Sicherheitstür wird mit einem Knall
    verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf
    erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk
    übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen
    heruntergefahren.“""", "yellow"
))
say("""""")
say(colored("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""", "yellow"))
say("""""")
say(colored("""„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von
    100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“""", "yellow"
))
say("""""")
say(colored("""Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort
    beschriftet ist. Na toll…Ransomware. Der Chef des Kraftwerks ist erschüttert und
    erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze
    kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er
    vor Schreck in Ohnmacht. Ministerin Schrader greift sofort zum Telefon um den
    Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen
    Empfang. Die Wände des Kontrollraums sind zu dick. Das Fernsehteam steht ratlos
    in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass
    eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender
    mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer
    Lösung.""", "yellow"
))


#Start
set_context("room1")
room_1.ueberleitung_room1()


# Debug #


@when("debugraum")
def debug_room():
    debug_input = input(colored("In welchen Raum möchten Sie springen [1, 2, 3, 4, 5, 6]: ", "cyan"))
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
def debug_item():
    debug_input = input(colored("Welches ITEM hinzufügen [brecheisen, smartphone, haarnadel, simkarte]: ", "cyan"))
    if debug_input == "brecheisen":
        inventory.add(inventory.crowbar)
    elif debug_input == "smartphone":
        inventory.add(inventory.smartphone)
    elif debug_input == "haarnadel":
        inventory.add(inventory.hairpin)
    elif debug_input == "simkarte":
        inventory.add(inventory.sim)


# start
start()
