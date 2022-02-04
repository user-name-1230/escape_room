################
# RAUM 3: FLUR #
################

# imports
from PIL import Image
import time
from adventurelib import when, say, Bag, Item, set_context
import room_4
# import inventory
from termcolor import colored


tür_welle = Item("welle")  # 1
tür_welle.closed = True
tür_stern = Item("stern")  # 2
tür_stern.closed = True
tür_plus = Item("plus")  # 3
tür_plus.closed = False
tür_fünfeck = Item("fünfeck")  # 4
tür_fünfeck.closed = False
tür_dach = Item("dach")  # 5
tür_dach.closed = False
tür_dreieck = Item("dreieck")  # 6
tür_dreieck.closed = True
tür_minus = Item("minus")  # 7
tür_minus.closed = True

türen = Bag(
    [tür_welle, tür_stern, tür_dach, tür_dreieck, tür_fünfeck, tür_minus, tür_plus]
)

#global vars
tueren_gesehen = False
pinnwand_gesehen = False

def ueberleitung_room3():
    time.sleep(1.0)
    say(
        colored(
            """---------------------------------------------------------------------------------""",
            "yellow"
        )
    )
    say(
        colored(
            """Doch von dem lauten Geräusch scheint der Kraftwerk-Chef wieder
            aufgewacht zu sein. Er kommt schweren Schrittes auf dich zugelaufen und
            versucht dir winkend und mit letztem Atem keuchend mitzuteilen, dass die
            Pumpen nur über den Haupt-Kontrollrechner gestartet werden können.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Du musst also unbedingt einen Weg finden, den Rechner zu entsperren. Doch wie
            sollst du das bloß anstellen? Vielleicht sind noch nicht alle Rechner mit
            der Ransomware infiziert. Du musst einen Rechner finden, der noch nicht
            betroffen ist, vielleicht hilft dir das weiter.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Herr Solar scheint einen Gedankenblitz zu haben: „Wir haben neulich mit anderen Kraftwerken zusammen
            ein 5G-Campusnetz aufgebaut, das alle verfügbaren Geräte in unserem Netzwerk
            auflisten kann. Dazu braucht man nur eine passende SIM-Karte. Jedoch hab ich
            leider vergessen, wo genau die SIM-Karten gelagert werden. Es muss irgendwo
            hier drüben sein.“, sagt er und führt dich in einen langen, kargen Flur mit
            sieben Türen.""",
            "yellow"
        )
    )
    set_context("room3")


@when("umschauen", context="room3")
@when("schaue um", context="room3")
@when("schau dich um", context="room3")
@when("umsehen", context="room3")
def look_around_room3():
    # umschauen in Raum 3
    say(
        colored(
            """Auf den Türen entdeckst du seltsame Symbole. Was die wohl zu bedeuten
            haben? An der Wand hängt außerdem eine Pinnwand mit Fotos.""",
            "yellow"
        )
    )


@when("pinnwand anschauen", context="room3")  # anschauen
@when("schaue pinnwand an", context="room3")
@when("schau pinnwand an", context="room3")
@when("gucke pinnwand an", context="room3")  # gucken
@when("guck pinnwand an", context="room3")
@when("pinnwand angucken", context="room3")
@when("pinnwand betrachten", context="room3")  # betrachten
@when("betrachte pinnwand", context="room3")
@when("fotos anschauen", context="room3")  # anschauen
@when("schaue fotos an", context="room3")
@when("schau fotos an", context="room3")
@when("gucke fotos an", context="room3")  # gucken
@when("guck fotos an", context="room3")
@when("fotos angucken", context="room3")
@when("fotos betrachten", context="room3")  # betrachten
@when("betrachte fotos", context="room3")
def pinnwand_anschauen():
    pinnwand = Image.open("pictures/pinnwand.jpg")
    pinnwand.show()
    global pinnwand_gesehen
    pinnwand_gesehen = True


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
@when("symbole anschauen", context="room3")
@when("schaue symbole an", context="room3")
def tueren_anschauen():
    say(
        colored(
            """Auf jeder der sieben Türen ist jeweils ein Symbol. \n
            Einige der Türen scheinen verschlossen, andere offen zu sein, aber alle
            Räume zu durchsuchen kostet zu viel Zeit.""",
            "yellow"
        )
    )
    img = Image.open("pictures/doors.png")
    img.show()
    global tueren_gesehen
    tueren_gesehen = True


@when("öffne tür FORM", context="room3")  # öffnen
@when("öffne tür mit FORM", context="room3")
@when("öffne die tür mit FORM", context="room3")
@when("tür öffnen mit FORM", context="room3")
@when("tür mit FORM öffnen", context="room3")
@when("FORM tür öffnen", context="room3")
@when("tür mit FORM beutzen", context="room3")  # benutzen
@when("benutze tür mit FORM", context="room3")
@when("benutze die tür mit FORM", context="room3")
@when("FORM tür benutzen", context="room3")
@when("betrete raum mit FORM", context="room3")  # betreten
def tuer_oeffnen(form):
    if türen.find(form) is None:
        say(colored("""Eine Tür mit diesem Symbol gibt es nicht.""", "yellow"))
    elif form == "stern":
        # türen.find("stern").status = True
        say(
            colored(
                """Du versuchst, die Tür mit dem Stern zu öffnen.\n
                Die Tür ist verschlossen, du siehst allerdings, dass der Schlüssel steckt.
                Du schließt die Tür auf und betrittst den Raum.""",
                "yellow"
            )
        )
        say("""""")
        input(colored("[...]", "yellow"))
        say("""""")
        room_4.ueberleitung_room4()
    elif türen.find(form).closed:
        say(
            colored(
                f"""Du versuchst, die Tür mit der Form {form} zu öffnen.\n
                Das scheint die falsche Tür zu sein. Leider lässt sie sich nicht öffnen.""",
                "yellow"
            )
        )
    elif not türen.find(form).closed :
        say(
            colored(
                f"""Du versuchst, die Tür mit der Form {form} zu öffnen.\n
                Die Tür ist offen. Du schaust dich im Raum um, doch kannst nichts
                entdecken, was dir irgendwie weiterhilft. Schade...du hast wertvolle Zeit verloren.""",
                "yellow"
            )
        )



@when("öffne tür", context="room3")
@when("tür öffnen", context="room3")
def tuer_oeffnen_unklar():
    say(colored("""Ich weiß nicht, welche Tür du meinst""", "yellow"))


@when("hilfe", context="room3")
@when("help", context="room3")
def help_room3():
    if (tueren_gesehen and pinnwand_gesehen):
        say(
            colored(
                """Die Fotos scheinen in verschiedenen deutschen Städten aufgenommen
                worden zu sein. Sieh dir diese Städte doch mal auf einer Karte an.""",
                "yellow"
            )
        )
    else:
        say(
            colored(
                """Schau dich doch noch einmal um. Vielleicht hast du etwas übersehen.""",
                "yellow"
            )
        )
