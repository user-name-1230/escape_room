#####################
# RAUM 4: LAGERRAUM #
#####################

# imports
from PIL import Image, ImageTk
import tkinter
import time
from adventurelib import when, say, set_context
import room_5
from inventory import *
from termcolor import colored


# global vars
sim_schrank_offen = False
sim_eingelegt = False
qr_gesehen = False
help_counter_room4 = 0

#objects
qr_code = colored("QR Code", "yellow", attrs=["underline"])
haarnadel = colored("Haarnadel", "yellow", attrs=["underline"])
lagerspind = colored("Lagerspind", "yellow", attrs=["underline"])
karton = colored("Karton", "yellow", attrs=["underline"])


def ueberleitung_room4():
    time.sleep(1.0)
    say(
        colored(
            """---------------------------------------------------------------------""",
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
@when("um", context="room4")
def look_around_room4():
    if sim_eingelegt:
        say(
            colored(
                """An der Innenseite der Spindtür entdeckst du einen """, "yellow") +
                qr_code + colored(""". Ob der wohl was damit zu tun hat?""",
                "yellow"
            )
        )
    elif "simkarte" in inventory:
        say(
            colored(
                """Dir fällt sofort die feine """, "yellow") + haarnadel + colored(""" der Ministerin ins Auge.
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
                """, "yellow") + lagerspind + colored(""" mit einem Zahlenschloss,
                das anscheinend bei der letzten Benutzung nicht richtig verschlossen wurde.""",
                "yellow",
            )
        )



@when("spind öffnen", context="room4")  # öffnen
@when("öffne spind", context="room4")
@when("spind anschauen", context="room4")  # anschauen
@when("spind an", context="room4")
@when("lagerspind öffnen", context="room4")  # öffnen
@when("öffne lagerspind", context="room4")
@when("lagerspind anschauen", context="room4")  # anschauen
@when("lagerspind an", context="room4")
def spind_oeffnen():
    global sim_schrank_offen
    sim_schrank_offen = True
    say(
        colored(
            """Du öffnest den Spind und schaust dir den Inhalt genau an.
            Zuerst siehst du nur alte Ersatzteile für Computer. RAM, Lüfter,
            Netzteile, alte Festplatten und so weiter. Doch dann sticht dir ein
            kleiner """, "yellow") + karton + colored(""" mit der Aufschrift „SIM Karten“ ins Auge.""",
            "yellow",
        )
    )


@when("sim karte nehmen", context="room4")  # nehmen
@when("sim nehmen", context="room4")
@when("karte nehmen", context="room4")
@when("sim karten nehmen", context="room4")
@when("karten nehmen", context="room4")
@when("sim karte anschauen", context="room4")  # anschauen
@when("sim anschauen", context="room4")
@when("karte anschauen", context="room4")
@when("karton anschauen", context="room4")
@when("sim karte an", context="room4")
@when("sim an", context="room4")
@when("karte an", context="room4")
@when("karton an", context="room4")
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
                    worauf die Aufforderung „[SIM PIN eingeben]“ angezeigt wird.""",
                    "yellow",
                )
            )
            global sim_eingelegt
            sim_eingelegt = True
        else:
            say(colored("""Tut mir Leid, der SIM-Slot kann nicht per Hand geöffnet werden.""", "red"))
    else:
        say(colored("""Tut mir Leid, du hast leider keine SIM-Karte in deinem Inventar.""", "red"))




@when("qr code anzeigen", context="room4")  # anzeigen
@when("qrcode anzeigen", context="room4")
@when("qr anzeigen", context="room4")
@when("qr code anschauen", context="room4")  # anschauen
@when("qrcode anschauen", context="room4")
@when("qr anschauen", context="room4")
@when("qr code an", context="room4")  # anschauen
@when("qrcode an", context="room4")
@when("qr an", context="room4")
def show_qr():
    root = tkinter.Tk()
    root.title('QR-Code')

    qr = ImageTk.PhotoImage(Image.open("pictures/qr.png"))
    tkinter.Label(root, image=qr).pack()

    root.mainloop()

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
    global help_counter_room4
    if sim_eingelegt and qr_gesehen:
        if help_counter_room4 == 0:
            say(
                colored(
                    """Bei der Übertragung der Nachricht mit der PIN ist wohl
                    etwas schief gelaufen. Der Name des Absenders im Protokoll
                    könnte etwas mit der Entschlüsselung des Codes zu tun haben. \n
                    Hast du auf der Seite des QR-Codes schon einmal nach unten gescrollt?""",
                    "yellow"
                )
            )
            help_counter_room4 += 1
        else:
            say(
                colored(
                    """Die Nachricht enthält einen Binärcode, der für die Übertragung
                    in einen einfachen fehlerkorrigierenden Code, den sogenannten Hamming
                    Code umgewandelt wurde. \n
                    Um ihn zurückzuwandeln musst du zunächst die Positionen der 1en
                    also 4, 5, 7, 9, 10 und 13 in binär umwandeln (0100, 0101, 0111, ...).\n
                    Anschließend schreibst du alle Binärwerte untereinander. Das Ergebnis
                    pro Spalte, in der sich eine gerade Anzahl 1en befindet ist 0. Bei
                    einer ungeraden Anzahl 1en ist das Ergebnis 1.\n
                    Das Endergebnis des exklusiven verODERns ist die Position im
                    ursprünglichen Binärcode, an der sich der Fehler befindet. \n
                    Nachdem dieser korrigiert wurde, löscht man wie beschrieben alle
                    Positionen, die eine Potenz von 2 darstellen (1, 2, 4 und 8) aus
                    dem Binärcode raus und wandelt das Ergebnis ohne die Paritätsbits
                    in Dezimal um.""",
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
