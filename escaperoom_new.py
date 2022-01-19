from PIL import Image
import time
from adventurelib import Room, when, say, start, Bag, Item, set_context
import sys

### Globale Variablen ###
room_number = 1
sicherheitstuer_offen = False
ransomware_passwort_eingegeben = False


can_check_sim_slot = False
sim_schrank_offen = False
can_use_pin = False
klappe_offen = False
zugriff_computer = False
status_gesehen = False
check_sicherheitsausruestung = False

### Befehle: umschauen anschauen nehmen benutzen öffnen 'verwende mit' Inventar help quit 'Raum verlassen'

@when ("hilfe")
def zeige_befehle():
    print("[hilfe] [umschauen] [anschauen] [nehmen] [benutzen] [öffnen] [Verwende mit]\n[Inventar] [Raum verlassen]\n\n[help] (sehr große Hilfe) [quit]\nauf Groß- und Kleinschreibung wird kein Wert gelegt ;-)")

@when("raum verlassen") ## aktuell noch keine Auswahl...
def raum_verlassen():
    if (room_number == 1 and sicherheitstuer_offen == False):
        print("Die Tür ist verschlossen. Du kannst den Raum nicht verlassen")
    else:
        print("Du hast folgende Möglichkeiten:")
        print("Kontrollraum (1)")
#        print("Wohin? zB 1")
        raum = int(input("Wohin? zB 1"))
#        raum = int(raum)
#        if (raum == room_number)
#            print("Du befindest dich schon in diesem Raum!"
        print("Du gehst in den Kontrollraum")


### Inventar ###
# Liste möglicher Items
brecheisen = Item("brecheisen")
smartphone = Item("smartphone")
haarnadel = Item("haarnadel")
simkarte = Item("simkarte")
inventory = Bag()

# Inventar Grundlagen
@when("inventar")
#@when("inventar benutzen")  # benutzen
#@when("benutze inventar")
#@when("inventar anschauen")  # anschauen
#@when("anschauen inventar")
#@when("öffne inventar")  # öffnen
#@when("inventar öffnen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f"* {item}")

### Räume ###

room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room4 = Room("""Beschreibung des Lagerraums""")
room5 = Room("""Beschreibung des Büros""")

# Debug Infos #
print("cmds for debug: debugraum, debugitem")

# Einleitungsstory
say(
    """----------------------------------------------------------------------------------"""
)
say(
    """Einleitung: \n
Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste
eingeladen. Unter anderem das BMI und somit [Ministerin Schrader]. Du, als
technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten,
welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef [Herr Solar]
führt [Ministerin Schrader], das [Fernsehteam] und dich durch die Anlage. Nach
einigen Minuten gelangt ihr in das Herzstück des AKWs – den [Kontrollraum] –
welches sich hinter einer meterdicken [Sicherheitstür] befindet."""
)
input("...")
say(
    """Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt
[Herr Solar] den Countdown herunter. Die Journalisten außerhalb des Kraftwerks
lauschen gespannt mit. [Ministerin Schrader] hat bereits die Hand auf dem großen
roten Knopf. 5...4...3...2...plötzlich völlige Dunkelheit."""
)
input("...")
say(
    """Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit
geht ein rot-pulsierendes Notlicht an und im [Kontrollraum] verhallt das
Warnsignal aus dem [Maschinenraum]. Die [Sicherheitstür] wird mit einem Knall
verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf
erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk
übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen
heruntergefahren.“"""
)
input("...")
say("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""")
input("...")
say(
    """„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von
100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“"""
)
input("...")
say(
    """Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort
beschriftet ist. Na toll...Ransomware. Der Chef des Kraftwerks ist erschüttert und
erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze
kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er
vor Schreck in Ohnmacht. [Ministerin Schrader] greift sofort zum Telefon, um den
Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen
Empfang. Die Wände des Kontrollraums sind zu dick. Das [Fernsehteam] steht ratlos
in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass
eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender
mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer
Lösung."""
)
input("...")

########################
# RAUM 1: KONTROLLRAUM #
########################
# Einleitung Raum 1:
# Befehle: umschauen anschauen nehmen benutzen öffnen 'verwende mit' Inventar help quit
say(
    """----------------------------------------------------------------------------------"""
)
say(
    """Du befindest dich nun im [Kontrollraum]. Die Menge an Schaltern, Hebeln und
erschlägt dich fast und es fällt dir schwer deine Panik in den Griff zu
bekommen. Du versuchst dich zu sammeln und deine Möglichkeiten abzuwägen: \n
Du kannst dich im Raum [umschauen]\n
Du kannst Dinge im Raum [anschauen], [nehmen] und [benutzen]\n
Du kannst dein aktuelles [Inventar] anschauen\n
Du kannst dir [help] suchen, wenn du nicht weiterkommst, aber Vorsicht, dies ist eine sehr große Hilfe!\n
Du kannst mit [quit] das AKW verlassen (Spiel beenden)\n"""
)
# Startumgebung festlegen
inventory.add(smartphone)
set_context("room1")
room_number = 1

# Look Around #
@when("umschauen", context="room1")
#@when("schaue um", context="room1")
#@when("schau dich um", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    if sicherheitstuer_offen == False:
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und 
        erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. 
        Du siehst den [Kontrollrechner], [Sicherheitsausrüstung] in der Ecke und die verschlossene [Sicherheitstür]. 
        Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")
    elif ransomware_passwort_eingegeben == False:
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und 
        erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. 
        Du siehst den [Kontrollrechner], [Sicherheitsausrüstung] in der Ecke und die offene [Sicherheitstür]. 
        Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")
    else:
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und 
        erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. 
        Du siehst den [Kontrollrechner], bei dem ein [Zettel] am Kontrollpult klebt, [Sicherheitsausrüstung] in der Ecke und die offene [Sicherheitstür]. 
        Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")
        


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
        inventory.add(brecheisen)
    elif debug_input == "smartphone":
        inventory.add(smartphone)
    elif debug_input == "haarnadel":
        inventory.add(haarnadel)
    elif debug_input == "simkarte":
        inventory.add(simkarte)


## start ###
start()


def no_command_matches(command):
    print("Das habe ich nicht verstanden")
