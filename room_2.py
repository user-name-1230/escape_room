#########################
# RAUM 2: MASCHINENRAUM #
#########################

# imports
from PIL import Image
import time
from adventurelib import when, say, set_context
import room_3
from inventory import *
from termcolor import colored

#global vars
ventile_gedreht = False
zurueckgegangen = False


def ueberleitung_room2():
    say(
        colored(
            """---------------------------------------------------------------------------------""",
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
            5 riesige Pumpen. „Das müssen sie sein!“ Vorsichtshalber ziehst du das
            Netzwerkkabel des Kontrollrechners des Kühlsystems. Die Hacker dürften jetzt
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
def look_around_room2():
    if ventile_gedreht:
        say(
            colored(
                """Schade. Im Maschinenraum liegt leider nichts herum, was dir
                weiterhelfen könnte.""",
                "yellow"
            )
        )
    else:
        say(
            colored(
                """Du entdeckst die Pumpenventile der riesigen Kühlpumpen und einen
                Zettel auf einem Tisch in der Nähe. Die Ventile scheinen beschriftet zu
                sein. Bestimmt muss eine Reihenfolge eingehalten werden.""",
                "yellow"
            )
        )


@when("zettel anschauen", context="room2")
def zettel_anschauen():
    say(
        colored(
            """Lila     –   L\n
            Rot     –   R\n
            Blau    –   B\n
            Schwarz –   S\n
            Grün    –   G""",
            "yellow"
        )
    )


@when("ventile anschauen", context="room2")
@when("pumpenventile anschauen", context="room2")
def ventile_anschauen():
    img = Image.open("pictures/ventile.jpg")
    img.show()


# @when("zu den ventilen gehen", context="room2")  # gehen
# @when("zu ventilen gehen", context="room2")
# @when("gehe zu ventilen", context="room2")
# @when("geh zu ventilen", context="room2")
# @when("gehe zu den ventilen", context="room2")
# @when("geh zu den ventilen", context="room2")
# @when("laufe zu ventilen", context="room2")  # laufen
# @when("lauf zu ventilen", context="room2")
# @when("laufe zu den ventilen", context="room2")
# @when("lauf zu den ventilen", context="room2")
# @when("zu ventilen laufen", context="room2")
@when("ventile drehen", context="room2")
@when("drehe ventile", context="room2")
@when("ventile benutzen", context="room2")
@when("ventile öffnen", context="room2")
@when("pumpen einschalten", context="room2")
def zu_ventilen():
    # if current_room == room2:
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
            global ventile_gedreht
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
@when("zurück in kontrollraum gehen", context="room2")
@when("in kontrollraum gehen", context="room2")
@when("zu kontrollraum gehen", context="room2")
@when("kontrollraum betreten", context="room2")
@when("gehe zurück", context="room2")
@when("gehe zurück in kontrollraum", context="room2")
def go_room1():
    say(
        colored(
            """Du bist zurück gegangen und befindest dich wieder im Kontrollraum.""",
            "yellow"
        )
    )
    set_context("room1")
    global zurueckgegangen
    zurueckgegangen = True


@when("brecheisen benutzen", context="room2")
@when("hebel benutzen", context="room2")
@when("stange benutzen", context="room2")
@when("hebel nehmen", context="room2")
@when("stange nehmen", context="room2")
def brecheisen_benutzen2():
    if inventory.find("brecheisen") is not None:
        say(
            colored(
                """Mit dem Brecheisen als Hebel lassen sich die Ventile nun drehen. Doch was ist das!? Ein lautes Knarzen übertönt plötzlich das Warnsignal
                und alle Pumpen gehen wieder aus. Na toll…erneut hörst du eine Durchsage aus den Lautsprechern: „Noch 15
                Minuten bis zur Kernschmelze!“""",
                "yellow"
            )
        )
        time.sleep(4.0)
        room_3.ueberleitung_room3()
    else:
        say(colored("""Du hast leider kein Brecheisen dabei.""", "yellow"))
