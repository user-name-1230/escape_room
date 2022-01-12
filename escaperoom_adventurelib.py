#!/usr/bin/env python3

from adventurelib import start, when, Room, say, set_context
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
        # umschauen in Raum 3
        say("""Du stehst in einem langen Flur mit 7 Türen.
        Auf jeder Tür ist ein Symbol: \n
        - Welle \n
        - Stern \n
        - Plus \n
        - Fünfeck \n
        - Dach \n
        - Minus \n
        - Dreieck \n
        Einige Türen scheinen verschlossen zu sein, aber alle durchzuprobieren kostet zu viel Zeit.\n
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
            say("""Du nimmst das Brecheisen. Es ist schwer.""")
            # Falls wir noch mehr Dinge benutzen wollen, sollten wir uns
            # nicht mehr nur auf Raumattribute verlassen,
            # sondern die Items in einem Inventar speichern
        else:
            say("""Du hast das Brecheisen schon genommen.""")


@when("brecheisen benutzen")
def brecheisen_benutzen():
    if current_room == room1:
        if not current_room.has_crowbar:
            say("""Vielleicht solltest du den Kontrollrechner lieber nicht zerstören...""")
            current_room.action_counter += 1
            if current_room.action_counter == 2:
                ueberleitung_room2()
        else:
            say("""Du müssen das Brecheisen zuerst von der Wand nehmen.""")


@when("computer neustarten")
@when("rechner neustarten")
@when("computer rebooten")
@when("rechner rebooten")
def computer_neustarten():
    if current_room == room1:
        say("""Du startest den Kontrollrechner neu.
            Der Bildschirm wird schwarz, nach einiger Zeit taucht der Totenkopf wieder auf.
            Das hat leider nichts gebracht.""")


@when("tasten drücken")
@when("drücke tasten")
def tasten_druecken():
    if current_room == room1:
        say("""Du versuchst verschiedenste Tastenkombinationen, doch der Totenkopf bleibt.
            Selbst Strg+Alt+Entf hilft nicht weiter. """)
        current_room.action_counter += 1
        if current_room.action_counter == 2:
            ueberleitung_room2()


def ueberleitung_room2():
    say("""Überleitung zu Raum 2""")
    global current_room
    current_room = room2
    set_context(room2)


@when("debug")
def debug():
    say(str(room1))
    say(str(room1.has_crowbar))


################
# RAUM 3: FLUR #
################

@when("pinnwand anschauen", context=room3)
@when("schaue pinnwand an", context=room3)
def pinnwand_anschauen():
    say("""Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten""")
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


@when("türen anschauen", context=room3)
@when("tür anschauen", context=room3)
@when("schaue tür an", context=room3)
@when("schaue türen an", context=room3)
def tuer_anschauen():
    say("""Einige Türen scheinen verschlossen zu sein. Keine Zeit zu verlieren, du musst die richtige finden!""")


# @when("öffne tür mit welle")
# @when("öffne tür mit stern")
# @when("öffne tür mit plus")
# @when("öffne tür mit fünfeck")
# @when("öffne tür mit dach")
# @when("öffne tür mit minus")
# @when("öffne tür mit dreieck")
@when("öffne tür mit FORM", context=room3)
@when("tür mit FORM öffnen", context=room3)
def tuer_oeffnen(form):
    if form not in ("welle", "stern", "plus", "fünfeck", "dach", "minus", "dreieck"):
        say("""Eine Tür mit diesem Symbol gibt es nicht.""")
    if form == "stern":
        say(f"""Du versuchst, die Tür mit der {form} zu öffnen."
        Die Tür lässt sich öffnen. Es scheint die richtige Tür zu sein!""")
    else:
        # Doppelt gemoppelt, damit die Deklination passt
        say(f"""Du versuchst, die Tür mit dem {form} zu öffnen.
        Diese Tür scheint verschlossen zu sein. Du verlierst Zeit!""")
        # TODO verschlossene Türen und leere Räume


@when("öffne tür", context=room3)
@when("tür öffnen", context=room3)
def tuer_oeffnen_unklar():
    say("""Ich weiß nicht, welche Tür du meinst""")


start()
