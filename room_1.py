########################
# RAUM 1: KONTROLLRAUM #
########################

# imports
from termcolor import colored
import time
from adventurelib import when, say, set_context
import room_2
from inventory import *

# global vars
kontrollrechner_neugestartet = False
sicherheitsausruestung_gesehen = False
sicherheitstuer_gesehen = False

#Überleitung Room1 und Instructions
def ueberleitung_room1():
    say(
        colored(
            """----------------------------------------------------------------------------------""",
            "yellow"
        )
    )
    time.sleep(1.0)
    say(
        colored(
            """Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und
            Knöpfen erschlägt dich fast und es fällt dir schwer deine Panik in den Griff zu
            bekommen. Du versuchst dich zu sammeln und deine Möglichkeiten abzuwägen: \n
            Du kannst dich im Raum [umschauen]\n
            Du kannst Dinge im Raum [anschauen], [nehmen] und [benutzen], sowie Knöpfe [drücken] oder Türen [öffnen], etc.\n
            Du kannst dein aktuelles [Inventar] anschauen\n
            Du kannst dir [hilfe] suchen, wenn du nicht weiterkommst\n
            Du kannst mit [quit] das AKW verlassen (Spiel beenden)\n
            Das Symbol [...] bedeutet, dass du Enter drücken sollst, um fortzufahren""",
            "yellow"
        )
    )


# Look Around #
@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
@when("umsehen", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    # TODO
    if room_2.zurueckgegangen:
        say(colored("""Du siehst die Tasche mit Sicherheitsausrüstung in der Ecke liegen.""", "yellow"))
    elif (kontrollrechner_neugestartet and sicherheitstuer_gesehen):
        say(colored("""Dir fällt ein auffälliges Poster ins Auge, welches an der Wand gegenüber des Kontrollrechners hängt.""", "yellow"))

    elif (kontrollrechner_neugestartet):
        say(colored("""Du blickst auf die riesige, meterdicke Sicherheitstür.""", "yellow"))

    elif (sicherheitsausruestung_gesehen):
        say(colored("""Du siehst den Kontrollrechner.""", "yellow"))

    else:
        say(colored("""Du siehst den Kontrollrechner und entdeckst eine Tasche mit Sicherheitsausrüstung in der Ecke.""", "yellow"))


@when("sicherheitsausrüstung anschauen", context="room1")
@when("ausrüstung anschauen", context="room1")
def sicherheitsausruestung_anschauen():
    if inventory.find("brecheisen") is None:
        global sicherheitsausruestung_gesehen
        sicherheitsausruestung_gesehen = True
        say(colored("""In der Sicherheitsausrüstung findest du ein Brecheisen.""", "yellow"))
    else:
        say(colored("""Du hast die Sicherheitsausrüstung bereits durchsucht""", "yellow"))


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
    if sicherheitsausruestung_gesehen:
        if inventory.find("brecheisen") is None:
            say(colored("""„Das könnte eventuell noch nützlich sein“, sagst du und packst das Brecheisen direkt ein.""", "yellow"))
            inventory.add(crowbar)
        else:
            say(colored("""Du hast das Brecheisen schon genommen.""", "yellow"))
    else:
        say(colored("""Du solltest dich zuerst noch ein wenig umsehen.""", "yellow"))


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
        say(colored("""Du hast kein Brecheisen.""", "yellow"))
    else:
        say(
            colored(
                """Vielleicht solltest du den Kontrollrechner damit lieber nicht
                zerstören...""",
                "yellow"
            )
        )


@when("kontrollrechner anschauen", context="room1")
@when("rechner anschauen", context="room1")
@when("pc anschauen", context="room1")
@when("kontrollpc anschauen", context="room1")
@when("kontrollrechner benutzen", context="room1")
@when("rechner benutzen", context="room1")
@when("pc benutzen", context="room1")
@when("kontrollrechner verwenden", context="room1")
def kontrollrechner_anschauen():
    say(
        colored(
            """Der Bildschirm zeigt weiterhin den Totenkopf und die Nachricht der
            Erpresser. Du entdeckst ein Terminal mit Anschlüssen und einigen Knöpfen.
            Darunter ein Knopf auf dem "Reset" steht und eine Buchse, die mit
            "DIN AT" beschriftet ist.""",
            "yellow"
        )
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
        colored(
            """Der Rechner startet neu, BIOS-Meldungen erscheinen auf dem Bildschirm,
            ein Windows 95 – Startsound ertönt und die Erpresserbotschaft erscheint
            direkt wieder nach dem Bootvorgang.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """„Das bringt nichts!“, denkst du dir und überlegst, was du tun sollst.
            Über den Kontrollrechner lassen sich die Pumpen für das Kühlsystem
            jedenfalls nicht mehr starten. Vielleicht hilft ein manueller Start der
            Pumpen. „Doch wie komme ich dorthin?“""",
            "yellow"
        )
    )
    global kontrollrechner_neugestartet
    kontrollrechner_neugestartet = True


@when("din at buchse anschauen", context="room1")
@when("buchse anschauen", context="room1")
@when("anschluss anschauen", context="room1")
def buchse_anschauen():
    say(
        colored(
            """So etwas Veraltetes, fast schon Antikes hast du schon lange nicht
            mehr gesehen. Leider hast du kein Eingabegerät zur Hand, das kompatibel
            ist.""",
            "yellow"
        )
    )


@when("sicherheitstür anschauen", context="room1")
@when("tür anschauen", context="room1")
@when("sicherheitstuer anschauen", context="room1")
@when("sicherheitstür öffnen", context="room1")
def sicherheitstuer_anschauen():
    if kontrollrechner_neugestartet:
        say(
            colored(
                """Du rüttelst an der Tür, doch sie bewegt sich keinen Zentimeter. Direkt neben der Tür befindet sich ein Tastenfeld
                und darüber eine Kamera. Du drückst die Grüne Starttaste und die Kamera beginnt mit einem Scan von deinem Gesicht. Du
                erschrickst. Auf dem Display erscheint in roter Schrift „Zugriff verweigert“.""",
                "yellow"
            )
        )
        say("""""")
        input(colored("[...]", "yellow"))
        say("""""")
        say(
            colored(
                """„Das Gesicht des Chefs sollte
                funktionieren!“, denkst du dir, erinnerst dich aber, dass dieser ohnmächtig geworden ist. Du nimmst dein Smartphone in
                die Hand und hältst ein Bild von Herrn Solar in die Kamera. „Guten Tag Herr Solar! Bitte geben Sie Ihre PIN ein!“,
                ertönt eine roboterartige Stimme aus dem Terminal und das Display zeigt: * * * * * *. „Mist, wo krieg ich denn jetzt den
                Zugangscode her?“, fragst du dich. Vielleicht schaust du dich einfach noch einmal um.""",
                "yellow"
            )
        )
        global sicherheitstuer_gesehen
        sicherheitstuer_gesehen = True
    else:
        say(
            colored(
                """Die Tür scheint verschlossen zu sein. Vielleicht versuchst du
                dein Glück erst mal am Kontrollrechner.""",
                "yellow"
            )
        )


@when("poster anschauen", context="room1")
@when("scooter poster anschauen", context="room1")
@when("scooter poster anschauen", context="room1")
@when("poster ansehen", context="room1")
def poster_anschauen():
    say(
        colored(
            """Das Poster trägt die Aufschrift „How much is the fish“. Es scheint
            mit Klebestreifen befestigt worden zu sein. Von der Rückseite schimmert
            Schrift durch das dünne Papier. Du hebst das Poster an und entdeckst
            eine Widmung an Herrn Solar mit der Unterschrift von HP Baxxter und
            einer kurzen Biografie des Künstlers unter anderem mit seinem
            Geburtsdatum: 16. März 1964""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Du erinnerst dich: Einer aus dem Kamerateam hat dir im Vorfeld erzählt,
            dass Herr Solar ein riesen Fan der Techno- und EDM-Band sei und immer
            wieder davon erzählte, dass er nur 5 Tage nach HP Baxxter Geburtstag hätte.""",
            "yellow"
        )
    )


@when("pin eingeben", context="room1")
@when("tür öffnen", context="room1")
@when("code eingeben", context="room1")
@when("zahl eingeben", context="room1")
@when("zugangscode eingeben", context="room1")
def pin_eingeben():
    while True:
        input_1 = input(
            colored("PIN eingeben ([exit] um abzubrechen): ", "grey", "on_green"))
        if (input_1 == "210364"):
            say(colored("""PIN wird überprüft...""", "grey", "on_green"))
            say("""""")
            time.sleep(3.0)
            say(colored("""PIN korrekt!""", "grey", "on_green"))
            say(colored("""Zugriff gewährt!""", "grey", "on_green"))
            time.sleep(2.0)
            room_2.ueberleitung_room2()
            return
        elif (input_1 == "exit"):
            return
        else:
            say(colored("""PIN wird überprüft...""", "grey", "on_green"))
            say("""""")
            time.sleep(3.0)
            say(colored("""PIN falsch!""", "red", "on_green"))
            say(colored("""Zugriff verweigert!""", "red", "on_green"))
            say("""""")


@when("zurück gehen", context="room1")
@when("zurück in maschinenraum gehen", context="room1")
@when("in maschinenraum gehen", context="room1")
@when("zu maschinenraum gehen", context="room1")
@when("maschinenraum betreten", context="room1")
@when("gehe zurück", context="room1")
@when("gehe zurück in maschinenraum", context="room1")
def go_room2():
    if room_2.zurueckgegangen:
        say(
            colored(
                """Du bist zurück gegangen und befindest dich wieder im Maschinenraum.""",
                "yellow"
            )
        )
        set_context("room2")
    else:
        say(
            colored(
                """Du hast keine Chance den Raum zu verlassen. Alle Türen sind verschlossen!""",
                "yellow"
            )
        )

@when("hilfe", context="room1")
@when("help", context="room1")
def help_room1():
    say(
        colored(
            """In diesem Raum ist leider keine Hilfe verfügbar. Schau dich einfach
            weiter um und die Hinweise werden dir den Weg zeigen.""",
            "yellow"
        )
    )
