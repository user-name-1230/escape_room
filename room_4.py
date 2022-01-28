#####################
# RAUM 4: LAGERRAUM #
#####################

# imports
from PIL import Image
import time
from adventurelib import when, say, set_context
import room_5
from inventory import *
from termcolor import colored


# global vars
sim_schrank_offen = False
sim_eingelegt = False
qr_gesehen = False


def ueberleitung_room4():
    time.sleep(1.0)
    say(
        colored(
            """---------------------------------------------------------------------------------""",
            "yellow",
        )
    )
    say(
        colored(
            """Du scheinst in eine Art Lagerraum gekommen zu sein mit allerlei
            technischen Geräten, die ihre beste Zeit hinter sich haben. In der Ecke
            steht ein leeres Serverrack und daneben eine Werkzeugtasche, die allerdings
            nur nutzlose Werkzeuge enthält. Mal sehen, was du noch so entdecken kannst,
            was dir weiterhelfen könnte.""",
            "yellow",
        )
    )
    set_context("room4")


@when("umschauen", context="room4")
@when("schau um", context="room4")
@when("schau dich um", context="room4")
@when("umsehen", context="room4")
def look_around_room4():
    if sim_eingelegt:
        say(
            colored(
                """An der Innenseite der Spindtür entdeckst du einen QR Code.
                Ob der wohl was damit zu tun hat?""",
                "yellow"
            )
        )
    elif "simkarte" in inventory:
        say(
            colored(
                """Dir fällt sofort die feine Haarnadel der Ministerin ins Auge.
                Du fragst sie, ob du dir ihre Haarnadel kurz ausleihen kannst.
                Sie nickt aufgeregt und übergibt sie dir schnell.""",
                "yellow",
            )
        )
        inventory.add(hairpin)
    else:
        say(
            colored(
                """An der gegenüberliegenden Wand des Serverracks steht ein
                Lagerspind mit einem Zahlenschloss, das anscheinend bei der letzten
                Benutzung nicht richtig verschlossen wurde.""",
                "yellow",
            )
        )



@when("spind öffnen", context="room4")  # öffnen
@when("öffne spind", context="room4")
@when("spind anschauen", context="room4")  # anschauen
@when("lagerspind öffnen", context="room4")  # öffnen
@when("öffne lagerspind", context="room4")
@when("lagerspind anschauen", context="room4")  # anschauen
def spind_oeffnen():
    global sim_schrank_offen
    sim_schrank_offen = True
    say(
        colored(
            """Du öffnest den Spind und schaust dir den Inhalt genau an.
            Zuerst siehst du nur alte Ersatzteile für Computer. RAM, Lüfter,
            Netzteile, alte Festplatten und so weiter. Doch dann sticht dir ein
            kleiner Karton mit der Aufschrift „SIM Karten“ ins Auge.""",
            "yellow",
        )
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
    if sim_schrank_offen:
        say(
            colored(
                """Du nimmst dir eine Karte aus dem Karton. „Verdammt...wie
                soll ich denn jetzt den SIM-Slot an meinem Handy öffnen?“, fragst du dich.\n
                Du hörst schnelle Schritte auf dem Gang. Die Ministerin und das
                Fernsehteam betreten den Raum.""",
                "yellow",
            )
        )
        inventory.add(sim)
    else:
        say(
            colored(
                """Ich weiß nicht, welche SIM Karte du meinst. Schau eventuell
                einmal im Spind nach.""",
                "red",
            )
        )




@when("haarnadel benutzen", context="room4")
@when("nadel benutzen", context="room4")
@when("sim karte einlegen", context="room4")
@when("sim einlegen", context="room4")
@when("karte einlegen", context="room4")
@when("sim benutzen", context="room4")
@when("sim karte benutzen", context="room4")
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
    if inventory.find("simkarte") is not None:
        if inventory.find("haarnadel") is not None:
            say(
                colored(
                    """Zum Glück ist die Nadel dünn genug, um den
                    SIM-Slot zu öffnen. Du legst die Karte in dein Handy ein,
                    worauf die Aufforderung „SIM PIN eingeben“ angezeigt wird.""",
                    "yellow",
                )
            )
            global sim_eingelegt
            sim_eingelegt = True
        else:
            say(colored("""Tut mir Leid, der SIM-Slot kann nicht per Hand geöffnet werden.""", "red"))
    else:
        say(colored("""Tut mir Leid, du hast leider keine SIM-Karte in deinem Inventar.""", "red"))




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
    img = Image.open("pictures/qr.png")
    img.show()
    global qr_gesehen
    qr_gesehen = True


@when("pin eingeben", context="room4")  # eingeben
@when("eingabe pin", context="room4")
@when("eingabe der pin", context="room4")
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
@when("sim pin eingeben", context="room4")
@when("sim pin benutzen", context="room4")
@when("simpin eingeben", context="room4")
@when("simpin benutzen", context="room4")
def pin_eingeben():
    if sim_eingelegt:
        while True:
            input_2 = input(colored("PIN eingeben (oder [Abbrechen]): ", "grey", "on_white"))
            say("""""")
            if input_2 == "1234":
                say(colored("""PIN akzeptiert!""", "grey", "on_white"))
                say("""""")
                time.sleep(2.0)
                raum4Ende()
                return
            elif (input_2 == "abbrechen") or (input_2 == "Abbrechen") or (input_2 == "Abbruch"):
                return
            else:
                say(colored("""PIN falsch, bitte noch einmal versuchen.""", "grey", "on_white"))
                say("""""")
    else:
        say(colored("""Tut mir Leid, du musst die SIM-Karte erst in den SIM Slot einlegen""", "red"))



def raum4Ende():
    say(
        colored(
            """Sehr gut. Du hast es geschafft, die SIM-Karte zu entsperren.
            Auf deinem Smartphone-Display erscheint direkt das Dashboard der
            Intranet-Seite des Kraftwerks. In einer Liste am Rand werden alle
            Computer im Netzwerk angezeigt.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Das sieht schlecht aus. Alle PCs sind mit einem Schloss-Symbol versehen.
            Das kann nichts Gutes bedeuten. Du scrollst durch die Liste. Doch was ist das?""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Kurz vor Ende der Liste ist tatsächlich noch ein PC aufgeführt,
            der noch nicht mit einem Schloss Symbol versehen ist. Das ist es!
            Du klickst darauf, um dir mehr Details ansehen zu können. Dabei steht
            sogar eine Raumnummer. „Ich kann Sie dort hinführen!“, sagt der
            Kraftwerkchef aufgeregt.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    room_5.ueberleitung_room5()



@when("hilfe", context="room4")
@when("help", context="room4")
def help_room4():
    help_counter = 0
    if sim_eingelegt and qr_gesehen:
        if help_counter == 0:
            say(
                colored(
                    """Bei der Übertragung der Nachricht mit der PIN ist wohl
                    etwas schief gelaufen. Der Name des Absenders im Protokoll
                    könnte etwas mit der Entschlüsselung des Codes zu tun haben. \n
                    Hast du auf der Seite des QR-Codes schon einmal nach unten gescrollt?""",
                    "yellow"
                )
            )
            help_counter += 1
        else:
            say(
                colored(
                    """Die Nachricht enthält einen Binärcode, der für die Übertragung
                    in einen einfachen fehlerkorrigierenden Code, den sogenannten Hamming
                    Code umgewandelt wurde. \n
                    Die Anleitung beschreibt, wie man den Fehler im Code findet
                    und behebt. Im Anschluss muss man lediglich die Paritätsbits
                    entfernen und die Binärzahl in eine Dezimalzahl umwandeln.""",
                    "yellow"
                )
            )
    elif sim_eingelegt and not qr_gesehen:
        say(
            colored(
                """Schau dich doch noch einmal um. Vielleicht hast du etwas übersehen.""",
                "yellow"
            )
        )
