#!/usr/bin/env python3

from adventurelib import start, when, Room, say
# import pyqrcode
from PIL import Image
import sys


room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room1.has_crowbar = True
room1.action_counter = 0

current_room = room3  # Startraum


@when("umschauen")
@when("schaue um")
@when("schau dich um")
def look_around():
    global current_room
    if current_room == room1:
        # umschauen in Raum 1
        if current_room.has_crowbar:
            say("""Hier ist eine Beschreibung des Kontrollraums mit hängendem Brecheisen""")
        else:
            say("""Hier ist eine Beschreibung des Kontrollraums ohne hängendem Brecheisen""")
    elif current_room == room3:
        say("""Sie stehen in einem langen Flur mit 7 Türen.
        Auf jeder Tür ist ein Symbol: \n
        - Welle \n
        - Stern \n
        - Plus \n
        - Fünfeck \n
        - Dach \n
        - Minus \n
        - Dreieck \n
        An einer Pinnwand hängen Fotos von einem Firmenausflug.
        """)

########################
# RAUM 1: KONTROLLRAUM #
########################


@when("brecheisen nehmen")
def brecheisen_nehmen():
    # Brecheisen in Raum 1 nehmen
    global current_room
    if current_room == room1:
        if current_room.has_crowbar:
            current_room.has_crowbar = False
            say("""Sie nehmen das Brecheisen. Es ist schwer.""")
            # Falls wir noch mehr Dinge benutzen wollen, sollten wir uns
            # nicht mehr nur auf Raumattribute verlassen,
            # sondern die Items in einem Inventar speichern
        else:
            say("""Sie haben das Brecheisen schon genommen.""")


@when("brecheisen benutzen")
def brecheisen_benutzen():
    if current_room == room1:
        if not current_room.has_crowbar:
            say("""Vielleicht sollten Sie den Kontrollrechner lieber nicht zerstören...""")
            current_room.action_counter += 1
            if current_room.action_counter == 2:
                ueberleitung_room2()
        else:
            say("""Sie müssen das Brecheisen zuerst von der Wand nehmen.""")


@when("computer neustarten")
@when("rechner neustarten")
@when("computer rebooten")
@when("rechner rebooten")
def computer_neustarten():
    if current_room == room1:
        say("""Sie starten den Kontrollrechner neu.
            Der Bildschirm wird schwarz, nach einiger Zeit taucht der Totenkopf wieder auf.
            Das hat leider nichts gebracht.""")


@when("tasten drücken")
def tasten_druecken():
    if current_room == room1:
        say("""Sie versuchen verschiedenste Tastenkombinationen, doch der Totenkopf bleibt.
            Selbst Strg+Alt+Entf hilft nicht weiter. """)
        current_room.action_counter += 1
        if current_room.action_counter == 2:
            ueberleitung_room2()


def ueberleitung_room2():
    say("""Überleitung zu Raum 2""")
    global current_room
    current_room = room2


@when("debug")
def debug():
    say(str(room1))
    say(str(room1.has_crowbar))


################
# RAUM 3: FLUR #
################

@when("pinnwand anschauen")
def pinnwand_anschauen():
    say("""Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten""")
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


start()
