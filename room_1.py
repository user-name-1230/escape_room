########################
# RAUM 1: KONTROLLRAUM #
########################

#imports
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import adventurelib
import sys
from room_2 import *
from inventory import *

#global vars
kontrollrechner_neugestartet = False
sicherheitsausruestung_gesehen = False
sicherheitstuer_gesehen = False


def ueberleitung_room1():
    say(
        """----------------------------------------------------------------------------------"""
    )
    say(
        """Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und
    Knöpfen erschlägt dich fast und es fällt dir schwer deine Panik in den Griff zu
    bekommen. Du versuchst dich zu sammeln und deine Möglichkeiten abzuwägen: \n
    Du kannst dich im Raum [umschauen]\n
    Du kannst Dinge im Raum [anschauen], [nehmen] und [benutzen], sowie Knöpfe [drücken]\n
    Du kannst dein aktuelles [Inventar] anschauen\n
    Du kannst dir [help] suchen, wenn du nicht weiterkommst\n
    Du kannst mit [quit] das AKW verlassen (Spiel beenden)"""
    )


# Look Around #
@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    # TODO
    if (sicherheitsausruestung_gesehen and kontrollrechner_neugestartet and sicherheitstuer_gesehen):
        say("""Du entdeckst ein Scooter-Poster an der Wand.""")

    elif (sicherheitsausruestung_gesehen and kontrollrechner_neugestartet):
        say("""Du entdeckst die riesige, meterdicke Sicherheitstür.""")

    elif (sicherheitsausruestung_gesehen):
        say("""Du siehst den Kontrollrechner.""")

    else:
        say("""Du siehst den Kontrollrechner und Sicherheitsausrüstung in der Ecke.""")


@when("sicherheitsausrüstung anschauen", context="room1")
@when("ausrüstung anschauen", context="room1")
def sicherheitsausruestung_anschauen():
    if inventory.find("brecheisen") is None:
        global sicherheitsausruestung_gesehen
        sicherheitsausruestung_gesehen = True
        say("""In der Sicherheitsausrüstung findest du ein Brecheisen.""")
    else:
        say("""Du hast die Sicherheitsausrüstung bereits durchsucht""")



@when("das brecheisen nehmen", context="room1")  # brecheisen, nehmen
@when("brecheisen nehmen", context="room1")
@when("nehm brecheisen", context="room1")
@when("nehm das brecheisen", context="room1")
@when("nimm brecheisen", context="room1")  # brecheisen, nimm
@when("nimm das brecheisen", context="room1")
@when("die brechstange nehmen", context="room1")  # brechstange, nehmen
@when("brechstange nehmen", context="room1")
@when("nehm brechstange", context="room1")
@when("nehm die brechstange", context="room1")
@when("nimm die brechstange", context="room1")  # brechstange, nimm
@when("nimm brechstange", context="room1")
def brecheisen_nehmen():
    # Brecheisen in Raum 1 nehmen
    if sicherheitsausruestung_gesehen == True:
        if "brecheisen" not in inventory:
            say("""„Das könnte eventuell noch nützlich sein“, sagst du und packst das Brecheisen direkt ein.""")
            inventory.add(crowbar)
        else:
            say("""Du hast das Brecheisen schon genommen.""")
    else:
        say("""Du solltest dich zuerst noch ein wenig umsehen.""")


@when("benutze brecheisen", context="room1")  # brecheisen, benutzen
@when("benutz brecheisen", context="room1")
@when("brecheisen benutzen", context="room1")
@when("nutze brecheisen", context="room1")  # brecheisen, nutzen
@when("nutz brecheisen", context="room1")
@when("brecheisen nutzen", context="room1")
@when("nutze brechstange", context="room1")  # brechstange, benutzen
@when("nutz brechstange", context="room1")
@when("benutze brechstange", context="room1")
@when("benutz brechstange", context="room1")
@when("brechstange benutzen", context="room1")  # brechstange, nutzen
@when("brechstange nutzen", context="room1")
def brecheisen_benutzen():
    if inventory.find("brecheisen") is None:
        say("Du hast kein Brecheisen.")
    else:
        say(
            """Vielleicht solltest du den Kontrollrechner damit lieber nicht
            zerstören..."""
        )



@when("kontrollrechner anschauen", context="room1")
def kontrollrechner_anschauen():
    say(
        """Der Bildschirm zeigt weiterhin den Totenkopf und die Nachricht der
        Erpresser. Du entdeckst ein Terminal mit Anschlüssen und einigen Knöpfen.
        Darunter ein Knopf auf dem "Reset" steht und eine Buchse, die mit
        "DIN AT" beschriftet ist."""
    )



@when("reset drücken", context="room1")
@when("knopf drücken", context="room1")
@when("computer neustarten", context="room1")  # neustarten
@when("starte computer neu", context="room1")
@when("rechner neustarten", context="room1")
@when("starte rechner neu", context="room1")
@when("pc neustarten", context="room1")
@when("starte pc neu", context="room1")
@when("kontrollrechner neustarten", context="room1")
@when("starte kontrollrechner neu", context="room1")
@when("system neustarten", context="room1")
@when("starte system neu", context="room1")
@when("computer rebooten", context="room1")  # rebooten
@when("reboote computer", context="room1")
@when("rechner rebooten", context="room1")
@when("reboote rechner", context="room1")
@when("system rebooten", context="room1")
@when("reboote system", context="room1")
@when("pc rebooten", context="room1")
@when("reboote pc", context="room1")
@when("kontrollrechner rebooten", context="room1")
@when("reboote kontrollrechner", context="room1")
def computer_neustarten():
    say(
        """Der Rechner startet neu, BIOS-Meldungen erscheinen auf dem Bildschirm,
        ein Windows 95 – Startsound ertönt und die Erpresserbotschaft erscheint
        direkt wieder nach dem Bootvorgang.\n
        „Das bringt nichts!“, denkst du dir und überlegst, was du tun sollst.
        Über den Kontrollrechner lassen sich die Pumpen für das Kühlsystem
        jedenfalls nicht mehr starten. Vielleicht hilft ein manueller Start der
        Pumpen."""
    )
    global kontrollrechner_neugestartet
    kontrollrechner_neugestartet = True


@when("din at buchse anschauen", context="room1")
@when("buchse anschauen", context="room1")
@when("anschluss anschauen", context="room1")
def buchse_anschauen():
    say("""So etwas Veraltetes, fast schon Antikes hast du schon lange nicht
        mehr gesehen. Leider hast du kein Eingabegerät zur Hand, das kompatibel
        ist.""")



@when("sicherheitstür anschauen", context="room1")
@when("tür anschauen", context="room1")
@when("sicherheitstuer anschauen", context="room1")
def sicherheitstuer_anschauen():
    if kontrollrechner_neugestartet:
        say(
            """Du rüttelst an der Tür, doch sie bewegt sich keinen Zentimeter. Direkt neben der Tür befindet sich ein Tastenfeld
    	    und darüber eine Kamera. Du drückst die Grüne Starttaste und die Kamera beginnt mit einem Scan von deinem Gesicht. Du
    	    erschrickst. Auf dem Display erscheint in roter Schrift „Zugriff verweigert“. „Das Gesicht des Chefs sollte
    	    funktionieren!“, denkst du dir, erinnerst dich aber, dass dieser ohnmächtig geworden ist. Du nimmst dein Smartphone in
    	    die Hand und hältst ein Bild von Herrn Solar in die Kamera. „Guten Tag Herr Solar! Bitte geben Sie Ihre PIN ein!“,
    	    ertönt eine roboterartige Stimme aus dem Terminal und das Display zeigt: * * * * * *. „Mist, wo krieg ich denn jetzt den
    	    PIN her?“, fragst du dich. Vielleicht schaust du dich einfach noch einmal um."""
        )
        global sicherheitstuer_gesehen
        sicherheitstuer_gesehen = True
    else:
        say("""Die Tür scheint verschlossen zu sein. Vielleicht versuchst du
            dein Glück erst mal am Kontrollrechner.""")


@when("poster anschauen", context="room1")
@when("scooter poster anschauen", context="room1")
@when("scooter poster anschauen", context="room1")
@when("poster ansehen", context="room1")
def poster_anschauen():
    say("""Das Poster trägt die Aufschrift „How much is the fish“. Es scheint
        mit Klebestreifen befestigt worden zu sein. Von der Rückseite schimmert
        Schrift durch das dünne Papier. Du hebst das Poster an und entdeckst
        eine Widmung an Herrn Solar mit der Unterschrift von HP Baxxter und
        einer kurzen Biografie des Künstlers unter anderem mit seinem
        Geburtsdatum: 16. März 1964\n
        Du erinnerst dich: Einer aus dem Kamerateam hat dir im Vorfeld erzählt,
        dass Herr Solar ein riesen Fan der Techno- und EDM-Band sei und immer
        wieder davon erzählte, dass er nur 5 Tage nach HP Baxxter Geburtstag hätte.""")


@when("pin eingeben", context="room1")
@when("tür öffnen", context="room1")
@when("code eingeben", context="room1")
@when("zahl eingeben", context="room1")
def pin_eingeben():
    while True:
        input_1 = input("PIN eingeben ([exit] um abzubrechen): ")
        if (input_1 == "210364"):
            say("""PIN wird überprüft...\n
                """)
            time.sleep(3.0)
            say("""PIN korrekt!\n
                Zugriff gewährt!""")
            time.sleep(2.0)
            ueberleitung_room2()
            return
        elif (input_1 == "exit"):
            return
        else:
            say("""PIN wird überprüft...\n
                """)
            time.sleep(3.0)
            say("""PIN falsch!\n
                Zugriff verweigert!""")
