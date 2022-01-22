# TODO
# Texte in der Einleitung langsamer machen
# Mehr Sätze
# Umlaute
# Ausrüstung / Kontrollrechner anschauen / benutzen / neustarten
# Inventar anschauen
# Sicherheitstür geht von alleine auf? (counter!)

# ventile / pumpenventile
# Mehr möglichkeiten
# Ventileingaben besser machen
# Brechstange wird automatisch benutzt

# Bild muss geschlossen werden
# Fotos / Pinnwand anschauen
# Hinweis auf L
# Hinweis auf Karte für Lösung
# "Benutze" öfter
# in raum gehen weglassen
# Spind öffnen
# haarnadel benutzen
# simslot öffnen
# pin eingeben
# Überleitung zu Raum 5

# exit in cmd
# ls richtig einrücken
# Überleitung in Raum 6
# NICHT STRG-C DRÜCKEN

# Hinweis zum Lückentext
# lower()
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import adventurelib
import sys


def no_command_matches(command):
    print(random.choice([
        "Das habe ich nicht verstanden.",
        f"Ich verstehe '{command}' leider nicht.",
        "Tur mir leid, diese Aktion scheint nicht zur Verfügung zu stehen.",
        f"Tut mir leid, die Aktion '{command}' scheint nicht zur Verfügung zu stehen."
    ]))

adventurelib.no_command_matches = no_command_matches


room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room4 = Room("""Beschreibung des Lagerraums""")


room1.has_crowbar = True
room1.action_counter = 0

# Startraum #
set_context("room1")
print("cmds for debug: debugraum, debugitem")

# Einleitungsstory
say(
"""----------------------------------------------------------------------------------"""
)
say(
    """Einleitung: \n
Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste
eingeladen. Unter anderem das BMI und somit Ministerin Schrader. Du, als
technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten,
welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef Herr Solar
führt Ministerin Schrader, das Fernsehteam und dich durch die Anlage. Nach
einigen Minuten gelangt ihr in das Herzstück des AKWs – den Kontrollraum –
welches sich hinter einer meterdicken Sicherheitstür befindet."""
)
say("""""")
say(
    """Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt
Herr Solar den Countdown herunter. Die Journalisten außerhalb des Kraftwerks
lauschen gespannt mit. Ministerin Schrader hat bereits die Hand auf dem großen
roten Knopf. 5...4...3...2........plötzlich völlige Dunkelheit."""
)
say("""""")
say(
    """Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit
geht ein rot-pulsierendes Notlicht an und im Kontrollraum verhallt das
Warnsignal aus dem Maschinenraum. Die Sicherheitstür wird mit einem Knall
verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf
erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk
übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen
heruntergefahren.“"""
)
say("""""")
say("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""")
say("""""")
say(
    """„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von
100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“"""
)
say("""""")
say(
    """Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort
beschriftet ist. Na toll…Ransomware. Der Chef des Kraftwerks ist erschüttert und
erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze
kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er
vor Schreck in Ohnmacht. Ministerin Schrader greift sofort zum Telefon um den
Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen
Empfang. Die Wände des Kontrollraums sind zu dick. Das Fernsehteam steht ratlos
in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass
eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender
mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer
Lösung."""
)


# Inventar #
crowbar = Item("brecheisen")
smartphone = Item("smartphone")
hairpin = Item("haarnadel")
sim = Item("simkarte")
inventory = Bag()


@when("inventar")
@when("inventar zeigen")  # zeigen
@when("zeige inventar")
@when("inventar anzeigen")  # anzeigen
@when("anzeige vom inventar")
@when("öffne inventar")  # öffnen
@when("inventar öffnen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f"*{item}")



# Global Vars #
#Room 1 - Kontrollraum
kontrollrechner_neugestartet = False
sicherheitsausruestung_gesehen = False
sicherheitstuer_gesehen = False
#Room 4 - Lagerraum
can_check_sim_slot = False
sim_schrank_offen = False
can_use_pin = False
#Room 5 - Büro
passwort_gefunden = False
#Room 6 - Kontrollraum
klappe_offen = False
kontrollrechner_entsperrt = False
firewall_gesehen = False



########################
# RAUM 1: KONTROLLRAUM #
########################
# Einleitung Raum 1:


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




#########################
# RAUM 2: MASCHINENRAUM #
#########################
def ueberleitung_room2():
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Sehr gut. Du konntest die Sicherheitstür öffnen und rennst so schnell
    du kannst los. Dabei folgst du stur dem Warnsignal, welches dich direkt zum
    Maschinenraum führt, während es immer lauter wird. \n Beim Betreten des
    Raums nimmst du eine Durchsage einer Computerstimme aus den Lautsprechern
    wahr: „Noch 20 Minuten bis zur Kernschmelze!“ Die vielen blinkenden Lichter
    vor Ort werden alle von dem immer noch rot-pulsierenden Licht überdeckt. Das
    laute Brummen der großen Maschinen ist ohrenbetäubend. Mittig im Raum stehen
    5 riesige Pumpen. „Das müssen sie sein!“ Vorsichtshalber ziehst du das
    Netzwerkkabel des Kontrollrechners des Kühlsystems. Die Hacker dürften jetzt
    wenigstens keinen Zugriff mehr darauf haben. Was nun?"""
    )
    say("""""")
    set_context("room2")


@when("umschauen", context="room2")
@when("schaue um", context="room2")
@when("schau dich um", context="room2")
def look_around_room2():
    say(
        """Du entdeckst die Pumpenventile der riesigen Kühlpumpen und einen
    Zettel auf einem Tisch in der Nähe. Die Ventile scheinen beschriftet zu
    sein. Bestimmt muss eine Reihenfolge eingehalten werden."""
    )


@when("zettel anschauen", context="room2")
def zettel_anschauen():
    say(
        """Lila – L\n
        Rot – R\n
        Blau – B\n
        Schwarz – S\n
        Grün – G"""
    )


@when("ventile anschauen", context="room2")
@when("pumpenventile anschauen", context="room2")
def ventile_anschauen():
    img = Image.open("ventile.jpg")
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
@when("drehen ventile", context="room2")
def zu_ventilen():
    # if current_room == room2:
    counter = 20
    while True:
        input_2 = input(
            "Reihenfolge der Ventile eingeben (um evtl. weitere Hinweise zu suchen [zurück]): "
        )
        if (input_2 == "35124" or
        input_2 == "3,5,1,2,4" or
        input_2 == "3, 5, 1, 2, 4" or
        input_2 == "III, V, I, II, IV" or
        input_2 == "III,V,I,II,IV"):
            say(
                """Das muss die richtige Reihenfolge gewesen sein. Doch die Ventile lassen sich nicht drehen. Du brauchst
                irgendetwas, womit du mehr Kraft aufbringen kannst. Eine Art Hebel."""
            )
            return
                # TODO gehe wieder zu Raum 1
        if input_2 == "zurück" or input_2 == "exit":
            return
        else:
            if counter > 15:
                counter = counter - 1
            print("Noch", counter, "Minuten bis zur Kernschmelze")


@when("brecheisen benutzen", context="room2")
def brecheisen_benutzen2():
    if inventory.find("brecheisen") is not None:
        say(
            """Die Ventile lassen sich nun drehen. Doch was ist das!? Ein lautes Knarzen übertönt plötzlich das Warnsignal
            und alle Pumpen gehen wieder aus. Na toll…erneut hörst du eine Durchsage aus den Lautsprechern: „Noch 15
            Minuten bis zur Kernschmelze!“"""
        )
        time.sleep(4.0)
        ueberleitung_room3()
    else:
        say(
            """Du hast leider kein Brecheisen dabei."""
        )



################
# RAUM 3: FLUR #
################

tür_welle = Item("welle")  # 1
tür_welle.status = False
tür_stern = Item("stern")  # 2
tür_stern.status = False
tür_plus = Item("plus")  # 3
tür_plus.status = False
tür_fünfeck = Item("fünfeck")  # 4
tür_fünfeck.status = False
tür_dach = Item("dach")  # 5
tür_dach.status = False
tür_dreieck = Item("dreieck")  # 6
tür_dreieck.status = False
tür_minus = Item("minus")  # 7
tür_minus.status = False

türen = Bag(
    [tür_welle, tür_stern, tür_dach, tür_dreieck, tür_fünfeck, tür_minus, tür_plus]
)


def ueberleitung_room3():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Doch von dem lauten Geräusch scheint der Kraftwerk-Chef wieder
    aufgewacht zu sein. Er kommt schweren Schrittes auf dich zugelaufen und
    versucht dir winkend und mit letztem Atem keuchend mitzuteilen, dass die
    Pumpen nur über den Haupt-Kontrollrechner gestartet werden können.\n
    Du musst also unbedingt einen Weg finden, den Rechner zu entsperren. Doch wie
    sollst du das bloß anstellen? Vielleicht sind noch nicht alle Rechner mit
    der Ransomware infiziert. Du musst einen Rechner finden, der noch nicht
    betroffen ist, vielleicht hilft dir das weiter.\n Herr Solar scheint einen
    Gedankenblitz zu haben: „Wir haben neulich mit anderen Kraftwerken zusammen
    ein 5G-Campusnetz aufgebaut, das alle verfügbaren Geräte in unserem Netzwerk
    auflisten kann. Dazu braucht man nur eine passende SIM-Karte. Jedoch hab ich
    leider vergessen, wo genau die SIM-Karten gelagert werden. Es muss irgendwo
    hier drüben sein.“, sagt er und führt dich in einen langen, kargen Flur mit
    sieben Türen."""
    )
    set_context("room3")


@when("umschauen", context="room3")
@when("schaue um", context="room3")
@when("schau dich um", context="room3")
def look_around_room3():
    # umschauen in Raum 3
    say(
        """Du stehst in einem langen Flur mit 7 Türen.
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
        """
    )
    img = Image.open("doors.png")
    img.show()



@when("pinnwand anschauen", context="room3")  # anschauen
@when("schaue pinnwand an", context="room3")
@when("schau pinnwand an", context="room3")
@when("gucke pinnwand an", context="room3")  # gucken
@when("guck pinnwand an", context="room3")
@when("pinnwand angucken", context="room3")
@when("pinnwand betrachten", context="room3")  # betrachten
@when("betrachte pinnwand", context="room3")
def pinnwand_anschauen():
    say(
        """Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten"""
    )
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


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
def tuer_anschauen():
    say(
        """Einige Türen scheinen verschlossen zu sein. Keine Zeit zu verlieren, du musst die richtige finden!"""
    )


@when("öffne tür mit FORM", context="room3")  # öffnen
@when("öffne die tür mit FORM", context="room3")
@when("öffne tür mit FORM", context="room3")
@when("tür öffnen mit FORM", context="room3")
@when("tür mit FORM öffnen", context="room3")
def tuer_oeffnen(form):
    if türen.find(form) is None:
        say("""Eine Tür mit diesem Symbol gibt es nicht.""")
    elif form == "stern":
        türen.find("stern").status = True
        say(
            f"""Du versuchst, die Tür mit der {form} zu öffnen.\n
        Die Tür lässt sich öffnen. Es scheint die richtige Tür zu sein!"""
        )
    else:
        # Doppelt gemoppelt, damit die Deklination passt
        say(
            f"""Du versuchst, die Tür mit dem {form} zu öffnen.
        Diese Tür scheint verschlossen zu sein. Du verlierst Zeit!"""
        )
        # TODO verschlossene Türen und leere Räume


@when("öffne tür", context="room3")
@when("tür öffnen", context="room3")
def tuer_oeffnen_unklar():
    say("""Ich weiß nicht, welche Tür du meinst""")


@when("gehe in den raum", context="room3")  # gehe,raum
@when("gehe in raum", context="room3")
@when("in raum gehen", context="room3")
@when("in den raum gehen", context="room3")
@when("gehe durch tür", context="room3")  # gehe, tür
@when("gehe durch die tür", context="room3")
@when("durch tür gehen", context="room3")
@when("durch die tür gehen", context="room3")
@when("durch die tür hindurch gehen", context="room3")
@when("geh in den raum", context="room3")  # geh, raum
@when("geh in raum", context="room3")
@when("geh durch tür", context="room3")  # geh, tür
@when("geh durch die tür", context="room3")
@when("geh durch die tür hindurch", context="room3")
@when("raum betreten", context="room3")  # betreten, raum
@when("den raum betreten", context="room3")
@when("betrete raum", context="room3")  # betrete, raum
@when("betrete den raum", context="room3")
def gehe_in_lagerraum():
    # TODO: andere Türen machen
    if türen.find("stern").status:
        say("""Du betrittst den Raum hinter der soeben geöffneten Tür.""")
        ueberleitung_room4()
    else:
        say("""Die Tür ist noch geschlossen.""")


#####################
# RAUM 4: LAGERRAUM #
#####################
def ueberleitung_room4():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Du scheinst in eine Art Lagerraum gekommen zu sein mit allerlei
    technischen Geräten, die ihre beste Zeit hinter sich haben. In der Ecke
    steht ein leeres Serverrack und daneben eine Werkzeugtasche, die allerdings
    nur nutzlose Werkzeuge enthält. Mal sehen, was du noch so entdecken kannst,
    was dir weiterhelfen könnte."""
    )
    set_context("room4")


@when("umschauen", context="room4")
@when("schau um", context="room4")
@when("schau dich um", context="room4")
def look_around_room4():
    say(
        """An der gegenüberliegenden Wand des Serverracks steht ein Lagerspind mit einem Zahlenschloss, das anscheinend bei der
    letzten Benutzung nicht richtig verschlossen wurde."""
    )



@when("oberes abteil angucken", context="room4")  # angucken
@when("gucke oberes abteil an", context="room4")
@when("guck oberes abteil an", context="room4")
@when("abteil oben angucken", context="room4")
@when("oberes abteil anschauen", context="room4")  # anschauen
@when("schaue oberes abteil an", context="room4")
@when("schau oberes abteil an", context="room4")
@when("abteil oben anschauen", context="room4")
@when("abteil oben betrachten", context="room4")  # betrachten
@when("betrachte oberes abteil", context="room4")
def oberes_abteil():
    print("oberes abteil beschreibung")


@when("mittleres abteil angucken", context="room4")  # angucken
@when("gucke mittleres abteil an", context="room4")
@when("guck mittleres abteil an", context="room4")
@when("abteil mitte angucken", context="room4")
@when("abteil in der mitte angucken", context="room4")
@when("mittleres abteil anschauen", context="room4")  # anschauen
@when("schaue mittleres abteil an", context="room4")
@when("schau mittleres abteil an", context="room4")
@when("abteil mitte anschauen", context="room4")
@when("abteil in der mitte anschauen", context="room4")
@when("abteil mitte betrachten", context="room4")  # betrachten
@when("abteil in der mitte betrachten", context="room4")
@when("betrachte mittleres abteil", context="room4")
def mittleres_abteil():
    print("mittleres abteil beschreibung")


@when("unteres abteil angucken", context="room4")  # angucken
@when("gucke unteres abteil an", context="room4")
@when("abteil unten angucken", context="room4")
@when("unteres abteil anschauen", context="room4")  # anschauen
@when("schaue unteres abteil an", context="room4")
@when("abteil unten anschauen", context="room4")
@when("abteil unten betrachten", context="room4")  # betrachten
@when("betrachte unteres abteil", context="room4")
def unteres_abteil():
    print("unteres abteil beschreibung")


@when("rechner anmachen", context="room4")  # rechner, anmachen
@when("mache rechner an", context="room4")
@when("rechner starten", context="room4")  # rechner, starten
@when("starte rechner", context="room4")
@when("rechner anschalten", context="room4")  # rechner, anschalten
@when("schalte rechner an", context="room4")
@when("computer anmachen", context="room4")  # computer, anmachen
@when("mache computer an", context="room4")
@when("computer starten", context="room4")  # computer, starten
@when("starte computer", context="room4")
@when("computer anschalten", context="room4")  # computer, anschalten
@when("schalte computer an", context="room4")
@when("pc anmachen", context="room4")  # pc, anmachen
@when("mache pc an", context="room4")
@when("pc starten", context="room4")  # pc, starten
@when("starte pc", context="room4")
@when("pc anschalten", context="room4")  # pc, anschalten
@when("schalte pc an", context="room4")
def rechner_anmachen():
    print("schon betroffen")


@when("werkzeugkiste öffnen", context="room4")  # öffnen
@when("öffne werkzeugkiste", context="room4")
def werkzeugkiste_oeffnen():
    print("werkzeugkiste geöffnet, nichts drin")


@when("spind öffnen", context="room4")  # öffnen
@when("öffne spind", context="room4")
def spind_oeffnen():
    global sim_schrank_offen
    sim_schrank_offen = True
    say(
        """Du öffnest den Spind und schaust dir den Inhalt genau an. Zuerst siehst du nur alte Ersatzteile für Computer.
    RAM,Lüfter, Netzteile, alte Festplatten und so weiter. Doch dann sticht dir ein kleiner Karton mit der Aufschrift „SIM-Karten“
    ins Auge. \n
    An der Innenseite der Spindtür entdeckst du einen QR-Code. Ob der wohl was damit zu tun hat? """
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
    if not sim_schrank_offen:
        print("nicht offen")
    if sim_schrank_offen:
        say(
            """Du nimmst dir eine Karte aus dem Karton. „Verdammt…wie soll ich denn jetzt den SIM-Slot an meinem Handy öffnen?“,
        fragst du dich.\n
        Du hörst schnelle Schritte auf dem Gang. Die Ministerin und das Fernsehteam betreten den Raum."""
        )
        inventory.add(sim)


@when("smartphone anschauen", context="room4")  # anschauen, smartphone
@when("schaue smartphone an", context="room4")
@when("schaue das smartphone an", context="room4")
@when("schau smartphone an", context="room4")
@when("schau das smartphone an", context="room4")
@when("handy anschauen", context="room4")  # anschauen, handy
@when("schaue handy an", context="room4")
@when("schaue das handy an", context="room4")
@when("schau handy an", context="room4")
@when("schau das handy an", context="room4")
@when("smartphone angucken", context="room4")  # angucken, smartphone
@when("gucke smartphone an", context="room4")
@when("gucke das smartphone an", context="room4")
@when("guck smartphone an", context="room4")
@when("guck das smartphone an", context="room4")
@when("handy angucken", context="room4")  # angucken, handy
@when("gucke handy an", context="room4")
@when("gucke das handy an", context="room4")
@when("guck handy an", context="room4")
@when("guck das handy an", context="room4")
def smartphone_anschauen():
    print("smartphone angeschaut")
    global can_check_sim_slot
    can_check_sim_slot = True


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
    if can_check_sim_slot:
        if inventory.find("simkarte") is not None:
            if inventory.find("haarnadel") is not None:
                say(
                    """Zum Glück ist die Nadel dünn genug, um den SIM-Slot zu öffnen. Du legst die SIM-Karte in dein Handy ein,
                worauf die Aufforderung „SIM-PIN eingeben“ angezeigt wird."""
                )
                global can_use_pin
                can_use_pin = True
            else:
                print("Kann nicht per Hand geöffnet werden")
        else:
            print("SIM Karte nicht im Inventar")
    else:
        print("du musst noch dein handy anschauen")


@when("schrader nach haarnadel fragen", context="room4")
@when("frage schrader nach haarnadel", context="room4")
def schrader_haarnadel():
    say(
        """Dir fällt sofort die feine Haarnadel der Ministerin ins Auge. Du fragst sie, ob du dir ihre Haarnadel kurz ausleihen
    kannst. Sie nickt aufgeregt und übergibt sie dir schnell."""
    )
    inventory.add(hairpin)


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
    img = Image.open("qr.png")
    img.show()


@when("pin eingeben", context="room4")  # eingeben
@when("eingabe pin", context="room4")
@when("eingabe vom pin", context="room4")
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
def pin_eingeben():
    if can_use_pin:
        say(
            """Sehr gut. Du hast es geschafft, die SIM-Karte zu entsperren. Auf deinem Smartphone-Display erscheint direkt das
            Dashboard der Intranet-Seite des Kraftwerks. In einer Liste am Rand werden alle Computer im Netzwerk angezeigt. Das sieht
            schlecht aus. Alle PCs sind mit einem Schloss-Symbol versehen. Das kann nichts Gutes bedeuten. Du scrollst durch die
            Liste. Doch was ist das? Kurz vor Ende der Liste ist tatsächlich noch ein PC aufgeführt, der noch nicht mit einem Schloss
            Symbol versehen ist. Das ist es! Du klickst darauf, um dir mehr Details ansehen zu können. Dabei steht sogar eine
            Raumnummer. „Ich kann Sie dort hinführen!“, sagt der Kraftwerkchef aufgeregt."""
        )
        hamming_code()
    else:
        print("SIM karte noch nicht hinzugefügt")


def hamming_code():
    while True:
        input_2 = input("PIN eingeben: ")
        if input_2 == "1234":
            print("PIN korrekt")
            raum4Ende()
            return
        else:
            print("Falscher PIN, bitte noch einmal versuchen.")


def raum4Ende():
    say("""Hier kommt eine Überleitung zu Raum 5""")
    # TODO
    set_context("room5")


################
# RAUM 5: BÜRO #
################


def ueberleitung_room5():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Du läufst zusammen mit den anderen zu einer Art Büro-Abteil. Herr Solar geht voran. Ihr betretet ein Büro und schaut
    euch kurz um. Das Büro ist bestückt mit mehreren Schreibtischen und PC-Arbeitsplätzen. Die meisten von ihnen zeigen die
    gleiche Nachricht wie der Kontrollrechner und den Totenkopf auf dem Monitor oder sind ausgeschaltet. """
    )
    set_context("room5")


@when("umschauen", context="room5")
@when("schau um", context="room5")
@when("schau dich um", context="room5")
def look_around_room5():
    say("""Schnell entdeckst du den potentiell nicht betroffenen PC im Raum.""")


# @when("computer des managers anschauen", context="room5")
# def nicht_befallenen_computer_anschauen():
#    say(
#        """Der Bildschirm zeigt ein Anmeldefenster mit einem Passwortfeld. Dir fällt direkt auf, dass auf dem Computer das Betriebssystem Kali Linux installiert ist. Du schaust dich kurz um und entdeckst, dass am Monitor ein Zettel hängt mit der Aufschrift „Passwort“. „Wie blöd!“, denkst du dir, „aber gut für mich!“. Du loggst dich ein und öffnest direkt die Kommandozeile. Mit ein paar Befehlen hast du Zugriff auf den Kontrollrechner bekommen und durchsuchst die Ordnerstruktur nach versteckten Dateien und Verzeichnissen."""
#    )


@when("computer anschauen", context="room5")
@when("computer benutzen", context="room5")
@when("computer verwenden", context="room5")
@when("pc anschauen", context="room5")
@when("pc benutzen", context="room5")
@when("pc verwenden", context="room5")
def computer_entsperren():
    # abandon all hope, ye who enters here
    say(
        """Der Bildschirm zeigt ein Anmeldefenster mit einem Passwortfeld. Dir fällt direkt auf, dass auf dem Computer das
        Betriebssystem Kali Linux installiert ist. Du schaust dich kurz um und entdeckst, dass am Monitor ein Zettel hängt mit der
        Aufschrift „Passwort“. „Wie blöd!“, denkst du dir, „aber gut für mich!“. Du loggst dich ein und öffnest direkt die
        Kommandozeile. Mit ein paar Befehlen hast du Zugriff auf den Kontrollrechner bekommen und durchsuchst die Ordnerstruktur
        nach versteckten Dateien und Verzeichnissen."""
    )

    current_dir = "/root"
    dir_system = {
        "/root/Dokumente": [
            "quartalsbericht_2021_q4.pdf",
            "auswertung_druckprofile_kuehlpumpen.xlsx",
            "reaktor_temperatur_log.log"
            "password_list.txt",
        ],
        "/root/Downloads": [".hash.txt"],
        "/root/Bilder": ["reaktor_schema.jpg"],
        "/root/Videos": [""],
        "/root/Musik": ["never_gonna_give_you_up.mp3"],
        "/root/Öffentlich": [""],
        "/root/Desktop": ["run_hl3.sh", "reactorcontrol.sh"],
    }
    helpmessage = """Verfügbare Kommandos: \n
            help                -   zeigt diese Hilfeseite an \n
            ls                  -   listet Dateien im aktuellen Verzeichnis auf \n
            cd [dir]            -   wechselt ins Verzeichnis [dir] \n
            hashcat [file]      -   vergleicht Hash in Datei [file] mit Hashes der Wörter in /root/Dokumente/password_list.txt  \n
            [command] --help    -   zeigt die Hilfeseite des Kommandos [command] an"""

    say(helpmessage)
    global passwort_gefunden
    # what a terrible day to have eyes...lol
    while True:
        command = input(current_dir + " # ")
        if command == "exit":
            break
        elif command.__contains__("ls"):
            list_all = False
            ls_in = command.split()
            if len(ls_in) > 1:
                arg = ls_in[1]
                if arg == "--help":
                    say(
                        """ls       -   listet Dateien im aktuellen Verzeichnis auf \n
                    ls -a   -   listet Dateien inklusive versteckter Dateien auf"""
                    )
                elif arg == "-a":
                    list_all = True
                else:
                    say("Fehler: Kommando ungültig")
                    continue
            if current_dir == "/root":
                for dir in dir_system:
                    say(dir)
            elif current_dir in dir_system:
                files = dir_system.get(current_dir)
                for file in files:
                    if not list_all:
                        if not file.startswith("."):
                            say(file)
                        else:
                            continue
                    else:
                        say(file)
            else:
                say("""Fehler: Kommando ungültig""")
        elif command == "help":
            say(helpmessage)
        elif command.__contains__("hashcat"):
            hashcat_in = command.split()
            if len(hashcat_in) > 1:
                file = hashcat_in[1]
                if current_dir == "/root/Downloads" and file == ".hash.txt":
                    say(
                        """Hash wird verglichen..."""
                    )
                    time.sleep(5.0)
                    say("""Hash gefunden!""")
                    say("""[781c15abfae7bda64ba65728f73b2b3c] = [30JahreBSI1991!]""")
                    passwort_gefunden = True
                else:
                    say(
                        """Fehler: Datei enthält keine Hash-Werte. Haben Sie die
                    richtige Datei ausgewählt?"""
                    )
            else:
                say("""Fehler: Kommando ungültig""")
        elif command.__contains__("cd"):
            cd_in = command.split()
            if len(cd_in) > 1:
                dir = cd_in[1]
                if dir == "--help":
                    say(
                        """cd [dir] -   wechselt ins Verzeichnis [dir] \n
                    cd         -    (ohne Eingabe) wechselt ins Home-Verzeichnis des aktuellen Nutzers"""
                    )
                elif "/root/" + dir in dir_system.keys() and current_dir == "/root":
                    current_dir = "/root/" + dir
                elif dir in dir_system.keys() and current_dir != "/root":
                    current_dir = dir
                else:
                    say("""Fehler: Verzeichnis {} nicht gefunden""".format(dir))
            else:
                current_dir = "/root"

        else:
            say(
                """Error: Befehl nicht erkannt. Geben Sie 'help' ein, um alle Befehle zu sehen."""
            )

    say("""Du verlässt die Kommandozeile""")
    if (passwort_gefunden):
        ueberleitung_room6()


########################
# RAUM 6: KONTROLLRAUM #
########################


def ueberleitung_room6():
    time.sleep(6.0)
    say(
        """---------------------------------------------------------------------------------"""
    )
    say(
        """Ihr seid alle zurück im Kontrollraum angekommen. Du rennst zum
    Rechner. Verdammt...wo ist die Tastatur? Du findest keine Eingabemöglichkeit.
    Die Tastaturen der anderen Rechner würden nicht funktionieren. Die haben alle
    einen USB-Anschluss."""
    )
    set_context("room6")


@when("umschauen", context="room6")
@when("schau um", context="room6")
@when("schau dich um", context="room6")
def look_around_room6():
    if firewall_gesehen:
        say(
            """In einer Ecke des Kontrollpultes liegt ein Zettel. Vielleicht
        hilft dir dieser ja weiter."""
        )
    else:
        say(
            """Ihr schaut euch fragend um. Der Kraftwerkchef kommt auf euch zu und
        fragt nach dem Status. Ihr erläutert ihm kurz das Problem und er zeigt auf
        eine Wartungsklappe neben dem Kontrollpult. Dort muss eine Tastatur drin
        sein, die mit dem alten DIN-AT-Anschluss kompatibel ist. Doch die Klappe
        ist so verrostet, dass du sie mit bloßen Händen nicht aufbekommt."""
        )

@when("zettel nehmen", context="room6")
@when("zettel anschauen", context="room6")
@when("zettel anzeigen", context="room6")
def zettel_anschauen2():
    say("""
    ORP.3.A7                |   5\n
    APP.3.4         | 2.2   |   14\n
    ISMS.1.A11              |   4\n
    OPS.1.1.4.A14           |   5\n
    SYS.2.1.A1              |   5"""
    )



@when("brecheisen benutzen", context="room6")
@when("mit brecheisen öffnen", context="room6")
@when("brecheisen anwenden", context="room6")
@when("brecheisen verwenden", context="room6")
def brecheisen_benutzen3():
    global klappe_offen
    klappe_offen = True
    say(
        """Gut, dass du das Brecheisen vom Anfang noch dabei hattest. Du brichst
    die Klappe auf und dahinter versteckt sich tatsächlich eine passende
    Tastatur."""
    )


@when("tastatur benutzen", context="room6")
@when("tastatur anstecken", context="room6")
@when("tastatur einstecken", context="room6")
@when("tastatur verwenden", context="room6")
@when("tastatur anstöpseln", context="room6")
@when("stecke tastatur an", context="room6")
@when("stecke tastatur ein", context="room6")
@when("passwort eintippen", context="room6")
@when("passwort eingeben", context="room6")
def tastatur_benutzen():
    if klappe_offen:
        while (True):
            input_tastatur = input("Passwort eingeben: ")
            if input_tastatur == "30JahreBSI1991!":
                say(
                    """Du steckst die Tastatur an den alten Kontrollrechner an
                und tippst das Passwort ein: 3…0…J…a…h…r…e…B…S…I…1…9…9…1…!
                ENTER!
                Der Totenkopf verschwindet. Du hast es geschafft. Doch dir fällt
                etwas ein: „Wir müssen irgendetwas tun, um die Hacker aus dem
                System zu werfen und das System besser.aBSIchern!“, rufst du.
                Du wendest dich wieder dem Kontrollrechner zu um dir den Status
                der Firewall anzuschauen."""
                )
                global kontrollrechner_entsperrt
                kontrollrechner_entsperrt = True
                return
            elif input_tastatur == "exit":
                return
            else:
                say("""Falsches Passwort. Tippe "exit" um abzubrechen.""")


@when("firewall schließen", context="room6")
@when("firewall anschauen", context="room6")
@when("status firewall", context="room6")
@when("lücken schließen", context="room6")
@when("status der firewall anschauen", context="room6")
@when("status der firewall anzeigen", context="room6")
@when("firewall reparieren", context="room6")
def firewall_schliessen():
    if kontrollrechner_entsperrt:
        global firewall_gesehen
        firewall_gesehen = True
        print(
            r"""
+---------------+---------------+-----------------------+---------------+
|               |               |                       |               |
|               |       -       |                       |       :       |
|---------------+-------+-------+------------------+----+---------------|
|                       |                          |                    |
|       DEN             |                          |                    |
|-----------------------+-------+------------------+--------------------|
|                               |                                       |
|               UND             |                                       |
|---------------+---------------+-------+---------------+---------------|
|               |                       |               |               |
|       MIT     |                       |               |       !       |
+---------------+-----------------------+---------------+---------------+

                """
        )
        say(
            """Ohje…jede Menge Lücken! Wir müssen irgendetwas tun, um die Lücken
            zu schließen:"""
        )
        while (True):
            input_loesung = input("Richtigen Satz eingeben (""exit"" um zurückzugehen): ")
            if (
                input_loesung
                == "IT-GRUNDSCHUTZ: DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN"
                or input_loesung
                == "IT-Grundschutz: Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzein"
            ):
                print_loesung_firewall()
                abspann()
            elif input_loesung == "exit":
                return
            else:
                say("""Das ist leider die falsche Antwort. Die Firewall ist immer noch offen. Hast du eventuell etwas überesehen?""")



def print_loesung_firewall():
    print(
        r"""
+---------------+---------------+-----------------------+---------------+
|               |               |                       |               |
|       IT      |       -       |       Grundschutz     |       :       |
|---------------+-------+-------+------------------+----+---------------|
|                       |                          |                    |
|       DEN             |       EINSTIEG           |       MEISTERN     |
|-----------------------+-------+------------------+--------------------|
|                               |                                       |
|               UND             |       SICHERHEITSKONZEPTE             |
|---------------+---------------+-------+---------------+---------------|
|               |                       |               |               |
|       MIT     |       MEHRWERT        |       NUTZEN  |       !       |
+---------------+-----------------------+---------------+---------------+

            """
    )


def abspann():
    say(
        """Super. Du hast die Angreifer ausgesperrt und die Lücken in der
    Firewall geschlossen. Ab hier übernimmt der Kraftwerkchef. In letzter
    Sekunde fährt er über den Kontrollrechner die Pumpen des Kühlsystems wieder
    hoch. Das rote Notlicht erlischt und das Warnsignal aus dem Maschinenraum
    ist auch nicht mehr zu hören. GESCHAFFT!"""
    )
    say(
        """Glückwunsch!\n
    Du hast die Welt vor einer Katastrophe gerettet und der Evil Corp erfolgreich
    die Stirn geboten!!!\n
    Du bist an diesem Tage wahrlich ein Volksheld und alle Anwesenden sind
    begeistert von deiner herausragenden Leistung.\n
    Zur Feier des Tages gibst du noch allen die Bedeutung der IT-Sicherheit in
    kritischen Infrastrukturen mit auf den Weg und, dass deine Reaktionen auf
    den Angriff mit sorgfältigen Präventionsmaßnahmen nach IT-Grundschutz gar
    nicht nötig gewesen wären.\n
    Natürlich wurde der Vorfall auch beim BSI-Lagezentrum gemeldet.\n
    \n
    Leider ist damit dann auch das Abenteuer vorbei.\n
    Wir bedanken uns ganz herzlich für deine Teilnahme und hoffen, das
    Textadventure hat dir gefallen.\n
    \n
    Das DACS-Praktikantenteam"""
    )
    sys.exit()


# Debug #


@when("debugraum")
def debug():
    print("RAUMNAMEN GENAU EINGEBEN!")
    print("1,2,3,4,5,6")
    debug_input = input("In welchen Raum springen? ")
    if debug_input == "1":
        set_context("room1")
    elif debug_input == "2":
        set_context("room2")
    elif debug_input == "3":
        set_context("room3")
    elif debug_input == "4":
        set_context("room4")
    elif debug_input == "5":
        set_context("room5")
    elif debug_input == "6":
        set_context("room6")


@when("debugitem")
def debug2():
    print("ITEMNAMEN GENAU EINGEBEN!")
    print("brecheisen, smartphone, haarnadel, simkarte")
    debug_input = input("Welches ITEM hinzufügen: ")
    if debug_input == "brecheisen":
        inventory.add(crowbar)
    elif debug_input == "smartphone":
        inventory.add(smartphone)
    elif debug_input == "haarnadel":
        inventory.add(hairpin)
    elif debug_input == "simkarte":
        inventory.add(sim)


## start ###
start()
