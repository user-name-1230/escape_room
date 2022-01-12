from PIL import Image
import time
from adventurelib import Room, when, say, start, Bag, Item, set_context

room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room4 = Room("""Beschreibung des Lagerraums""")

room1.has_crowbar = True
room1.action_counter = 0

# Startraum #
set_context("room1")

# Inventar #
crowbar = Item("brecheisen")
smartphone = Item("smartphone")
hairpin = Item("haarnadel")
sim = Item("sim")
inventory = Bag()

can_check_sim_slot = False
can_ask_faeser = False
sim_schrank_offen = False


@when("inventar")
@when("inventar zeigen")
@when("zeige inventar")
@when("inventar anzeigen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f'*{item}')

# Look Around #


@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    # TODO
    if inventory.find("brecheisen") is None:
        say("""Hier ist eine Beschreibung des Kontrollraums mit hängendem Brecheisen""")
    else:
        say("""Hier ist eine Beschreibung des Kontrollraums ohne hängendem Brecheisen""")


# Global Vars #
can_check_sim_slot = False

########################
# RAUM 1: KONTROLLRAUM #
########################


@when("brecheisen nehmen", context="room1")
@when("nimm brecheisen", context="room1")
@when("nimm das brecheisen", context="room1")
def brecheisen_nehmen():
    # Brecheisen in Raum 1 nehmen
    if "brecheisen" not in inventory:
        say("""Du nimmst das Brecheisen. Es ist schwer.""")
        inventory.add(crowbar)
    else:
        say("""Du hast das Brecheisen schon genommen.""")


@when("brecheisen benutzen", context="room1")
def brecheisen_benutzen():
    if inventory.find("brecheisen") is None:
        say("Du hast kein Brecheisen.")
    else:
        say("""Vielleicht solltest du den Kontrollrechner lieber nicht zerstören...""")

        if room1.action_counter < 2:
            # Wenn wir später in Raum 2 zurückgehen,
            # wollen wir mit dem action_counter
            # nix mehr am Hut haben
            room1.action_counter += 1
            if room1.action_counter == 2:
                ueberleitung_room2()


@when("computer neustarten", context="room1")
@when("rechner neustarten", context="room1")
@when("computer rebooten", context="room1")
@when("rechner rebooten", context="room1")
@when("system neustarten", context="room1")
@when("system rebooten", context="room1")
@when("kontrollrechner rebooten", context="room1")
@when("starte rechner neu", context="room1")
@when("starte kontrollrechner neu", context="room1")
@when("starte computer neu", context="room1")
@when("starte system neu", context="room1")
def computer_neustarten():
    say("""Du startest den Kontrollrechner neu.
    Der Bildschirm wird schwarz, nach einiger Zeit taucht der Totenkopf wieder auf.
            Das hat leider nichts gebracht.""")

    if room1.action_counter < 2:
        room1.action_counter += 1
        if room1.action_counter == 2:
            ueberleitung_room2()


@when("tasten drücken", context="room1")
@when("drücke tasten", context="room1")
def tasten_druecken():
    say("""Du versuchst verschiedenste Tastenkombinationen, doch der Totenkopf bleibt.
            Selbst Strg+Alt+Entf hilft nicht weiter. """)

    if room1.action_counter < 2:
        room1.action_counter += 1
        if room1.action_counter == 2:
            ueberleitung_room2()


#########################
# RAUM 2: MASCHINENRAUM #
#########################


@when("umschauen", context="room2")
@when("schaue um", context="room2")
@when("schau dich um", context="room2")
def look_around_room2():
    print("Lila-L \n Rot-R \n Blau-B \n Schwarz-S \n Grün-S \n Du solltest zu den Ventilen gehen.")


def ueberleitung_room2():
    print("""Du betrittst den Maschinenraum voller blinkender Lichter und lauten Maschinen.
    In der Mitte des Raumes stehen 5 große Pumpen. Die Pumpen haben Ventile mit Farben darauf. \n
    I->Lila \n
    II->Rot \n
    III->Blau \n
    IV->Schwarz \n
    V->Blau""")
    set_context("room2")


@when("zu den ventilen gehen", context="room2")
@when("zu ventilen gehen", context="room2")
@when("gehe zu ventilen", context="room2")
def zu_ventilen():
    # if current_room == room2:
    counter = 20
    while(True):
        input_1 = input("Reihenfolge der Ventile eingeben: ")
        if input_1 == "35124":
            say("""Es scheint die richtige Reihenfolge zu sein, jedoch lassen sich die Pumpenventile nicht drehen.""")
            if inventory.find("brecheisen") is not None:
                say("""Du benutzt das Brecheisen um die Ventile zu drehen, aber selbst das hilft nicht.""")
                time.sleep(4.0)
                room2Ende()
                return
            else:
                say("""Du benötigst einen Gegenstand um die Ventile zu drehen.""")
                # TODO gehe wieder zu Raum 1
        else:
            if counter > 15:
                counter = counter - 1
            print("Noch", counter, "Minuten bis zur Kernschmelze")


def room2Ende():
    say("""Das Kühlsystem fällt komplett aus. Noch 15 Minuten bis zur Kernschmelze.
    Der AKW Chef wacht wieder auf und teilt mir mit, dass der Haupt-Kontrollrechner
    entschlüsselt werden muss um diesen wieder hochzufahren. Du kommst auf die
    Idee einen Rechner zu suchen welcher noch nicht von der Ransomware befallen wurde.
    Der Kraftwerks-Chef erwähnt ein 5G-Campusnetz, welches alle verfübaren Geräte im Netzwerk auflistet.
    Um Zugriff auf das Campusnetz zu bekommen, muss man eine zugehörige SIM-Karte benutzen.
    Er weiß aber nicht mehr wo genau die SIM-Karten gelagert werden.""")
    ueberleitung_room3()


################
# RAUM 3: FLUR #
################

@when("umschauen", context="room3")
@when("schaue um", context="room3")
@when("schau dich um", context="room3")
def look_around_room3():
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


def ueberleitung_room3():
    print("ueberleitung raum 3")
    set_context("room3")


@when("pinnwand anschauen", context="room3")
@when("schaue pinnwand an", context="room3")
def pinnwand_anschauen():
    say("""Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten""")
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


@when("türen anschauen", context="room3")
@when("tür anschauen", context="room3")
@when("schaue tür an", context="room3")
@when("schaue türen an", context="room3")
def tuer_anschauen():
    say("""Einige Türen scheinen verschlossen zu sein. Keine Zeit zu verlieren, du musst die richtige finden!""")


@when("öffne tür mit FORM", context="room3")
@when("tür öffnen mit FORM", context="room3")
@when("tür mit FORM öffnen", context="room3")
def tuer_oeffnen(form):
    if form not in ("welle", "stern", "plus", "fünfeck", "dach", "minus", "dreieck"):
        say("""Eine Tür mit diesem Symbol gibt es nicht.""")
    elif form == "stern":
        say(f"""Du versuchst, die Tür mit der {form} zu öffnen.\n
        Die Tür lässt sich öffnen. Es scheint die richtige Tür zu sein!""")
    else:
        # Doppelt gemoppelt, damit die Deklination passt
        say(f"""Du versuchst, die Tür mit dem {form} zu öffnen.
        Diese Tür scheint verschlossen zu sein. Du verlierst Zeit!""")
        # TODO verschlossene Türen und leere Räume


@when("öffne tür", context="room3")
@when("tür öffnen", context="room3")
def tuer_oeffnen_unklar():
    say("""Ich weiß nicht, welche Tür du meinst""")


@when("gehe in den raum", context="room3")
@when("gehe in raum", context="room3")
@when("geh in den raum", context="room3")
@when("geh in raum", context="room3")
@when("in raum gehen", context="room3")
@when("in den raum gehen", context="room3")
@when("raum betreten", context="room3")
@when("den raum betreten", context="room3")
@when("betrete raum", context="room3")
@when("betrete den raum", context="room3")
def gehe_in_lagerraum():
    print("""Du betrittst den Raum hinter der soeben geöffneten Tür.""")
    ueberleitung_raum4()


@when("debug")
def debug():
    # debug
    # say(str(room1))
    # say(str(room1.has_crowbar))
    global current_room
    current_room == 4

#####################
# RAUM 4: LAGERRAUM #
#####################


@when("umschauen", context="room4")
@when("schau um", context="room4")
@when("schau dich um", context="room4")
def look_around_room4():
    say("""Du siehst einen Schrank mit SIM Karten drinnen. Zudem siehst du einen Lagerschrank mit 3 Abteilen und eine Werkzeugkiste. Zudem hat Ministerin Faeser ein Haarnadel dabei. etc.""")


def ueberleitung_raum4():
    print("ueberleitung raum 4")
    set_context("room4")


@when("oberes abteil angucken", context="room4")
def oberes_abteil():
    print("beschreibung")


@when("mittleres abteil angucken", context="room4")
def mittleres_abteil():
    print("beschreibung")


@when("unteres abteil angucken", context="room4")
def unteres_abteil():
    print("beschreibung")


@when("rechner anmachen", context="room4")
def rechner_anmachen():
    print("schon betroffen")


@when("werkzeugkiste öffnen", context="room4")
def werkzeugkiste_oeffnen():
    print("werkzeugkiste geöffnet, nichts drin")


@when("schrank öffnen", context="room4")
def schrank_oeffnen():
    sim_schrank_offen = True
    print("sim schrank geöffnet")


@when("sim karte nehmen", context="room4")
def sim_karte_nehmen():
    if sim_schrank_offen:
        print("sim karte genommen")
        inventory.add("sim")


@when("sim karten slot öffnen", context="room4")
def sim_kartenslot_oeffnen():
    if inventory.find("sim") is not None:
        print("sim slot geöffnet")


@when("smartphone anschauen", context="room4")
def smartphone_anschauen():
    print("smartphone angeschaut")
    can_check_sim_slot = True


@when("sim schacht öffnen", context="room4")
@when("sim slot öffnen", context="room4")
def sim_slot_oeffnen():
    if inventory.find("sim") is not None:
        if inventory.find("haarnadel") is None:
            print("Erfolglos mit der Hand versucht zu öffnen")
        else:
            print("erfolgreich geöffnet")
    else:
        print("SIM Karte nicht im Inventar")


@when("haarnadel nehmen", context="room4")
@when("faeser nach haarnadel fragen", context="room4")
def faeser_haarnadel():
    print("...brauchst pin....siehst qr code")
    inventory.add(hairpin)


@when("faeser nach haarnadel fragen", context="room4")
def faeser_haarnadel():
    print("...brauchst pin....siehst qr code")


@when("qr code anzeigen", context="room4")
@when("qr code anschauen", context="room4")
def show_qr():
    img = Image.open("qr.png")
    img.show()
    hamming_code()


def hamming_code():
    while(True):
        input_2 = input(
            "Bei der Übertragung der binären Nachricht kam es zu einem Fehler, Nachricht korrigieren und in Dezimal umwandeln für den PIN: ")
        if input_2 == "1234":
            print("PIN korrekt")
            raum4Ende()
            return
        else:
            print("Falscher PIN, bitte noch einmal versuchen.")


def raum4Ende():
    print("raum 4 ende beschreibung")


## start ###
start()
