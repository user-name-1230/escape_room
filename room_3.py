################
# RAUM 3: FLUR #
################

#imports
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import adventurelib
import sys
from room_1 import *
from room_2 import *
from room_4 import *
from room_5 import *
from room_6 import *

tür_welle = Item("welle")  # 1
tür_welle.status = False
tür_stern = Item("stern")  # 2
tür_stern.status = False
tür_plus = Item("plus")  # 3
tür_plus.status = False
tür_fünfeck = Item("fünfeck")  # 4
tür_fünfeck.status = False
tür_dach = Item("dach")  # 5
tür_dach.status = False
tür_dreieck = Item("dreieck")  # 6
tür_dreieck.status = False
tür_minus = Item("minus")  # 7
tür_minus.status = False

türen = Bag(
    [tür_welle, tür_stern, tür_dach, tür_dreieck, tür_fünfeck, tür_minus, tür_plus]
)


def ueberleitung_room3():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Doch von dem lauten Geräusch scheint der Kraftwerk-Chef wieder
    aufgewacht zu sein. Er kommt schweren Schrittes auf dich zugelaufen und
    versucht dir winkend und mit letztem Atem keuchend mitzuteilen, dass die
    Pumpen nur über den Haupt-Kontrollrechner gestartet werden können.\n
    Du musst also unbedingt einen Weg finden, den Rechner zu entsperren. Doch wie
    sollst du das bloß anstellen? Vielleicht sind noch nicht alle Rechner mit
    der Ransomware infiziert. Du musst einen Rechner finden, der noch nicht
    betroffen ist, vielleicht hilft dir das weiter.\n Herr Solar scheint einen
    Gedankenblitz zu haben: „Wir haben neulich mit anderen Kraftwerken zusammen
    ein 5G-Campusnetz aufgebaut, das alle verfügbaren Geräte in unserem Netzwerk
    auflisten kann. Dazu braucht man nur eine passende SIM-Karte. Jedoch hab ich
    leider vergessen, wo genau die SIM-Karten gelagert werden. Es muss irgendwo
    hier drüben sein.“, sagt er und führt dich in einen langen, kargen Flur mit
    sieben Türen."""
    )
    set_context("room3")


@when("umschauen", context="room3")
@when("schaue um", context="room3")
@when("schau dich um", context="room3")
def look_around_room3():
    # umschauen in Raum 3
    say(
        """Du stehst in einem langen Flur mit 7 Türen.
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
        """
    )
    img = Image.open("doors.png")
    img.show()



@when("pinnwand anschauen", context="room3")  # anschauen
@when("schaue pinnwand an", context="room3")
@when("schau pinnwand an", context="room3")
@when("gucke pinnwand an", context="room3")  # gucken
@when("guck pinnwand an", context="room3")
@when("pinnwand angucken", context="room3")
@when("pinnwand betrachten", context="room3")  # betrachten
@when("betrachte pinnwand", context="room3")
def pinnwand_anschauen():
    say(
        """Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten"""
    )
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


@when("türen anschauen", context="room3")  # anschauen
@when("schaue türen an", context="room3")
@when("schau türen an", context="room3")
@when("tür anschauen", context="room3")
@when("schaue tür an", context="room3")
@when("schau tür an", context="room3")
@when("türen angucken", context="room3")  # angucken
@when("gucke türen an", context="room3")
@when("guck türen an", context="room3")
@when("tür angucken", context="room3")
@when("gucke tür an", context="room3")
@when("guck tür an", context="room3")
@when("tür betrachten", context="room3")  # betrachten
@when("betrachte tür", context="room3")
@when("türen betrachten", context="room3")
@when("betrachte türen ", context="room3")
def tuer_anschauen():
    say(
        """Einige Türen scheinen verschlossen zu sein. Keine Zeit zu verlieren, du musst die richtige finden!"""
    )


@when("öffne tür mit FORM", context="room3")  # öffnen
@when("öffne die tür mit FORM", context="room3")
@when("öffne tür mit FORM", context="room3")
@when("tür öffnen mit FORM", context="room3")
@when("tür mit FORM öffnen", context="room3")
def tuer_oeffnen(form):
    if türen.find(form) is None:
        say("""Eine Tür mit diesem Symbol gibt es nicht.""")
    elif form == "stern":
        türen.find("stern").status = True
        say(
            f"""Du versuchst, die Tür mit der {form} zu öffnen.\n
        Die Tür lässt sich öffnen. Es scheint die richtige Tür zu sein!"""
        )
    else:
        # Doppelt gemoppelt, damit die Deklination passt
        say(
            f"""Du versuchst, die Tür mit dem {form} zu öffnen.
        Diese Tür scheint verschlossen zu sein. Du verlierst Zeit!"""
        )
        # TODO verschlossene Türen und leere Räume


@when("öffne tür", context="room3")
@when("tür öffnen", context="room3")
def tuer_oeffnen_unklar():
    say("""Ich weiß nicht, welche Tür du meinst""")


@when("gehe in den raum", context="room3")  # gehe,raum
@when("gehe in raum", context="room3")
@when("in raum gehen", context="room3")
@when("in den raum gehen", context="room3")
@when("gehe durch tür", context="room3")  # gehe, tür
@when("gehe durch die tür", context="room3")
@when("durch tür gehen", context="room3")
@when("durch die tür gehen", context="room3")
@when("durch die tür hindurch gehen", context="room3")
@when("geh in den raum", context="room3")  # geh, raum
@when("geh in raum", context="room3")
@when("geh durch tür", context="room3")  # geh, tür
@when("geh durch die tür", context="room3")
@when("geh durch die tür hindurch", context="room3")
@when("raum betreten", context="room3")  # betreten, raum
@when("den raum betreten", context="room3")
@when("betrete raum", context="room3")  # betrete, raum
@when("betrete den raum", context="room3")
def gehe_in_lagerraum():
    # TODO: andere Türen machen
    if türen.find("stern").status:
        say("""Du betrittst den Raum hinter der soeben geöffneten Tür.""")
        ueberleitung_room4()
    else:
        say("""Die Tür ist noch geschlossen.""")
