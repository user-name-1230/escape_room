from adventurelib import Room, when, say, start, Bag, Item
import time
# import pyqrcode
# from PIL import Image


room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room1.has_crowbar = True
room1.action_counter = 0

crowbar = Item("brecheisen", "crowbar")
inventory = Bag()

current_room = room1  # Startraum


@when("inventar")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f'*{item}')


@when("umschauen")
@when("schaue um")
@when("schau dich um")
def look_around():
    if current_room == room1:
        # umschauen in Raum 1
        if current_room.has_crowbar:
            say("""Hier ist eine Beschreibung des Kontrollraums mit hängender Brecheisen""")
        else:
            say("""Hier ist eine Beschreibung des Kontrollraums ohne hängende Brecheisen""")
    if current_room == room2:
        print("Lila-L \n Rot-R \n Blau-B \n Schwarz-S \n Grün-S \n Du solltest zu den Ventilen gehen.")


@when("brecheisen nehmen")
def brecheisen_nehmen():
    # Brecheisen in Raum 1 nehmen
    global current_room
    if current_room == room1:
        if current_room.has_crowbar:
            current_room.has_crowbar = False
            say("""Sie nehmen die Brecheisen. Sie ist scharf und schwer.""")
            inventory.add(crowbar)
            # Falls wir noch mehr Dinge benutzen wollen, sollten wir uns
            # nicht mehr nur auf Raumattribute verlassen,
            # sondern die Items in einem Inventar speichern
        else:
            say("""Sie haben die Brecheisen schon genommen.""")


@when("brecheisen benutzen")
def brecheisen_benutzen():
    if current_room == room1:
        if not current_room.has_crowbar:
            say("""Vielleicht sollten Sie den Kontrollrechner lieber nicht zerstören...""")
            current_room.action_counter += 1
            if current_room.action_counter == 2:
                ueberleitung_room2()
        else:
            say("""Sie müssen die Brecheisen zuerst von der Wand nehmen.""")


@when("computer neustarten")
@when("rechner neustarten")
@when("computer rebooten")
@when("rechner rebooten")
def computer_neustarten():
    if current_room == room1:
        say("""Sie starten den Kontrollrechner neu.
            Der Bildschirm wird schwarz, nach einiger Zeit taucht der Totenkopf wieder auf.
            Das hat leider nichts gebracht.""")


@when("tasten drücken")
def tasten_druecken():
    if current_room == room1:
        say("""Sie versuchen verschiedenste Tastenkombinationen, doch der Totenkopf bleibt.
            Selbst Strg+Alt+Entf hilft nicht weiter. """)
        current_room.action_counter += 1
        if current_room.action_counter == 2:
            ueberleitung_room2()


def ueberleitung_room2():
    print("""Du betrittst den Maschinenraum voller blinkender Lichter und lauten Maschinen.
    In der Mitte des Raumes stehen 5 große Pumpen. Die Pumpen haben Ventile mit Farben darauf. \n
    I->Lila \n II->Rot \n III->Blau \n IV->Schwarz \n V->Blau""")
    global current_room
    current_room = room2


@when("zu den ventilen gehen")
def zu_ventilen():
    if current_room == room2:
        counter = 20
        while(True):
            input_1 = input("Reihenfolge der Ventile eingeben: ")
            if input_1 == "35124":
                say("""Es scheint die richtige Reihenfolge zu sein, jedoch lassen sich die Pumpenventile nicht drehen.""")
                if inventory.find("crowbar") != None:
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
    print("uberleitung raum 3")
    global current_room
    current_room = 3


@when("debug")
def debug():
    say(str(room1))
    say(str(room1.has_crowbar))


start()
