#####################
# RAUM 4: LAGERRAUM #
#####################

#imports
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import adventurelib
import sys
from room_1 import *
from room_2 import *
from room_3 import *
from room_5 import *
from room_6 import *

#global vars
can_check_sim_slot = False
sim_schrank_offen = False
can_use_pin = False


def ueberleitung_room4():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Du scheinst in eine Art Lagerraum gekommen zu sein mit allerlei
    technischen Geräten, die ihre beste Zeit hinter sich haben. In der Ecke
    steht ein leeres Serverrack und daneben eine Werkzeugtasche, die allerdings
    nur nutzlose Werkzeuge enthält. Mal sehen, was du noch so entdecken kannst,
    was dir weiterhelfen könnte."""
    )
    set_context("room4")


@when("umschauen", context="room4")
@when("schau um", context="room4")
@when("schau dich um", context="room4")
def look_around_room4():
    say(
        """An der gegenüberliegenden Wand des Serverracks steht ein Lagerspind mit einem Zahlenschloss, das anscheinend bei der
    letzten Benutzung nicht richtig verschlossen wurde."""
    )



@when("oberes abteil angucken", context="room4")  # angucken
@when("gucke oberes abteil an", context="room4")
@when("guck oberes abteil an", context="room4")
@when("abteil oben angucken", context="room4")
@when("oberes abteil anschauen", context="room4")  # anschauen
@when("schaue oberes abteil an", context="room4")
@when("schau oberes abteil an", context="room4")
@when("abteil oben anschauen", context="room4")
@when("abteil oben betrachten", context="room4")  # betrachten
@when("betrachte oberes abteil", context="room4")
def oberes_abteil():
    print("oberes abteil beschreibung")


@when("mittleres abteil angucken", context="room4")  # angucken
@when("gucke mittleres abteil an", context="room4")
@when("guck mittleres abteil an", context="room4")
@when("abteil mitte angucken", context="room4")
@when("abteil in der mitte angucken", context="room4")
@when("mittleres abteil anschauen", context="room4")  # anschauen
@when("schaue mittleres abteil an", context="room4")
@when("schau mittleres abteil an", context="room4")
@when("abteil mitte anschauen", context="room4")
@when("abteil in der mitte anschauen", context="room4")
@when("abteil mitte betrachten", context="room4")  # betrachten
@when("abteil in der mitte betrachten", context="room4")
@when("betrachte mittleres abteil", context="room4")
def mittleres_abteil():
    print("mittleres abteil beschreibung")


@when("unteres abteil angucken", context="room4")  # angucken
@when("gucke unteres abteil an", context="room4")
@when("abteil unten angucken", context="room4")
@when("unteres abteil anschauen", context="room4")  # anschauen
@when("schaue unteres abteil an", context="room4")
@when("abteil unten anschauen", context="room4")
@when("abteil unten betrachten", context="room4")  # betrachten
@when("betrachte unteres abteil", context="room4")
def unteres_abteil():
    print("unteres abteil beschreibung")


@when("rechner anmachen", context="room4")  # rechner, anmachen
@when("mache rechner an", context="room4")
@when("rechner starten", context="room4")  # rechner, starten
@when("starte rechner", context="room4")
@when("rechner anschalten", context="room4")  # rechner, anschalten
@when("schalte rechner an", context="room4")
@when("computer anmachen", context="room4")  # computer, anmachen
@when("mache computer an", context="room4")
@when("computer starten", context="room4")  # computer, starten
@when("starte computer", context="room4")
@when("computer anschalten", context="room4")  # computer, anschalten
@when("schalte computer an", context="room4")
@when("pc anmachen", context="room4")  # pc, anmachen
@when("mache pc an", context="room4")
@when("pc starten", context="room4")  # pc, starten
@when("starte pc", context="room4")
@when("pc anschalten", context="room4")  # pc, anschalten
@when("schalte pc an", context="room4")
def rechner_anmachen():
    print("schon betroffen")


@when("werkzeugkiste öffnen", context="room4")  # öffnen
@when("öffne werkzeugkiste", context="room4")
def werkzeugkiste_oeffnen():
    print("werkzeugkiste geöffnet, nichts drin")


@when("spind öffnen", context="room4")  # öffnen
@when("öffne spind", context="room4")
def spind_oeffnen():
    global sim_schrank_offen
    sim_schrank_offen = True
    say(
        """Du öffnest den Spind und schaust dir den Inhalt genau an. Zuerst siehst du nur alte Ersatzteile für Computer.
    RAM,Lüfter, Netzteile, alte Festplatten und so weiter. Doch dann sticht dir ein kleiner Karton mit der Aufschrift „SIM-Karten“
    ins Auge. \n
    An der Innenseite der Spindtür entdeckst du einen QR-Code. Ob der wohl was damit zu tun hat? """
    )


@when("sim karte nehmen", context="room4")  # nehmen
@when("sim nehmen", context="room4")
@when("nehme sim karte", context="room4")
@when("nehme sim", context="room4")
@when("nehme die sim karte", context="room4")
@when("nehme die sim", context="room4")
@when("nehm sim karte", context="room4")
@when("nehm sim", context="room4")
@when("nehm die sim karte", context="room4")
@when("nehm die sim", context="room4")
@when("nimm sim karte", context="room4")  # nimm
@when("nimm sim", context="room4")
@when("nimm die sim karte", context="room4")
@when("nimm die sim", context="room4")
def sim_karte_nehmen():
    if not sim_schrank_offen:
        print("nicht offen")
    if sim_schrank_offen:
        say(
            """Du nimmst dir eine Karte aus dem Karton. „Verdammt…wie soll ich denn jetzt den SIM-Slot an meinem Handy öffnen?“,
        fragst du dich.\n
        Du hörst schnelle Schritte auf dem Gang. Die Ministerin und das Fernsehteam betreten den Raum."""
        )
        inventory.add(sim)


@when("smartphone anschauen", context="room4")  # anschauen, smartphone
@when("schaue smartphone an", context="room4")
@when("schaue das smartphone an", context="room4")
@when("schau smartphone an", context="room4")
@when("schau das smartphone an", context="room4")
@when("handy anschauen", context="room4")  # anschauen, handy
@when("schaue handy an", context="room4")
@when("schaue das handy an", context="room4")
@when("schau handy an", context="room4")
@when("schau das handy an", context="room4")
@when("smartphone angucken", context="room4")  # angucken, smartphone
@when("gucke smartphone an", context="room4")
@when("gucke das smartphone an", context="room4")
@when("guck smartphone an", context="room4")
@when("guck das smartphone an", context="room4")
@when("handy angucken", context="room4")  # angucken, handy
@when("gucke handy an", context="room4")
@when("gucke das handy an", context="room4")
@when("guck handy an", context="room4")
@when("guck das handy an", context="room4")
def smartphone_anschauen():
    print("smartphone angeschaut")
    global can_check_sim_slot
    can_check_sim_slot = True


@when("sim schacht öffnen", context="room4")  # sim schacht, öffnen
@when("öffne sim schacht", context="room4")  # sim karten schacht, öffnen
@when("sim karten schacht öffnen", context="room4")
@when("öffne sim karten schacht", context="room4")
@when("sim slot öffnen", context="room4")  # sim slot, öffnen
@when("öffne sim slot", context="room4")
@when("sim karten slot öffnen", context="room4")  # sim karten slot, öffnen
@when("öffne sim karten slot", context="room4")
@when("sim tray öffnen", context="room4")  # sim tray, öffnen
@when("öffne sim tray", context="room4")
@when("sim karten tray öffnen", context="room4")  # sim karten tray, öffnen
@when("öffne sim karten tray", context="room4")
def sim_slot_oeffnen():
    if can_check_sim_slot:
        if inventory.find("simkarte") is not None:
            if inventory.find("haarnadel") is not None:
                say(
                    """Zum Glück ist die Nadel dünn genug, um den SIM-Slot zu öffnen. Du legst die SIM-Karte in dein Handy ein,
                worauf die Aufforderung „SIM-PIN eingeben“ angezeigt wird."""
                )
                global can_use_pin
                can_use_pin = True
            else:
                print("Kann nicht per Hand geöffnet werden")
        else:
            print("SIM Karte nicht im Inventar")
    else:
        print("du musst noch dein handy anschauen")


@when("schrader nach haarnadel fragen", context="room4")
@when("frage schrader nach haarnadel", context="room4")
def schrader_haarnadel():
    say(
        """Dir fällt sofort die feine Haarnadel der Ministerin ins Auge. Du fragst sie, ob du dir ihre Haarnadel kurz ausleihen
    kannst. Sie nickt aufgeregt und übergibt sie dir schnell."""
    )
    inventory.add(hairpin)


@when("qr code anzeigen", context="room4")  # qr code, anzeigen
@when("zeige qr code an", context="room4")
@when("zeig qr code an", context="room4")
@when("qr code anschauen", context="room4")  # qr code, anschauen
@when("schaue qr code an", context="room4")
@when("schau qr code an", context="room4")
@when("qrcode anzeigen", context="room4")  # qrcode, anzeigen
@when("zeige qrcode an", context="room4")
@when("zeig qrcode an", context="room4")
@when("qrcode anschauen", context="room4")  # qrcode, anschauen
@when("schaue qrcode an", context="room4")
@when("schau qrcode an", context="room4")
@when("qr anzeigen", context="room4")  # qr, anzeigen
@when("zeige qr an", context="room4")
@when("zeig qr an", context="room4")
@when("qr anschauen", context="room4")  # qr, anschauen
@when("schaue qr an", context="room4")
@when("schau qr an", context="room4")
def show_qr():
    img = Image.open("qr.png")
    img.show()


@when("pin eingeben", context="room4")  # eingeben
@when("eingabe pin", context="room4")
@when("eingabe vom pin", context="room4")
@when("pin bestaetigen", context="room4")  # bestätigen
@when("bestaetigen mit pin", context="room4")
@when("bestaetige mit pin", context="room4")
@when("nutze pin", context="room4")  # benutzen
@when("nutz pin", context="room4")
@when("nutze den pin", context="room4")
@when("nutz den pin", context="room4")
@when("benutze pin", context="room4")
@when("benutz pin", context="room4")
@when("benutze den pin", context="room4")
@when("benutz den pin", context="room4")
def pin_eingeben():
    if can_use_pin:
        say(
            """Sehr gut. Du hast es geschafft, die SIM-Karte zu entsperren. Auf deinem Smartphone-Display erscheint direkt das
            Dashboard der Intranet-Seite des Kraftwerks. In einer Liste am Rand werden alle Computer im Netzwerk angezeigt. Das sieht
            schlecht aus. Alle PCs sind mit einem Schloss-Symbol versehen. Das kann nichts Gutes bedeuten. Du scrollst durch die
            Liste. Doch was ist das? Kurz vor Ende der Liste ist tatsächlich noch ein PC aufgeführt, der noch nicht mit einem Schloss
            Symbol versehen ist. Das ist es! Du klickst darauf, um dir mehr Details ansehen zu können. Dabei steht sogar eine
            Raumnummer. „Ich kann Sie dort hinführen!“, sagt der Kraftwerkchef aufgeregt."""
        )
        hamming_code()
    else:
        print("SIM karte noch nicht hinzugefügt")


def hamming_code():
    while True:
        input_2 = input("PIN eingeben: ")
        if input_2 == "1234":
            print("PIN korrekt")
            raum4Ende()
            return
        else:
            print("Falscher PIN, bitte noch einmal versuchen.")


def raum4Ende():
    say("""Hier kommt eine Überleitung zu Raum 5""")
    # TODO
    set_context("room5")
