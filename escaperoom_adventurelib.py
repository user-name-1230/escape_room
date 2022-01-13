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

# Inventar #
crowbar = Item("brecheisen")
smartphone = Item("smartphone")
hairpin = Item("haarnadel")
sim = Item("simkarte")
inventory = Bag()

@when("inventar")
@when("inventar zeigen")			#zeigen
@when("zeige inventar")
@when("inventar anzeigen")			#anzeigen
@when("anzeige vom inventar")
@when("öffne inventar")			#öffnen
@when("inventar öffnen")
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
sim_schrank_offen = False
can_use_pin = False

########################
# RAUM 1: KONTROLLRAUM #
########################


@when("das brecheisen nehmen", context="room1")	#brecheisen, nehmen
@when("brecheisen nehmen", context="room1")
@when("nehm brecheisen", context="room1")
@when("nehm das brecheisen", context="room1")
@when("nimm brecheisen", context="room1")		#brecheisen, nimm
@when("nimm das brecheisen", context="room1")
@when("die brechstange nehmen", context="room1")	#brechstange, nehmen
@when("brechstange nehmen", context="room1")
@when("nehm brechstange", context="room1")
@when("nehm die brechstange", context="room1")
@when("nimm die brechstange", context="room1")	#brechstange, nimm
@when("nimm brechstange", context="room1")
def brecheisen_nehmen():
    # Brecheisen in Raum 1 nehmen
    if "brecheisen" not in inventory:
        say("""Du nimmst das Brecheisen. Es ist schwer.""")
        inventory.add(crowbar)
    else:
        say("""Du hast das Brecheisen schon genommen.""")


@when("benutze brecheisen", context="room1")		#brecheisen, benutzen
@when("benutz brecheisen", context="room1")
@when("brecheisen benutzen", context="room1")
@when("nutze brecheisen", context="room1")		#brecheisen, nutzen
@when("nutz brecheisen", context="room1")
@when("brecheisen nutzen", context="room1")
@when("nutze brechstange", context="room1")		#brechstange, benutzen
@when("nutz brechstange", context="room1")	
@when("benutze brechstange", context="room1")
@when("benutz brechstange", context="room1")
@when("brechstange benutzen", context="room1")	#brechstange, nutzen
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


@when("computer neustarten", context="room1")		#neustarten
@when("starte computer neu", context="room1")
@when("rechner neustarten", context="room1")
@when("starte rechner neu", context="room1")
@when("pc neustarten", context="room1")
@when("starte pc neu", context="room1")
@when("kontrollrechner neustarten", context="room1")	
@when("starte kontrollrechner neu", context="room1")
@when("system neustarten", context="room1")
@when("starte system neu", context="room1")
@when("computer rebooten", context="room1")		#rebooten
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
    say("""Lila-L Rot-R Blau-B Schwarz-S Grün-G | Du solltest zu den Ventilen gehen.""")


def ueberleitung_room2():
    say("""Du betrittst den Maschinenraum voller blinkender Lichter und lauten Maschinen.
    In der Mitte des Raumes stehen 5 große Pumpen. Die Pumpen haben Ventile mit Farben darauf. \n
    I->Lila II->Rot III->Blau IV->Schwarz V->Blau""")
    set_context("room2")



@when("zu den ventilen gehen", context="room2")	#gehen
@when("zu ventilen gehen", context="room2")
@when("gehe zu ventilen", context="room2")
@when("geh zu ventilen", context="room2")
@when("gehe zu den ventilen", context="room2")
@when("geh zu den ventilen", context="room2")
@when("laufe zu ventilen", context="room2")		#laufen
@when("lauf zu ventilen", context="room2")
@when("laufe zu den ventilen", context="room2")
@when("lauf zu den ventilen", context="room2")
@when("zu ventilen laufen", context="room2")
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
                return
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



@when("pinnwand anschauen", context="room3")		#anschauen
@when("schaue pinnwand an", context="room3")
@when("schau pinnwand an", context="room3")
@when("gucke pinnwand an", context="room3")		#gucken
@when("guck pinnwand an", context="room3")
@when("pinnwand angucken", context="room3")
@when("pinnwand betrachten", context="room3")		#betrachten
@when("betrachte pinnwand", context="room3")
def pinnwand_anschauen():
    say("""Auf der Pinnwand hängen 6 Fotos von den Mitarbeitern des AKWs bei verschiedenen deutschen Sehenswürdigkeiten""")
    pinnwand = Image.open("pinnwand.jpg")
    pinnwand.show()


@when("türen anschauen", context="room3")		#anschauen
@when("schaue türen an", context="room3")
@when("schau türen an", context="room3")
@when("tür anschauen", context="room3")
@when("schaue tür an", context="room3")
@when("schau tür an", context="room3")
@when("türen angucken", context="room3")		#angucken
@when("gucke türen an", context="room3")
@when("guck türen an", context="room3")
@when("tür angucken", context="room3")
@when("gucke tür an", context="room3")
@when("guck tür an", context="room3")
@when("tür betrachten", context="room3")		#betrachten
@when("betrachte tür", context="room3")
@when("türen betrachten", context="room3")
@when("betrachte türen ", context="room3")
def tuer_anschauen():
    say("""Einige Türen scheinen verschlossen zu sein. Keine Zeit zu verlieren, du musst die richtige finden!""")


@when("öffne tür mit FORM", context="room3")		#öffnen
@when("öffne die tür mit FORM", context="room3")
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


@when("gehe in den raum", context="room3")	#gehe,raum
@when("gehe in raum", context="room3")
@when("in raum gehen", context="room3")
@when("in den raum gehen", context="room3")
@when("gehe durch tür", context="room3")	#gehe, tür
@when("gehe durch die tür", context="room3")
@when("durch tür gehen", context="room3")
@when("durch die tür gehen", context="room3")
@when("durch die tür hindurch gehen", context="room3")
@when("geh in den raum", context="room3")	#geh, raum
@when("geh in raum", context="room3")
@when("geh durch tür", context="room3")	#geh, tür
@when("geh durch die tür", context="room3")
@when("geh durch die tür hindurch", context="room3")
@when("raum betreten", context="room3")	#betreten, raum
@when("den raum betreten", context="room3")
@when("betrete raum", context="room3")	#betrete, raum
@when("betrete den raum", context="room3")
def gehe_in_lagerraum():
    print("""Du betrittst den Raum hinter der soeben geöffneten Tür.""")
    ueberleitung_raum4()



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

@when("oberes abteil angucken", context="room4")	#angucken
@when("gucke oberes abteil an", context="room4")
@when("guck oberes abteil an", context="room4")
@when("abteil oben angucken", context="room4")
@when("oberes abteil anschauen", context="room4") 	#anschauen
@when("schaue oberes abteil an", context="room4")
@when("schau oberes abteil an", context="room4")
@when("abteil oben anschauen", context="room4")
@when("abteil oben betrachten", context="room4")	#betrachten
@when("betrachte oberes abteil", context="room4")
def oberes_abteil():
    print("oberes abteil beschreibung")


@when("mittleres abteil angucken", context="room4")	#angucken
@when("gucke mittleres abteil an", context="room4")
@when("guck mittleres abteil an", context="room4")
@when("abteil mitte angucken", context="room4")
@when("abteil in der mitte angucken", context="room4")
@when("mittleres abteil anschauen", context="room4")	#anschauen
@when("schaue mittleres abteil an", context="room4")
@when("schau mittleres abteil an", context="room4")
@when("abteil mitte anschauen", context="room4")
@when("abteil in der mitte anschauen", context="room4")
@when("abteil mitte betrachten", context="room4")	#betrachten
@when("abteil in der mitte betrachten", context="room4")
@when("betrachte mittleres abteil", context="room4")
def mittleres_abteil():
    print("mittleres abteil beschreibung")


@when("unteres abteil angucken", context="room4")	#angucken
@when("gucke unteres abteil an", context="room4")
@when("abteil unten angucken", context="room4")
@when("unteres abteil anschauen", context="room4") 	#anschauen
@when("schaue unteres abteil an", context="room4")
@when("abteil unten anschauen", context="room4")
@when("abteil unten betrachten", context="room4")	#betrachten
@when("betrachte unteres abteil", context="room4")
def unteres_abteil():
    print("unteres abteil beschreibung")



@when("rechner anmachen", context="room4")		#rechner, anmachen
@when("mache rechner an", context="room4")
@when("rechner starten", context="room4")		#rechner, starten
@when("starte rechner", context="room4")
@when("rechner anschalten", context="room4")		#rechner, anschalten
@when("schalte rechner an", context="room4")
@when("computer anmachen", context="room4")		#computer, anmachen
@when("mache computer an", context="room4")
@when("computer starten", context="room4")		#computer, starten
@when("starte computer", context="room4")
@when("computer anschalten", context="room4")		#computer, anschalten
@when("schalte computer an", context="room4")
@when("pc anmachen", context="room4")			#pc, anmachen
@when("mache pc an", context="room4")
@when("pc starten", context="room4")			#pc, starten
@when("starte pc", context="room4")
@when("pc anschalten", context="room4")		#pc, anschalten
@when("schalte pc an", context="room4")
def rechner_anmachen():
    print("schon betroffen")


@when("werkzeugkiste öffnen", context="room4")	#öffnen
@when("öffne werkzeugkiste", context="room4")
def werkzeugkiste_oeffnen():
    print("werkzeugkiste geöffnet, nichts drin")


@when("schrank öffnen", context="room4")		#öffnen
@when("öffne schrank", context="room4")
def schrank_oeffnen():
    global sim_schrank_offen 
    sim_schrank_offen = True
    print("sim schrank geöffnet")


@when("sim karte nehmen", context="room4")		#nehmen
@when("sim-karte nehmen", context="room4")
@when("sim nehmen", context="room4")
@when("nehme sim karte", context="room4")
@when("nehme sim-karte", context="room4")
@when("nehme sim", context="room4")
@when("nehme die sim karte", context="room4")
@when("nehme die sim-karte", context="room4")	
@when("nehme die sim", context="room4")
@when("nehm sim karte", context="room4")
@when("nehm sim-karte", context="room4")
@when("nehm sim", context="room4")
@when("nehm die sim karte", context="room4")
@when("nehm die sim-karte", context="room4")	
@when("nehm die sim", context="room4")
@when("nimm sim karte", context="room4")		#nimm
@when("nimm sim-karte", context="room4")
@when("nimm sim", context="room4")
@when("nimm die sim karte", context="room4")
@when("nimm die sim-karte", context="room4")
@when("nimm die sim", context="room4")
def sim_karte_nehmen():
    if  not sim_schrank_offen:
        print("nicht offen")
    if  sim_schrank_offen:
        print("sim karte genommen")
        inventory.add(sim)

@when("smartphone anschauen", context="room4")	#anschauen, smartphone
@when("schaue smartphone an", context="room4")
@when("schaue das smartphone an", context="room4")
@when("schau smartphone an", context="room4")
@when("schau das smartphone an", context="room4")
@when("handy anschauen", context="room4")		#anschauen, handy
@when("schaue handy an", context="room4")
@when("schaue das handy an", context="room4")
@when("schau handy an", context="room4")
@when("schau das handy an", context="room4")
@when("smartphone angucken", context="room4")		#angucken, smartphone
@when("gucke smartphone an", context="room4")
@when("gucke das smartphone an", context="room4")
@when("guck smartphone an", context="room4")
@when("guck das smartphone an", context="room4")
@when("handy angucken", context="room4")		#angucken, handy
@when("gucke handy an", context="room4")
@when("gucke das handy an", context="room4")
@when("guck handy an", context="room4")
@when("guck das handy an", context="room4")
def smartphone_anschauen():
    print("smartphone angeschaut")
    global can_check_sim_slot 
    can_check_sim_slot = True

@when("sim schacht öffnen", context="room4")
@when("sim slot öffnen", context="room4")
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
def faeser_haarnadel():
    print("...")
    inventory.add(hairpin)

@when("qr code anzeigen", context="room4")
@when("qr code anschauen", context="room4")
def show_qr():
    img = Image.open("qr.png")
    img.show()
    
@when("pin eingeben", context="room4")
def pin_eingeben():
    if can_use_pin:
        hamming_code()
    else:
        print("SIM karte noch nicht hinzugefügt")

def hamming_code():
    while(True):
        input_2 = input("PIN eingeben: ")
        if input_2 == "1234":
            print("PIN korrekt")
            raum4Ende()
            return
        else:
            print("Falscher PIN, bitte noch einmal versuchen.")

def raum4Ende():
    print("raum 4 ende beschreibung")



########################
# RAUM 6: KONTROLLRAUM #
########################

@when("umschauen", context="room6")
@when("schau um", context="room6")
@when("schau dich um", context="room6")
def look_around_room6():
    say("Hinweiszettel Raum 6")

def ueberleitung_raum6():
    print("ueberleitung raum 6")
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
