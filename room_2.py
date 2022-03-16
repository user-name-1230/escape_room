#########################
# RAUM 2: MASCHINENRAUM #
#########################

# imports
from PIL import Image, ImageTk
import tkinter
import time
from adventurelib import when, say, set_context
import room_3
from inventory import *
from termcolor import colored

#global vars
zettel_angeschaut = False
ventile_angeschaut = False
ventile_gedreht = False
hebel_gesucht = False
zurueckgegangen = False
help_counter1_room2 = 0
help_counter2_room2 = 0

#objects
zettel = colored("Zettel", "yellow", attrs=["underline"])
ventile = colored("Ventile", "yellow", attrs=["underline"])
kontrollraum = colored("Kontrollraum", "yellow", attrs=["underline"])
zurueckgehen = colored("in den Kontrollraum zurückgehen", "yellow", attrs=["underline"])


def ueberleitung_room2():
    time.sleep(1.0)
    say(
        colored(
            """---------------------------------------------------------------------""",
            "yellow"
        )
    )
    say(
        colored(
            """Sehr gut. Du konntest die Sicherheitstür öffnen und rennst so schnell
            du kannst los. Dabei folgst du stur dem Warnsignal, welches dich direkt zum
            Maschinenraum führt, während es immer lauter wird. \n Beim Betreten des
            Raums nimmst du eine Durchsage einer Computerstimme aus den Lautsprechern
            wahr: „Noch 20 Minuten bis zur Kernschmelze!“ Die vielen blinkenden Lichter
            vor Ort werden alle von dem immer noch rot-pulsierenden Licht überdeckt. Das
            laute Brummen der großen Maschinen ist ohrenbetäubend. Mittig im Raum stehen
            5 riesige Pumpen.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """„Das müssen sie sein!“ Vorsichtshalber ziehst du das
            Netzwerkkabel des Steuerungsrechners für das Kühlsystems. Die Hacker dürften jetzt
            wenigstens keinen Zugriff mehr darauf haben. Was nun?""",
            "yellow"
        )
    )
    say("""""")
    set_context("room2")


@when("umschauen", context="room2")
@when("schaue um", context="room2")
@when("schau dich um", context="room2")
@when("umsehen", context="room2")
@when("um", context="room2")
def look_around_room2():
    if ventile_gedreht:
        say(
            colored(
                """Schade. Im Maschinenraum liegt leider nichts herum, was dir
                weiterhelfen könnte.""",
                "yellow"
            )
        )
        global hebel_gesucht
        hebel_gesucht = True
    else:
        say(
            colored(
                """Du entdeckst die Pumpenventile der riesigen Kühlpumpen und einen """, "yellow") +
                zettel + colored(""" auf einem Tisch in der Nähe. Die """, "yellow") + ventile +
                colored(""" scheinen beschriftet zu sein. Bestimmt muss beim Benutzen eine Reihenfolge eingehalten werden.""",
                "yellow"
            )
        )


@when("zettel anschauen", context="room2")
@when("zettel an", context="room2")
@when("zettel nehmen", context="room2")
def zettel_anschauen():
    say(colored("""                  """, "grey", "on_white"))
    say(colored(""" Lila    –   L    """, "grey", "on_white"))
    say(colored("""                  """, "grey", "on_white"))
    say(colored(""" Rot     –   R    """, "grey", "on_white"))
    say(colored("""                  """, "grey", "on_white"))
    say(colored(""" Blau    –   B    """, "grey", "on_white"))
    say(colored("""                  """, "grey", "on_white"))
    say(colored(""" Schwarz –   S    """, "grey", "on_white"))
    say(colored("""                  """, "grey", "on_white"))
    say(colored(""" Grün    –   G    """, "grey", "on_white"))
    say(colored("""                  """, "grey", "on_white"))
    global zettel_angeschaut
    zettel_angeschaut = True


@when("ventile anschauen", context="room2")
@when("pumpenventile anschauen", context="room2")
@when("ventile an", context="room2")
@when("pumpenventile an", context="room2")
def ventile_anschauen():
    root = tkinter.Tk()
    root.title('Ventile')

    ventile = ImageTk.PhotoImage(Image.open("pictures/ventile.png"))
    tkinter.Label(root, image=ventile).pack()

    root.mainloop()

    global ventile_angeschaut
    ventile_angeschaut = True


@when("ventile drehen", context="room2")
@when("ventile aufdrehen", context="room2")
@when("ventile benutzen", context="room2")
@when("ventile öffnen", context="room2")
@when("pumpenventile drehen", context="room2")
@when("pumpenventile aufdrehen", context="room2")
@when("pumpenventile benutzen", context="room2")
@when("pumpenventile öffnen", context="room2")
@when("pumpen einschalten", context="room2")
@when("pumpen benutzen", context="room2")
def ventile_drehen():
    global ventile_gedreht
    if (zurueckgegangen and ventile_gedreht and ("brecheisen" in inventory)):
        say(
            colored(
                """Die Ventile sind so fest zugedreht, dass du sie nicht bewegen
                kannst. Benutze einen Hebel, um sie aufzudrehen.""",
                "yellow"
            )
        )
    else:
        counter = 20
        while True:
            input_2 = input(colored(
                "Reihenfolge der Ventile eingeben (um evtl. weitere Hinweise zu suchen [zurück]): ", "white"))
            if (input_2 == "35124" or input_2 == "3,5,1,2,4" or input_2 == "3, 5, 1, 2, 4" or input_2 == "III, V, I, II, IV" or input_2 == "III,V,I,II,IV"):
                say(
                    colored(
                        """Das muss die richtige Reihenfolge gewesen sein. Doch die Ventile lassen sich nicht drehen. Du brauchst
                        irgendetwas, womit du mehr Kraft aufbringen kannst. Eine Art Hebel.""",
                        "yellow"
                    )
                )
                ventile_gedreht = True
                return
                # TODO gehe wieder zu Raum 1
            if input_2 == "zurück" or input_2 == "exit":
                return
            else:
                if counter > 16:
                    counter = counter - 1
                say(
                    colored(
                        f"""Das war leider die falsche Reihenfolge...du hast wertvolle Zeit verloren!\n
                        Noch {counter} Minuten bis zur Kernschmelze""",
                        "yellow"
                    )
                )
                say("""""")


@when("zurück gehen", context="room2")
@when("zurueck gehen", context="room2")
@when("zurück in kontrollraum gehen", context="room2")
@when("zurück in den kontrollraum gehen", context="room2")
@when("in kontrollraum gehen", context="room2")
@when("zu kontrollraum gehen", context="room2")
@when("kontrollraum betreten", context="room2")
@when("gehe zurück", context="room2")
@when("gehe zurück in kontrollraum", context="room2")
@when("gehe zurück in den kontrollraum", context="room2")
@when("in den kontrollraum zurückgehen", context="room2")
@when("in den kontrollraum zurück gehen", context="room2")
@when("in den kontrollraum gehen", context="room2")
@when("gehe in kontrollraum", context="room2")
@when("gehe in den kontrollraum", context="room2")
@when("gehe zu kontrollraum", context="room2")
@when("gehe in kontrollraum zurück", context="room2")
@when("gehe in kontrollraum zurueck", context="room2")
@when("gehe in den kontrollraum zurück", context="room2")
@when("gehe in den kontrollraum zurueck", context="room2")
def go_room1():
    say(
        colored(
            """Du bist zurück gegangen und befindest dich wieder im """, "yellow") +
            kontrollraum + colored(""".""",
            "yellow"
        )
    )
    set_context("room1")
    global zurueckgegangen
    zurueckgegangen = True


@when("benutze brecheisen", context="room2")  # brecheisen, benutzen
@when("benutz brecheisen", context="room2")
@when("brecheisen benutzen", context="room2")
@when("nutze brecheisen", context="room2")  # brecheisen, nutzen
@when("nutz brecheisen", context="room2")
@when("brecheisen nutzen", context="room2")
@when("nutze brechstange", context="room2")  # brechstange, benutzen
@when("nutz brechstange", context="room2")
@when("benutze brechstange", context="room2")
@when("benutz brechstange", context="room2")
@when("brechstange benutzen", context="room2")  # brechstange, nutzen
@when("brechstange nutzen", context="room2")
@when("hebel benutzen", context="room2")
@when("stange benutzen", context="room2")
@when("hebel nehmen", context="room2")
@when("stange nehmen", context="room2")
def brecheisen_benutzen2():
    if inventory.find("brecheisen") is not None:
        say(
            colored(
                """Mit dem Brecheisen als Hebel lassen sich die Ventile nun drehen.
                Die Kühlpumpen scheinen wieder anzulaufen. Doch was ist das!?
                Ein lautes Knarzen übertönt plötzlich das Warnsignal und alle
                Pumpen gehen wieder aus. Na toll...erneut hörst du eine Durchsage
                aus den Lautsprechern: „Noch 15 Minuten bis zur Kernschmelze!“""",
                "yellow"
            )
        )
        say("""""")
        input(colored("[...]", "yellow"))
        say("""""")
        room_3.ueberleitung_room3()
    else:
        say(colored("""Du hast leider nichts dabei, was du als Hebel benutzen könntest.""", "yellow"))


@when("hilfe", context="room2")
@when("help", context="room2")
def help_room2():
    if zettel_angeschaut and ventile_angeschaut and not ventile_gedreht:
        global help_counter1_room2
        if help_counter1_room2 == 0:
            say(
                colored(
                    """Irgendeine Reihenfolge muss beim Aufdrehen der Pumpenventile
                    beachtet werden. Es muss etwas mit den Buchstaben auf dem Zettel
                    zu tun haben. Vielleicht sind die Buchstaben in eine Reihenfolge
                    zu setzen.""",
                    "yellow"
                )
            )
            help_counter1_room2 += 1
        else:
            say(
                colored(
                    """Wie du bestimmt bereits gemerkt hast, ergeben die Buchstaben
                    kein spezielles Wort. Welche andere Reihenfolge können Buchstaben
                    noch haben?""",
                    "yellow"
                )
            )
    elif ((not ventile_angeschaut) or (not zettel_angeschaut)) and (not ventile_gedreht):
        say(
            colored(
                """Schau dich einfach noch einmal um. Vielleicht hast du einen
                Hinweis übersehen.""",
                "yellow"
            )
        )
    elif ventile_gedreht and (inventory.find("brecheisen") is None) and hebel_gesucht:
        global help_counter2_room2
        if help_counter2_room2 == 0:
            say(
                colored(
                    """In DIESEM Raum befindet sich kein Gegenstand, den du als Hebel
                    benutzen könntest...""",
                    "yellow"
                )
            )
            help_counter2_room2 += 1
        else:
            say(
                colored(
                    """Vielleicht kannst du """, "yellow") + zurueckgehen + colored("""
                    und dich dort noch einmal umschauen.""",
                    "yellow"
                )
            )
