# TODO
# Fehlermeldungen bei unbekannten Befehlen
# help Befehl deaktivieren? siehe ganz unten
# Beschreibung Räume, über Einleitungsstory

from PIL import Image
import time
from adventurelib import Room, when, say, start, Bag, Item, set_context
import sys


### Globale Variablen ###
sicherheitstuer_offen = False
ransomware_passwort_eingegeben = False
check_sicherheitsausruestung = False
brecheisen_schienbein = False

# unbenutzt...aus alter Version
can_check_sim_slot = False
sim_schrank_offen = False
can_use_pin = False
klappe_offen = False
zugriff_computer = False
status_gesehen = False



### allgemeine Befehle ### fuer jeden Raum

def no_command_matches(command):
    print("Das habe ich nicht verstanden")
    # das funktioinert leider nicht. Hinweise auf Befehl: [Hilfe] hinzufügen
    # siehe https://adventurelib.readthedocs.io/en/stable/customising.html


@when ("hilfe")
def zeige_befehle():
    print("Folge Befehle sind möglich:\n[hilfe] [umschauen] [anschauen] [nehmen] [benutzen] [öffnen] [Verwende mit]\n[Inventar] [Raum verlassen]\n\n[help] (sehr große Hilfe) [quit]\nauf Groß- und Kleinschreibung wird kein Wert gelegt ;-)")
# Befehle: umschauen anschauen nehmen benutzen öffnen 'verwende mit' Inventar help quit 'Raum verlassen'

@when ("nehmen")
@when("nimm")
def nehmen():
    print("Was möchtest du nehmen?")

@when ("benutzen")
@when("benutze")
def benutzen():
    print("Was möchtest du benutzen?")

@when ("anschauen")
@when("schaue an")
def anschauen():
    print("Was möchtest du anschauen?")

@when ("öffnen")
@when("öffne")
def oeffnen():
    print("Was möchtest du öffnen?")

@when ("verwende mit")
@when("verwenden mit")
def verwende_mit():
    print("Was möchtest womit verwenden?")
    print("zB verwende Smartphone mit dir")


@when("raum verlassen") ## aktuell nur Maschinenraum
def raum_verlassen():
    global room_number
    global sicherheitstuer_offen
    if (room_number == 1 and sicherheitstuer_offen == False):
        print("Die Tür ist verschlossen. Du kannst den Raum nicht verlassen")
    else:
        print("Du hast folgende Möglichkeiten:")
        print("(1) Kontrollraum")
        while 1:
            wohin = input("Wohin? Bitte Nummer eingeben:")
            if (wohin == "1"):
                break
            else:
                print("dies ist kein Raum, bitte Nummer eingeben, zB 1")
        wohin = int (wohin)
        if (wohin == room_number):
            print("Du befindest dich schon in diesem Raum!")
        else:
            print("Du gehst in den Raum")
            room_number = wohin
# umschauen einbauen, als Hinweis in welchem Raum jetzt

### Inventar ###
# Liste möglicher Items
brecheisen = Item("brecheisen")
smartphone = Item("smartphone")
# ab hier unbenutze Items
haarnadel = Item("haarnadel")
simkarte = Item("simkarte")
inventory = Bag()

# Inventar Grundlagen
@when("inventar")
@when("inventar benutzen")  # benutzen
@when("benutze inventar")
@when("inventar anschauen")  # anschauen
@when("anschauen inventar")
@when("öffne inventar")  # öffnen
@when("inventar öffnen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f"* {item}")

### Smartphone Grundlagen
@when("smartphone")
@when("anschauen smartphone")
@when("smartphone anschauen")
def zeige_smartphone():
    print("Die ist dein Smartphone")

@when("smartphone benutzen")
@when("benutzen smartphone")
@when("benutze smartphone")
def benutze_smartphone():
    if (room_number == 1):
        print("Du hast keinen Empfang, aber die Kamera funktioniert noch")
    else:
        print("Du versuchst deine bessere Hälfte anzurufen, um sie vor der Kernschmelze zu warnen. Aber du erreichst nur die Mailbox")

@when("smartphone öffnen")
@when("öffnen smartphone")
@when("öffne smartphone")
def oeffne_smartphone():
    if (sicherheitstuer_offen == False):
        print("Du kannst das Smartphone nicht öffnen")

@when("nimm smartphone")
@when("nehmen smartphone")
@when("smartphone nehmen")
def nehme_smartphone():
    print("Das Smartphone befindet sich schon in deinem Inventar")

@when("smartphone verwenden")
@when("verwenden smartphone")
@when("verwende smartphone")
def verwende_smartphone():
    print("Womit möchtest du das Smartphone verwenden")
    print("zB verwende Smartphone mit dir")

@when("selfie")
@when("verwende mit smartphone dir")
@when("verwende smartphone mit dir")
def verwende_smartphone_mit_dir():
    print("Du machst ein Selfie von dir")




### Räume ###
#aktuell von mir unbenutzt, kann das weg???
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

# Look Around #
@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
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
        

### Gegenstände Raum 1 ###

#Poster anschauen nehmen benutzen öffnen, kein verwende mit

@when("anschauen poster", context="room1")
@when("poster", context="room1")
@when("schaue poster an", context="room1")
def zeige_poster():
    say("""Das Poster trägt die Aufschrift „How much is the fish“. Es scheint mit Klebestreifen befestigt worden zu sein. Von der Rückseite schimmert Schrift durch das dünne Papier.""")

@when("poster nehmen", context="room1")
@when("nimm poster", context="room1")
@when("nehme poster", context="room1")
@when("nehmen poster", context="room1")
def nehme_poster():
    say("""Es ist mit Klebestreifen an der Wand befestigt. Die oberen Klebenstreifen haften zu stark und du möchstest es nicht zerstören. Du kannst aber einen Blick auf die Rückseite erhaschen. Du findest eine Widmung an Herrn Solar mit der Unterschrift von HP Baxxter und einer kurzen Biografie des Künstlers unter anderem mit seinem Geburtsdatum:""")
    say("""16. März 1964""")
    #zur erhöhung des Schwierigkeitsgrades, noch weitere Daten einbauen: siehe Confluence

@when("poster öffnen", context="room1")
@when("öffne poster", context="room1")
def oeffne_poster():
    print("Du kannst das Poster nicht öffnen!")

@when("poster benutzen", context="room1")
@when("benutze poster", context="room1")
def benutze_poster():
    print("Du kannst das Poster nicht benutzen!")

#Sicherheitsausrüstung anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue sicherheitsausrüstung an", context="room1")
@when("sicherheitsausrüstung", context="room1")
@when("anschauen sicherheitsausrüstung", context="room1")
def zeige_sicherheitsausruestung():
    global check_sicherheitsausruestung
    check_sicherheitsausruestung = True
    if inventory.find("brecheisen") is None:
        say("""Du durchsuchst die Sicherheitsausrüstung am Ende des Raumes. Dabei findest du ein Brecheisen.""")
    else:
        say("""Du durchsuchst die Sicherheitsausrüstung am Ende des Raumes. Dabei findest nichts brauchbares.""")

@when("sicherheitsausrüstung nehmen", context="room1")
@when("nimm sicherheitsausrüstung", context="room1")
@when("nehme sicherheitsausrüstung", context="room1")
@when("nehmen sicherheitsausrüstung", context="room1")
def nehme_sicherheitsausruestung():
    global check_sicherheitsausruestung
    if (check_sicherheitsausruestung == True and inventory.find("brecheisen") is None):
        nehme_brecheisen()
    else:
        print("Du kannst die Sicherheitsausrüstung nicht nehmen")

@when("sicherheitsausrüstung benutzen", context="room1")
@when("benutze sicherheitsausrüstung", context="room1")
def benutze_sicherheitsausruestung():
    print("Du kannst die Sicherheitsausrüstung nicht benutzen!")

@when("sicherheitsausrüstung öffnen", context="room1")
@when("öffne sicherheitsausrüstung", context="room1")
def oeffne_sicherheitsausruestung():
    print("Du kannst die Sicherheitsausrüstung nicht öffnen!")

#Brecheisen Inventar anschauen nehmen benutzen öffnen, noch kein verwende mit (kommt später)

@when("schaue brecheisen an")
@when("brecheisen")
@when("anschauen brecheisen")
def zeige_brecheisen():
    global check_sicherheitsausruestung
    global room_number
    if ((check_sicherheitsausruestung == True and room_number == 1) or inventory.find("brecheisen") is not None):
        print("Dies ist ein Brecheisen")
    else:
        print("Welches Brecheisen?")

@when("brecheisen nehmen", context="room1")
@when("nimm brecheisen", context="room1")
@when("nehme brecheisen", context="room1")
@when("nehmen brecheisen", context="room1")
def nehme_brecheisen():
    global check_sicherheitsausruestung
    if (inventory.find("brecheisen") is not None):
        print("Das Brecheisen befindet sich schon in deinem Inventar")
    elif (check_sicherheitsausruestung == True):
        inventory.add(brecheisen)
        say("""„Das könnte eventuell noch nützlich sein“, sagst du und packst das Brecheisen direkt ein.""")
        say("""Jetzt fühlst du dich wie Gordon Freeman""")
    else:
        print("Welches Brecheisen?")

@when("brecheisen benutzen")
@when("benutze brecheisen")
def benutze_brecheisen():
    global brecheisen_schienbein
    if (inventory.find("brecheisen") is not None):
        if (brecheisen_schienbein == False):
            say("""Aus Wut möchtest du etwas kaputt machen. Du suchst nach dem nächst besten Gegenstand und holst mit dem Brecheisen aus. Dabei verlierst du das Gleichgewicht und haust dir das Brecheisen gegen das Schienbein.""")
            say("""AUA""")
            say("""Du bist wohl doch kein Gordon Freeman ;-)""")
            brecheisen_schienbein = True
        else:
            print("Dein Schienbein schmerzt immer noch")
    else:
        print("Du hast kein Brecheisen in deinem Inventar")

@when("brecheisen öffnen")
@when("öffne brecheisen")
def oeffne_brecheisen():
    print("Du kannst das Brecheisen nicht öffnen!")


### Ende der Raume ### nun nur noch Debug und der Start-Aufruf

# Debug #


@when("debugraum")
def debug():
    global room_number
    print("RAUMNAMEN GENAU EINGEBEN!")
    print("1,2,3,4,5,6")
    debug_input = input("In welchen Raum springen? ")
    if debug_input == "1":
        set_context("room1")
        room_number = 1
    elif debug_input == "2":
        room_number = 2
        set_context("room2")
    elif debug_input == "3":
        room_number = 3
        set_context("room3")
    elif debug_input == "4":
        room_number = 5
        set_context("room4")
    elif debug_input == "5":
        room_number = 5
        set_context("room5")
    elif debug_input == "6":
        room_number = 6
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

### Startumgebung festlegen ###
inventory.add(smartphone)
set_context("room1")
room_number = 1

start()
# start(help = False) um den Help Befehl auszuschalten




