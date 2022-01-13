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
print("cmds for debug: debugraum, debugitem")

# Einleitungsstory
say("""Einleitung: \n
Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste eingeladen. Unter anderem das BMI und somit Ministerin Schrader. Du, als technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten, welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef Herr Solar führt Ministerin Schrader, das Fernsehteam und dich durch die Anlage. Nach einigen Minuten gelangt ihr in das Herzstück des AKWs – den Kontrollraum – welches sich hinter einer meterdicken Sicherheitstür befindet.""")
say("""""")
time.sleep(6.0)
say("""Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt Herr Solar den Countdown herunter. Die Journalisten außerhalb des Kraftwerks lauschen gespannt mit. Ministerin Schrader hat bereits die Hand auf dem großen roten Knopf. 5...4...3...2……...plötzlich völlige Dunkelheit.""")
say("""""")
time.sleep(6.0)
say("""Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit geht ein rot-pulsierendes Notlicht an und im Kontrollraum verhallt das Warnsignal aus dem Maschinenraum. Die Sicherheitstür wird mit einem Knall verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf erscheint mit folgender Mitteilung:
"Die Evil Corp hat soeben das Kraftwerk übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen heruntergefahren.“""")
say("""""")
time.sleep(6.0)
say("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""")
say("""""")
time.sleep(6.0)
say("""„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von 100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“""")
say("""""")
time.sleep(6.0)
say("""Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort beschriftet ist. Na toll…Ransomware. Der Chef des Kraftwerks ist erschüttert und erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er vor Schreck in Ohnmacht. Ministerin Schrader greift sofort zum Telefon um den Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen Empfang. Die Wände des Kontrollraums sind zu dick. Das Fernsehteam steht ratlos in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer Lösung.""")


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


# Look Around #
@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    # TODO
    if inventory.find("brecheisen") is None:
        say("""Du siehst den Kontrollrechner und Sicherheitsausrüstung in der Ecke.""")
    else:
        say(
            """Hier ist eine Beschreibung des Kontrollraums ohne hängendem Brecheisen"""
        )


# Global Vars #
can_check_sim_slot = False
sim_schrank_offen = False
can_use_pin = False

########################
# RAUM 1: KONTROLLRAUM #
########################
<<<<<<< HEAD
# Einleitung Raum 1:
time.sleep(6.0)
say("""----------------------------------------------------------------------------------""")
say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und erschlägt dich fast und es fällt dir schwer deine Panik in den Griff zu bekommen. Du versuchst dich zu sammeln und deine Möglichkeiten abzuwägen: \n 
Du kannst dich im Raum [umschauen]\n
Du kannst Dinge im Raum [anschauen], [nehmen] und [benutzen]\n
Du kannst dein aktuelles [Inventar] anschauen\n
Du kannst dir [Hilfe] suchen, wenn du nicht weiterkommst""")

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
    if "brecheisen" not in inventory:
        say("""„Das könnte eventuell noch nützlich sein“, sagst du und packst das Brecheisen 	 direkt ein.""")
        inventory.add(crowbar)
    else:
        say("""Du hast das Brecheisen schon genommen.""")


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
        say("""Vielleicht solltest du den Kontrollrechner lieber nicht zerstören...""")

        if room1.action_counter < 2:
            # Wenn wir später in Raum 2 zurückgehen,
            # wollen wir mit dem action_counter
            # nix mehr am Hut haben
            room1.action_counter += 1
            if room1.action_counter == 2:
                ueberleitung_room2()


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
        """Du startest den Kontrollrechner neu.
    Der Bildschirm wird schwarz, nach einiger Zeit taucht der Totenkopf wieder auf.
            Das hat leider nichts gebracht."""
    )

    if room1.action_counter < 2:
        room1.action_counter += 1
        if room1.action_counter == 2:
            ueberleitung_room2()


@when("tasten drücken", context="room1")
@when("drücke tasten", context="room1")
def tasten_druecken():
    say(
        """Du versuchst verschiedenste Tastenkombinationen, doch der Totenkopf bleibt.
            Selbst Strg+Alt+Entf hilft nicht weiter. """
    )

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
    say("""Du entdeckst die Pumpenventile der riesigen Kühlpumpen und einen Zettel auf einem Tisch in der Nähe. Die Ventile scheinen beschriftet zu sein. Bestimmt muss eine Reihenfolge eingehalten werden.""")


def ueberleitung_room2(): 
	time.sleep(6.0)   						 		      	
	say("""---------------------------------------------------------------------------------""")
	say("""Sehr gut. Du konntest die Sicherheitstür öffnen und rennst so schnell du kannst los. Dabei folgst du stur dem Warnsignal, welches dich direkt zum Maschinenraum führt, während es immer lauter wird. \n Beim Betreten des Raums nimmst du eine Durchsage einer Computerstimme aus den Lautsprechern wahr: „Noch 20 Minuten bis zur Kernschmelze!“ Die vielen blinkenden Lichter vor Ort werden alle von dem immer noch rot-pulsierenden Licht überdeckt. Das laute Brummen der großen Maschinen ist ohrenbetäubend. Mittig im Raum stehen 5 riesige Pumpen. „Das müssen sie sein!“ Vorsichtshalber ziehst du das Netzwerkkabel des Kontrollrechners des Kühlsystems. Die Hacker dürften jetzt wenigstens keinen Zugriff mehr darauf haben. Was nun?""")
	say("""""")
	set_context("room2")

@when("zu den ventilen gehen", context="room2")  # gehen
@when("zu ventilen gehen", context="room2")
@when("gehe zu ventilen", context="room2")
@when("geh zu ventilen", context="room2")
@when("gehe zu den ventilen", context="room2")
@when("geh zu den ventilen", context="room2")
@when("laufe zu ventilen", context="room2")  # laufen
@when("lauf zu ventilen", context="room2")
@when("laufe zu den ventilen", context="room2")
@when("lauf zu den ventilen", context="room2")
@when("zu ventilen laufen", context="room2")
def zu_ventilen():
    # if current_room == room2:
    counter = 20
    while True:
        input_1 = input("Reihenfolge der Ventile eingeben: ")
        if input_1 == "35124":
            say(
                """Es scheint die richtige Reihenfolge zu sein, jedoch lassen sich die Pumpenventile nicht drehen."""
            )
            if inventory.find("brecheisen") is not None:
                say(
                    """Du benutzt das Brecheisen um die Ventile zu drehen, aber selbst das hilft nicht."""
                )
                time.sleep(4.0)
                room2Ende()
                return
            else:
                say("""Du benötigst einen Gegenstand um die Ventile zu drehen.""")
                return
                # TODO gehe wieder zu Raum 1
        else:
            if counter > 15:
                counter = counter - 1
            print("Noch", counter, "Minuten bis zur Kernschmelze")


def room2Ende():
    say(
        """Das Kühlsystem fällt komplett aus. Noch 15 Minuten bis zur Kernschmelze.
    Der AKW Chef wacht wieder auf und teilt mir mit, dass der Haupt-Kontrollrechner
    entschlüsselt werden muss um diesen wieder hochzufahren. Du kommst auf die
    Idee einen Rechner zu suchen welcher noch nicht von der Ransomware befallen wurde.
    Der Kraftwerks-Chef erwähnt ein 5G-Campusnetz, welches alle verfübaren Geräte im Netzwerk auflistet.
    Um Zugriff auf das Campusnetz zu bekommen, muss man eine zugehörige SIM-Karte benutzen.
    Er weiß aber nicht mehr wo genau die SIM-Karten gelagert werden."""
    )
    ueberleitung_room3()


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


def ueberleitung_room3():
    time.sleep(6.0)   						 		     	
    say("""---------------------------------------------------------------------------------""")
    say("""Doch von dem lauten Geräusch scheint der Kraftwerk-Chef wieder aufgewacht zu sein. Er kommt schweren Schrittes auf dich zugelaufen und versucht dir winkend und mit letztem Atem keuchend mitzuteilen, dass die Pumpen nur über den Haupt-Kontrollrechner gestartet werden können.\n
    Du musst also unbedingt einen Weg finden, den Rechner zu entsperren. Doch wie sollst du das bloß anstellen? Vielleicht sind noch nicht alle Rechner mit der Ransomware infiziert. Du musst einen Rechner finden, der noch nicht betroffen ist, vielleicht hilft dir das weiter.\n
    Herr Solar scheint einen Gedankenblitz zu haben: „Wir haben neulich mit anderen Kraftwerken zusammen ein 5G-Campusnetz aufgebaut, das alle verfügbaren Geräte in unserem Netzwerk auflisten kann. Dazu braucht man nur eine passende SIM-Karte. Jedoch hab ich leider vergessen, wo genau die SIM-Karten gelagert werden. Es muss irgendwo hier drüben sein.“, sagt er und führt dich in einen langen, kargen Flur mit sieben Türen.""")
    set_context("room3")


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
        ueberleitung_raum4()
    else:
        say("""Die Tür ist noch geschlossen.""")


#####################
# RAUM 4: LAGERRAUM #
#####################


@when("umschauen", context="room4")
@when("schau um", context="room4")
@when("schau dich um", context="room4")
def look_around_room4():
    say(
        """Du siehst einen Schrank mit SIM Karten drinnen. Zudem siehst du einen Lagerschrank mit 3 Abteilen und eine Werkzeugkiste. Zudem hat Ministerin Faeser ein Haarnadel dabei. etc."""
    )


def ueberleitung_raum4():
    time.sleep(6.0)   						 		     	
    say("""---------------------------------------------------------------------------------""")
    say("""Du scheinst in eine Art Lagerraum gekommen zu sein mit allerlei technischen Geräten, die ihre beste Zeit hinter sich haben. In der Ecke steht ein leeres Serverrack und daneben eine Werkzeugtasche, die allerdings nur nutzlose Werkzeuge enthält. Mal sehen, was du noch so entdecken kannst, was dir weiterhelfen könnte.""")
    set_context("room4")


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


@when("schrank öffnen", context="room4")  # öffnen
@when("öffne schrank", context="room4")
def schrank_oeffnen():
    global sim_schrank_offen
    sim_schrank_offen = True
    print("sim schrank geöffnet")


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
        print("sim karte genommen")
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
@when("öffne sim schacht", context="room4")
# sim karten schacht, öffnen
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
                print("erfolgreich geöffnet")
                global can_use_pin
                can_use_pin = True
            else:
                print("Kann nicht per Hand geöffnet werden")
        else:
            print("SIM Karte nicht im Inventar")
    else:
        print("du musst noch dein handy anschauen")


@when("faeser nach haarnadel fragen", context="room4")
@when("frage faeser nach haarnadel", context="room4")
def faeser_haarnadel():
    print("...")
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
    print("raum 4 ende beschreibung")


################
# RAUM 5: BÜRO #
################


@when("umschauen", context="room5")
@when("schau um", context="room5")
@when("schau dich um", context="room5")
def look_around_room5():
    say(
        """Du bist in einem Büro mit vielen Schreibtischen und Computern, aber keiner Menschenseele.
    Manche Computer wurden nicht ausgeschaltet."""
    )


@when("computer anschauen", context="room5")
def computer_anschauen():
    say(
        """Mehrere Computer wurden einfach angelassen. Viele zeigen den gleichen Totenkopf wie im Kontrollraum an, doch
    der Computer des Abteilungsmanagers scheint nicht befallen zu sein."""
    )


@when("computer des managers anschauen", context="room5")
def nicht_befallenen_computer_anschauen():
    say(
        """Dieser Rechner ist nicht von der Ransomware betroffen. Er scheint eine Verbindung zum Kontrollrechner
    im Kontrollraum zu haben, jedoch ist er mit einem Passwort geschützt. Das Passwort hängt auf einem
    Post-It am Monitor."""
    )


@when("computer entsperren", context="room5")
def computer_entsperren():
    # abandon all hope, ye who enters here
    say(
        """Der Computer nimmt das Passwort an. Du siehst, dass die aktuell geöffnete Kommandozeile über SSH an den
    Rechner im Kontrollraum eingeloggt ist. So ein Glück! Vielleicht findet sich jahr hier ein Passwort oder Schlüssel...
    Du setzt dich an den Rechner und wählst die Kommandozeile aus."""
    )

    current_dir = "/root"
    dir_system = {
        "/root/Dokumente": [
            "quartalsbericht_2021_q4.pdf",
            "auswertung_mitarbeiterbefragung.pptx",
            "hash_list.txt"
        ],
        "/root/Downloads": [".hash.txt"],
        "/root/Bilder": ["reaktor_schema.jpg"],
        "/root/Videos": [""],
        "/root/Musik": ["never_gonna_give_you_up.mp3"],
        "/root/Öffentlich": [""],
        "/root/Desktop": ["run_hl3.sh", "reactorcontrol.sh"],
    }
    helpmessage = """Verfügbare Kommandos: \n
            help - zeigt diese Hilfe an
            ls - listet Dateien im aktuellen Verzeichnis \n
            cd [dir] - wechselt ins Verzeichnis [dir] \n
            hashcat [file] - vergleicht Hash in Datei [file] mit Hashtabelle in Documents/hash_list.txt  \n
            [command] --help - zeigt die Hilfe des jeweiligen Programms an"""

    say(helpmessage)
    # what a terrible day to have eyes...
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
                    say("""ls - listet Dateien im aktuellen Verzeichnis \n
                    ls -a - listet Dateien inklusive versteckter Dateien auf""")
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
                if current_dir == "/root/Downloads" and file == ".passwort.txt":
                    say("""Vergleiche Hashes mit Hash in .passwort.txt...""")
                    time.sleep(5.0)
                    say("""Hash gefunden!""")
                    say("""[hash] = [passwort im klartext]""")
                else:
                    say(
                        """Fehler: Datei ist nicht verschlüsselt. Haben Sie die
                    richtige Datei ausgewählt?""")
            else:
                say("""Fehler: Kommando ungültig""")
        elif command.__contains__("cd"):
            cd_in = command.split()
            if len(cd_in) > 1:
                dir = cd_in[1]
                if dir == "--help":
                    say(
                        """cd [dir] - wechselt ins Verzeichnis [dir] \n
                    cd - (ohne Eingabe) wechselt ins Home-Verzeichnis des aktuellen Nutzers"""
                    )
                elif "/root/" + dir in dir_system.keys() and current_dir == "/root":
                    current_dir = "/root/" + dir
                elif dir in dir_system.keys() and current_dir != "/root"
                else:
                    say("""Fehler: Verzeichnis {} nicht gefunden""".format(dir))
            else:
                current_dir = "/root"

        else:
            say(
                """Error: Befehl nicht erkannt. Geben Sie 'help' ein, um alle Befehle zu sehen."""
            )

    say("""Du verlässt die Kommandozeile""")


########################
# RAUM 6: KONTROLLRAUM #
########################


@when("umschauen", context="room6")
@when("schau um", context="room6")
@when("schau dich um", context="room6")
def look_around_room6():
    say("Hinweiszettel Raum 6")


def ueberleitung_raum6():
    time.sleep(6.0)   						 		     	
    say("""---------------------------------------------------------------------------------""")
    say("""Ihr seid alle zurück im Kontrollraum angekommen. Du rennst zum Rechner. Verdammt…wo ist die Tastatur? Du findest keine Eingabemöglichkeit. Die Tastaturen der anderen Rechner würden nicht funktionieren. Die sind alle mit USB.""")
    set_context("room6")


def abspann():
    say("""IT Grundschutz Abspann""")


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
