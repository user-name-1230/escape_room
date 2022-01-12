from PIL import Image
import time
from adventurelib import Room, when, say, start, Bag, Item, set_context
# import pyqrcode

room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room1.has_crowbar = True
room1.action_counter = 0


# current_room = room3  # Startraum
set_context("room1")

crowbar = Item("brecheisen", "crowbar")
smartphone = Item("smartphone", "smartphone")
inventory = Bag()


can_check_sim_slot = False
can_ask_faeser = False


@when("inventar")
@when("inventar zeigen")
@when("zeige inventar")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f'*{item}')


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
    I->Lila \n II->Rot \n III->Blau \n IV->Schwarz \n V->Blau""")  # TODO
    # global current_room
    # current_room = room2
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
            if inventory.find("crowbar") is not None:
                say("""Du benutzt das Brecheisen um die Ventile zu drehen, aber selbst das hilft nicht.""")
                time.sleep(4.0)
                room2Ende()
                return
            else:
                say("""Du benötigst einen Gegenstand um die Ventile zu drehen.""")
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


def ueberleitung_room3():
    # print("uberleitung raum 3")
    # global current_room
    # current_room = 3
    set_context("room3")

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


@when("gehe in raum", context="roon3")
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

def ueberleitung_raum4():
    print("ueberleitung raum 4")
    global current_room
    current_room = 4


@when("schrank öffnen")
def schrank_oeffnen():
    if current_room == 4:
        print("...")


@when("sim karte nehmen")
def sim_karte_nehmen():
    if current_room == 4:
        print("...")


@when("sim karten slot öffnen")
def sim_kartenslot_oeffnen():
    if current_room == 4:
        print("...")


@when("smartphone anschauen")
def smartphone_anschauen():
    if current_room == 4:
        print("...")
        can_check_sim_slot = True


@when("sim slot öffnen")
def sim_slot_oeffnen():
    if current_room == 4:
        if can_check_sim_slot == True:
            print("Erfolglos mit der Hand versucht zu öffnen")
            can_ask_faeser = True


@when("faeser nach haarnadel fragen")
def faeser_haarnadel():
    print("...brauchst pin....siehst qr code")


@when("qr code anschauen")
def show_qr():
    img = Image.open("qr.png")
    img.show()
    hamming_code()


def hamming_code():
    while(True):
        input_2 = input(
            "Bei der Übertragung der binären Nachricht kam es zu einem Fehler, Nachricht korrigieren und in Dezimal umwandeln für den PIN: ")
        if input_2 == "1234":
            print("PIN korrekt. Freigabe 5G Campus Netz. Öffnest Spind.")
            raum4Ende()
            return
        else:
            print("Falscher PIN, bitte noch einmal versuchen.")


@when("oberes abteil angucken")
def oberes_abteil():
    if current_room == 4:
        print("beschreibung")


@when("mittleres abteil angucken")
def mittleres_abteil():
    if current_room == 4:
        print("beschreibung")


@when("unteres abteil angucken")
def unteres_abteil():
    if current_room == 4:
        print("beschreibung")


@when("rechner anmachen")
def rechner_anmachen():
    if current_room == 4:
        print("schon betroffen")


@when("werkzeugkiste öffnen")
def werkzeugkiste_oeffnen():
    if current_room == 4:
        print("nichts drin")


def raum4Ende():
    print("raum 4 ende beschreibung")


start()
