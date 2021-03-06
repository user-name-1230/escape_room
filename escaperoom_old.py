# TODO
# ??? Mehr Daten hinter Poster ????
# Gespräche Schrader erweitern, als Hilfestellung
# Tastatur am Kontrollrechner, noch keine Abfrage, ob Passwort schon eingeben wurde, dann zu Rätsel Firewall
# Tastatur Passwort abfrage einbauen
# [Zettel] mit Hinweisen für Firewall einbauen, kommt bei umschauen, wenn Passwort erfolgreich eingegeben wurde
# Verwenden mit Brecheisen mit allem möglichen für die Neugierde der Spieler, teilweise erledigt
# Verwendung Smartphone, Foto Herr Solar und dem restlichem Inventar
# Inventar Haarnadel. Foto Herr Solar, simkarte einbauen, also deren Verwendungsoptionen
# Raum 2-6
# Fehlermeldungen bei unbekannten Befehlen ändern, auf Deutsch und auf [hilfe] hinweisen
# help Befehl deaktivieren? siehe ganz unten, bei den ganzen Befehlen ist die Übersicht sowieso weg, dann auch bei [hilfe] und zum Start den Hinweis darauf entfernen
# Beschreibung Räume, über Einleitungsstory, noch wichtig? kann das weg?
# Problem Leerzeile bei Ausgabe von benutze_reset_button und benutze_power_button, erfolgreicher PIN Eingabe, wenn das letzte Zeichen in der Zeile zu schmal ist, klappt wohl der automatische Umbruch nicht
# Geschlecht Protagonist, gendern, so lassen oder neutral schreiben
# Einbauen reden mit, aktuell nur Personen im Kontrollraum, soll das so bleiben? Würde den Code vereinfachen
# als Gag [rede mit] Gegenständen einbauen?
# gibt es überhaupt einen Raum 6?

from PIL import Image
import time
from adventurelib import Room, when, say, start, Bag, Item, set_context
import sys


### Globale Variablen ###
sicherheitstuer_offen = False
ransomware_passwort_eingegeben = False
check_sicherheitsausruestung = False
brecheisen_schienbein = False
hinweis_wartungsklappe = False
wartungsklappe_offen = False
kontrollrechner_neugestartet = False
gesichtsscan_erforderlich = False
problem_gesichtsscan = False
gesichtsscan_erfolgreich = False
problem_smartphone_oeffnen = False
herr_solar_wach = False
hinweis_maschinenraum = False
erstes_mal_raum2 = True


### allgemeine Befehle ### fuer jeden Raum

def no_command_matches(command):
    print("Das habe ich nicht verstanden")
    # das funktioniert leider nicht. Hinweise auf Befehl: [Hilfe] hinzufügen
    # siehe https://adventurelib.readthedocs.io/en/stable/customising.html


@when("hilfe")
def zeige_befehle():
    print("\nFolge Befehle sind möglich:\n[hilfe] [umschauen] [anschauen] [nehmen] [benutzen] [öffnen] [verwende mit] [rede mit]\n[Inventar] [Raum verlassen]\n\n[help] (sehr große Hilfe)\n[quit] (zum Beenden des Spiels)\n\nauf Groß- und Kleinschreibung wird keinen Wert gelegt ;-)\nAber dafür auf die genaue Schreibweise der Befehle und Objekte!")
# Befehle: umschauen anschauen nehmen benutzen öffnen 'verwende mit' Inventar help quit 'Raum verlassen'

@when("nehmen", action = "nehmen")
@when("nimm", action = "nehmen")
@when("nehme", action = "nehmen")
@when("benutzen", action = "benutzen")
@when("benutze", action = "benutzen")
@when("anschauen", action = "anschauen")
@when("schaue an", action = "anschauen")
@when("öffnen", action = "öffnen")
@when("öffne", action = "öffnen")
def standard_aktion(action):
    print(f"Was möchtest du {action}?")

@when("verwende mit")
@when("verwenden mit")
def verwende_mit():
    print("Was möchtest du womit verwenden?")
    print("zB verwende Smartphone mit dir")

# gibt es einen Raum 6?
@when("raum verlassen") ## aktuell nur Kontrollraum und Maschinenraum
@when("verlasse raum")
@when("verlassen raum")
def raum_verlassen():
    global erstes_mal_raum2
    global hinweis_maschinenraum
    global room_number
    global sicherheitstuer_offen
    if (room_number == 1 and sicherheitstuer_offen == False):
        print("Die Tür ist verschlossen. Du kannst den Raum nicht verlassen")
    else:
        while 1:
            print("Du hast folgende Möglichkeiten:")
            print("(1) Kontrollraum")
            if (hinweis_maschinenraum == True):
                print("(2) Maschinenraum")
            wohin = input("Wohin? Bitte Nummer eingeben:")
            if (wohin == "1" or wohin == "2" or wohin == "3" or wohin == "4" or wohin == "5"):
                break
            else:
                print("dies ist kein Raum, bitte Nummer eingeben, zB 1")
        wohin = int (wohin)
        if (wohin == room_number):
            print("Du befindest dich schon in diesem Raum!")
        elif (wohin == 1):
            room_number = 1
            set_context("room1")
            say("""Du gehst in den Kontrollraum.""")
            input("...")
            look_around_room1()
        elif (wohin == 2 and hinweis_maschinenraum == True):
            room_number = 2
            set_context("room2")
            if (inventory.find("foto_herr_solar") is not None):
                print("Aus Gründen des Datenschutzes löschst du das Foto von Herrn Solar.")
                inventory.take("foto_herr_solar")
                input("...")
            # Überleitungen Raum 2 beim ersten Besuch
            if (erstes_mal_raum2 == True):
                erstes_mal_raum2 = False
                ueberleitung_room2()
            else:
                say("""Du gehst in den Maschinenraum.""")
            input("...")
            look_around_room2()
# weitere elif für die anderen Räume einfügen, bitte mit Bedingung, damit man nicht vorwärts springen kann
        else:
            print("Vorwärtsspringen ist leider nicht erlaubt ;-)")


### Inventar ###
# Liste möglicher Items (Bezeichnung bei Inventaraufruf, Aliase für den internen Zugriff)
brecheisen = Item("ein Brecheisen", "brecheisen")
smartphone = Item("dein Smartphone", "smartphone")
foto_herr_solar = Item("ein Foto vom Gesicht von [Herr Solar]", "foto_herr_solar")
haarnadel = Item("eine Haarnadel von [Ministerin Schrader]", "haarnadel")
simkarte = Item("eine 5G SIM-Karte für das AKW-Netz", "simkarte")
inventory = Bag()

# Inventar Grundlagen
@when("inventar")
@when("inventar benutzen")  # benutzen
@when("benutze inventar")
@when("inventar anschauen")  # anschauen
@when("anschauen inventar")
@when("öffne inventar")  # öffnen
@when("inventar öffnen")
def zeige_inventar():
    print("Du hast: ")
    if not inventory:
        print("nichts")
        return
    for item in inventory:
        print(f"* {item}")

### Smartphone Grundlagen
@when("smartphone")
@when("anschauen smartphone")
@when("smartphone anschauen")
def zeige_smartphone():
    print("Die ist dein Smartphone.")

@when("smartphone benutzen")
@when("benutzen smartphone")
@when("benutze smartphone")
def benutze_smartphone():
    if (room_number == 1):
        print("Du hast keinen Empfang, aber die Kamera funktioniert noch.")
    else:
        print("Du versuchst deine bessere Hälfte anzurufen, um sie vor der Kernschmelze zu warnen. Aber du erreichst nur die Mailbox.")

@when("smartphone öffnen")
@when("öffnen smartphone")
@when("öffne smartphone")
def oeffne_smartphone():
    global problem_smartphone_oeffnen
    if (inventory.find("simkarte") is not None):
        print("Du kannst das Smartphone nicht öffnen. Etwas langes Spitzes könnte helfen")
        problem_smartphone_oeffnen = True
    else:
        print("Wozu solltest du das Smartphone öffnen?")

@when("nimm smartphone")
@when("nehmen smartphone")
@when("smartphone nehmen")
def nehme_smartphone():
    print("Das Smartphone befindet sich schon in deinem Inventar")

@when("smartphone verwenden")
@when("verwenden smartphone")
@when("verwende smartphone")
def verwende_smartphone():
    print("Womit möchtest du das Smartphone verwenden")
    print("zB verwende Smartphone mit dir")

@when("benutze smartphone mit OBJEKT")
@when("verwende smartphone mit OBJEKT")
def verwende_smartphone(objekt):
    global sicherheitstuer_offen
    global problem_gesichtsscan
    if (objekt == "dir"):
        say("""Du machst ein Selfie von dir. Dir gefällt es nicht und somit löschst du es gleich wieder.""")
    elif (objekt == "herr solar"):
        if (sicherheitstuer_offen == True or problem_gesichtsscan == False):
            print("Du brauchst kein Foto von ihm!")
        elif (inventory.find("foto_herr_solar") is None):
            say("""Du machst ein Foto von Herrn Solars Gesicht. Mal sehen, ob das funktioniert.""")
            inventory.add(foto_herr_solar)
        else:
            say("""Du hast schon ein Foto von ihm.""")
    else:
        say("""Du darfst hier keine Fotos machen, dies ist ein Sicherheitsbereich!""")



### Räume ###
#aktuell von mir unbenutzt, kann das weg???
room1 = Room("""Beschreibung des Kontrollraums""")
room2 = Room("""Beschreibung des Maschinenraums""")
room3 = Room("""Beschreibung des Flurs""")
room4 = Room("""Beschreibung des Lagerraums""")
room5 = Room("""Beschreibung des Büros""")

# Debug Infos #
print("cmds for debug: debugraum, debugitem, debugstatus")

# Einleitungsstory
say("""----------------------------------------------------------------------------------""")
say("""Einleitung:""")
say(""" Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste eingeladen. Unter anderem das BMI und somit [Ministerin Schrader]. Du, als technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten, welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef [Herr Solar] führt [Ministerin Schrader], das [Fernsehteam] und dich durch die Anlage. Nach einigen Minuten gelangt ihr in das Herzstück des AKWs – den [Kontrollraum] – welches sich hinter einer meterdicken [Sicherheitstür] befindet.""")
input("...")
say("""Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt [Herr Solar] den Countdown herunter. Die Journalisten außerhalb des Kraftwerks lauschen gespannt mit. [Ministerin Schrader] hat bereits die Hand auf dem großen roten Knopf. 5...4...3...2...plötzlich völlige Dunkelheit.""")
input("...")
say("""Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit geht ein rot-pulsierendes Notlicht an und im [Kontrollraum] verhallt das Warnsignal aus dem [Maschinenraum]. Die [Sicherheitstür] wird mit einem Knall verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen heruntergefahren.“""")
input("...")
say("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""")
input("...")
say("""„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von 100.000.000 Dogecoin auf die Wallet-Adresse besser.aBSIchern überweisen.“""")
input("...")
say("""Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort beschriftet ist. Na toll...Ransomware. Der Chef des Kraftwerks ist erschüttert und erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er vor Schreck in Ohnmacht. [Ministerin Schrader] greift sofort zum Telefon, um den Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen Empfang. Die Wände des Kontrollraums sind zu dick. Das [Fernsehteam] steht ratlos in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer Lösung.""")
input("...")

########################
# RAUM 1: KONTROLLRAUM #
########################
# Einleitung Raum 1:
say("""----------------------------------------------------------------------------------""")
say(
    """Du befindest dich nun im [Kontrollraum]. Die Menge an Schaltern, Hebeln und erschlägt dich fast und es fällt dir schwer deine Panik in den Griff zu bekommen. Du versuchst dich zu sammeln und deine Möglichkeiten abzuwägen: \n
Du kannst dich im Raum [umschauen].\n
Du kannst Dinge im Raum [anschauen], [nehmen], [öffnen] und [benutzen].\n
Du kannst dein aktuelles [Inventar] anschauen.\n
Du kannst dir [hilfe] suchen, wenn du nicht weiterkommst.\n
Du kannst den [Raum verlassen] oder mit [quit] das AKW verlassen (Spiel beenden).\n
Objekte in [eckigen Klammern] bieten Interaktionen. Vorsicht, hier kommt es auf die genaue Schreibweise an."""
)

# Look Around #
@when("umschauen", context="room1")
@when("schaue um", context="room1")
@when("schau dich um", context="room1")
def look_around_room1():
    # umschauen in Raum 1
    global sicherheitstuer_offen
    global ransomware_passwort_eingegeben
    if (sicherheitstuer_offen == False):
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. Du siehst den [Kontrollrechner], eine [Sicherheitsausrüstung] in der Ecke und die verschlossene [Sicherheitstür]. Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")
    elif (ransomware_passwort_eingegeben == False):
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. Du siehst den [Kontrollrechner], eine [Sicherheitsausrüstung] in der Ecke und die offene [Sicherheitstür]. Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")
    else:
        say("""Du befindest dich nun im Kontrollraum. Die Menge an Schaltern, Hebeln und erschlägt dich fast, dazwischen erblickst du ein [Poster] an der Wand. Du siehst den [Kontrollrechner], bei dem ein [Zettel] auf der Rückseite des Terminals klebt, eine [Sicherheitsausrüstung] in der Ecke und die offene [Sicherheitstür]. Des Weiteren erblickst du [Ministerin Schrader], die den ohnmächtigen [Herr Solar] in die stabile Seitenlage gebracht hat, und in einer weiteren Ecke das [Fernsehteam].""")

### Gegenstände Raum 1 ###

#Poster anschauen nehmen benutzen öffnen, kein verwende mit

@when("anschauen poster", context="room1")
@when("poster", context="room1")
@when("schaue poster an", context="room1")
def zeige_poster():
    say("""Das Poster trägt die Aufschrift „How much is the fish“. Es scheint mit Klebestreifen befestigt worden zu sein. Von der Rückseite schimmert Schrift durch das dünne Papier.""")

@when("poster nehmen", context="room1")
@when("nimm poster", context="room1")
@when("nehme poster", context="room1")
@when("nehmen poster", context="room1")
def nehme_poster():
    say("""Es ist mit Klebestreifen an der Wand befestigt. Die oberen Klebenstreifen haften zu stark und du möchstest es nicht zerstören. Du kannst aber einen Blick auf die Rückseite erhaschen. Du findest eine Widmung an Herrn Solar mit der Unterschrift von HP Baxxter und einer kurzen Biografie des Künstlers unter anderem mit seinem Geburtsdatum:""")
    say("""16. März 1964""")
    #zur erhöhung des Schwierigkeitsgrades, noch weitere Daten einbauen: siehe Confluence

@when("poster öffnen", context="room1")
@when("öffne poster", context="room1")
def oeffne_poster():
    print("Du kannst das Poster nicht öffnen!")

@when("poster benutzen", context="room1")
@when("benutze poster", context="room1")
def benutze_poster():
    print("Du kannst das Poster nicht benutzen!")

#Sicherheitsausrüstung anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue sicherheitsausrüstung an", context="room1")
@when("sicherheitsausrüstung", context="room1")
@when("anschauen sicherheitsausrüstung", context="room1")
def zeige_sicherheitsausruestung():
    global check_sicherheitsausruestung
    check_sicherheitsausruestung = True
    if inventory.find("brecheisen") is None:
        say("""Du durchsuchst die Sicherheitsausrüstung am Ende des Raumes. Dabei findest du ein Brecheisen.""")
    else:
        say("""Du durchsuchst die Sicherheitsausrüstung am Ende des Raumes. Dabei findest nichts brauchbares.""")

@when("sicherheitsausrüstung nehmen", context="room1")
@when("nimm sicherheitsausrüstung", context="room1")
@when("nehme sicherheitsausrüstung", context="room1")
@when("nehmen sicherheitsausrüstung", context="room1")
def nehme_sicherheitsausruestung():
    global check_sicherheitsausruestung
    if (check_sicherheitsausruestung == True and inventory.find("brecheisen") is None):
        nehme_brecheisen()
    else:
        print("Du kannst die Sicherheitsausrüstung nicht nehmen")

@when("sicherheitsausrüstung benutzen", context="room1")
@when("benutze sicherheitsausrüstung", context="room1")
@when("benutzen sicherheitsausrüstung", context="room1")
def benutze_sicherheitsausruestung():
    print("Du kannst die Sicherheitsausrüstung nicht benutzen!")

@when("sicherheitsausrüstung öffnen", context="room1")
@when("öffne sicherheitsausrüstung", context="room1")
def oeffne_sicherheitsausruestung():
    print("Du kannst die Sicherheitsausrüstung nicht öffnen!")

#Brecheisen Inventar anschauen nehmen benutzen öffnen, noch kein verwende mit (kommt später)
# Verwendung mit Kontrollrechner, Sicherheitstür, Pumpenventile, ...., Personen ;-)

@when("schaue brecheisen an")
@when("brecheisen")
@when("anschauen brecheisen")
def zeige_brecheisen():
    global check_sicherheitsausruestung
    global room_number
    if ((check_sicherheitsausruestung == True and room_number == 1) or inventory.find("brecheisen") is not None):
        print("Dies ist ein Brecheisen")
    else:
        print("Welches Brecheisen?")

@when("brecheisen nehmen", context="room1")
@when("nimm brecheisen", context="room1")
@when("nehme brecheisen", context="room1")
@when("nehmen brecheisen", context="room1")
def nehme_brecheisen():
    global check_sicherheitsausruestung
    if (inventory.find("brecheisen") is not None):
        print("Das Brecheisen befindet sich schon in deinem Inventar")
    elif (check_sicherheitsausruestung == True):
        inventory.add(brecheisen)
        say("""„Das könnte eventuell noch nützlich sein“, sagst du und packst das Brecheisen direkt ein.""")
        say("""Jetzt fühlst du dich wie Gordon Freeman""")
    else:
        print("Welches Brecheisen?")

@when("brecheisen benutzen")
@when("benutze brecheisen")
@when("benutzen brecheisen")
def benutze_brecheisen():
    global brecheisen_schienbein
    if (inventory.find("brecheisen") is not None):
        if (brecheisen_schienbein == False):
            say("""Aus Wut möchtest du etwas kaputt machen. Du suchst nach dem nächst besten Gegenstand und holst mit dem Brecheisen aus. Dabei verlierst du das Gleichgewicht und haust dir das Brecheisen gegen das Schienbein.""")
            say("""AUA""")
            say("""Du bist wohl doch kein Gordon Freeman ;-)""")
            brecheisen_schienbein = True
        else:
            print("Dein Schienbein schmerzt immer noch")
    else:
        print("Du hast kein Brecheisen in deinem Inventar")

@when("brecheisen öffnen")
@when("öffne brecheisen")
def oeffne_brecheisen():
    print("Du kannst das Brecheisen nicht öffnen!")

@when("benutze brecheisen mit OBJEKT")
@when("verwende brecheisen mit OBJEKT")
def verwende_brecheisen(objekt):
    global room_number
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    global brecheisen_schienbein
    if (inventory.find("brecheisen") is not None):
        if (objekt == "kontrollrechner" and room_number == 1) or (objekt == "computer" and room_number == 1):
            say("""Du schlägst mit dem [Brecheisen] auf den [Kontrollrechner] ein. Aber er bekommt nicht einmal einen kleinen Kratzer, da er aus Adamantium besteht.""")
        elif (objekt == "sicherheitstür" and room_number == 1):
            say("""Du schlägst mit dem [Brecheisen] auf die [Sicherheitstür] ein. Diese besteht aus meterdicken Stahl und du kratzt somit nur an der Oberfläche.""")
        elif (objekt == "wartungsklappe" and hinweis_wartungsklappe == True and room_number == 1 and wartungsklappe_offen == False):
            say("""Du hebelst mit dem [Brecheisen] die [Wartungsklappe] auf. Dahinter verbirgt sich eine [Tastatur].""")
            wartungsklappe_offen = True
        elif (objekt == "wartungsklappe" and room_number == 1 and wartungsklappe_offen == True):
            say("""Du hast die [Wartungsklappe] schon aufgehebelt. Noch offener wird es nicht!""")
        elif (objekt == "reset button" and room_number == 1):
            say("""Als Fingerübung drückst du mit Hilfe des Brecheisen den Reset Button.""")
            benutze_reset_button()
        elif (objekt == "power button" and room_number == 1):
            say("""Als Fingerübung drückst du mit Hilfe des Brecheisen den Power Button.""")
            benutze_power_button()
        elif (objekt == "sicherheitsausrüstung" and room_number == 1):
            say("""Du möchtest das Brecheisen nicht zurück legen, denn es fühlt sich so gut in deiner Hand an.""")
        elif (objekt == "kamera" and room_number == 1):
            say("""Es macht keinen Sinn, die Kamera zu zerstören.""")
        elif (objekt == "tastenfeld" and room_number == 1):
            say("""Du findest keinen Angriffspunkt für das Brecheisen, um es aufzuhebeln.""")
        elif (objekt == "din at buchse" and room_number == 1):
            say("""Somit wird es auch nicht zu einem USB-C Anschluss mit USB 3.2 Gen 2x2 ;-)""")
        elif (objekt == "dir"):
            say("""In das Land der Träume zu flüchten, ist keine Lösung.""")
        else:
            if (brecheisen_schienbein == False):
                say("""Du kannst nicht wahllos mit dem Brecheisen herumfuchteln, sonst verletzt du dich noch.""")
            else:
                say("""Du kannst nicht wahllos mit dem Brecheisen herumfuchteln, sonst verletzt du dich erneut ;-)""")
    else:
        print("Welches Brecheisen?")



# Kontrollrechner anschauen nehmen benutzen öffnen, kein verwende mit
# Power Button, Reset Button, DIN AT Buchse, Wartungsklappe, Tastatur

@when("schaue kontrollrechner an", context="room1")
@when("kontrollrechner", context="room1")
@when("anschauen kontrollrechner", context="room1")
@when("schaue computer an", context="room1")
@when("computer", context="room1")
@when("anschauen computer", context="room1")
def zeige_kontrollrechner():
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    say("""Der Bildschirm zeigt weiterhin den Totenkopf und die Nachricht der Erpresser. Du entdeckst ein Terminal mit Anschlüssen und einigen Knöpfen. Darunter ein [Power Button], ein [Reset Button] und eine [DIN AT Buchse].""")
    if (hinweis_wartungsklappe == True and wartungsklappe_offen == False):
        say("""Bei genauerer Betrachtung findest du unter dem Terminal eine [Wartungsklappe]""")
    if (wartungsklappe_offen == True):
        say("""Bei genauerer Betrachtung findest du unter dem Terminal eine [Tastatur]""")

@when("kontrollrechner nehmen", context="room1")
@when("nimm kontrollrechner", context="room1")
@when("nehme kontrollrechner", context="room1")
@when("nehmen kontrollrechner", context="room1")
@when("computer nehmen", context="room1")
@when("nimm computer", context="room1")
@when("nehme computer", context="room1")
@when("nehmen computer", context="room1")
def nehme_kontrollrechner():
    print("Du kannst den [Kontrollrechner] nicht nehmen!")

@when("kontrollrechner benutzen", context="room1")
@when("benutze kontrollrechner", context="room1")
@when("benutzen kontrollrechner", context="room1")
@when("computer benutzen", context="room1")
@when("benutze computer", context="room1")
@when("benutzen computer", context="room1")
def benutze_kontrollrechner():
    global wartungsklappe_offen
    if (wartungsklappe_offen == False):
        print("Du kannst den [Kontrollrechner] nicht benutzen. Du findest kein Eingabegerät.")
    else:
        beutze_tastatur()


@when("kontrollrechner öffnen", context="room1")
@when("öffne kontrollrechner", context="room1")
@when("öffnen kontrollrechner", context="room1")
@when("computer öffnen", context="room1")
@when("öffne computer", context="room1")
@when("öffnen computer", context="room1")
def oeffne_kontrollrechner():
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    if (hinweis_wartungsklappe == True and wartungsklappe_offen == False):
        print("Die [Wartungsklappe] klemmt, du kannst sie mit bloßen Händen nicht öffnen.")
    elif (wartungsklappe_offen == True):
        print("Du hast die [Wartungsklappe] schon geöffnet.")
    else:
        print("Du kannst den [Kontrollrechner] nicht öffnen!")

# DIN AT Buchse anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue din at buchse an", context="room1")
@when("din at buchse", context="room1")
@when("anschauen din at buchse", context="room1")
@when("din at buchse nehmen", context="room1")
@when("nimm din at buchse", context="room1")
@when("nehme din at buchse", context="room1")
@when("nehmen din at buchse", context="room1")
@when("din at buchse benutzen", context="room1")
@when("benutze din at buchse", context="room1")
@when("benutzen din at buchse", context="room1")
@when("din at buchse öffnen", context="room1")
@when("öffne din at buchse", context="room1")
@when("öffnen din at buchse", context="room1")
def din_at_buchse():
    print("Solch einen vorsintflutlichen Anschluß hast du lange nicht mehr gesehen. Der ist wohl zu nix zu gebrauchen.")

# Power Button anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue power button an", context="room1")
@when("power button", context="room1")
@when("anschauen power button", context="room1")
def zeige_power_button():
    print("Dies ist ein [Power Button]. Dieser sollte den [Kontrollrechner] an- bzw. ausschalten.")

@when("power button nehmen", context="room1")
@when("nimm power button", context="room1")
@when("nehme power button", context="room1")
@when("nehmen power button", context="room1")
@when("power button öffnen", context="room1")
@when("öffne power button", context="room1")
@when("öffnen power button", context="room1")
def power_button():
    print("Das funktioniert nicht mit dem [Power Button].")

@when("power button benutzen", context="room1")
@when("benutze power button", context="room1")
@when("benutzen power button", context="room1")
def benutze_power_button():
    global kontrollrechner_neugestartet
    kontrollrechner_neugestartet = True
    say("""Du drückst auf den [Power Button], aber nichts passiert. Also versuchst du es ein zweites Mal, nur länger. Nach gefühlten 10 Sekunden wird der Bildschirm schwarz, nur um gleich wieder zu erhellen. Der Rechner fährt wieder hoch, BIOS-Meldungen erscheinen auf dem Bildschirm, ein Windows 95 – Startsound ertönt und die Erpresserbotschaft erscheint direkt wieder nach dem Bootvorgang. „Das bringt nichts!“, denkst du dir und überlegst, was du tun sollst.""")

# Reset Button anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue reset button an", context="room1")
@when("reset button", context="room1")
@when("anschauen reset button", context="room1")
def zeige_reset_button():
    print("Dies ist ein [Reset Button]. Dieser sollte den [Kontrollrechner] neustarten.")

@when("reset button nehmen", context="room1")
@when("nimm reset button", context="room1")
@when("nehme reset button", context="room1")
@when("nehmen reset button", context="room1")
@when("reset button öffnen", context="room1")
@when("öffne reset button", context="room1")
@when("öffnen reset button", context="room1")
def reset_button():
    print("Das funktioniert nicht mit dem [Reset Button].")

@when("reset button benutzen", context="room1")
@when("benutze reset button", context="room1")
@when("benutzen reset button", context="room1")
def benutze_reset_button():
    global kontrollrechner_neugestartet
    kontrollrechner_neugestartet = True
    say("""Du drückst auf den [Reset Button]. Der Rechner startet neu, BIOS-Meldungen erscheinen auf dem Bildschirm, ein Windows 95 – Startsound ertönt und die Erpresserbotschaft erscheint direkt wieder nach dem Bootvorgang. „Das bringt nichts!“, denkst du dir und überlegst, was du tun sollst.""")

# Tastatur anschauen nehmen benutzen öffnen, kein verwende mit
# TODO erweitern auf Eingabe Passwort und Eingabe Firewall

@when("schaue tastatur an", context="room1")
@when("tastatur", context="room1")
@when("anschauen tastatur", context="room1")
def zeige_tastatur():
    global wartungsklappe_offen
    if (wartungsklappe_offen == True):
        print("Dies ist die [Tastatur] vom [kontrollrechner]. Damit kannst du ihn bedienen.")
    else:
        print("Welche Tastatur?")

@when("tastatur nehmen", context="room1")
@when("nimm tastatur", context="room1")
@when("nehme tastatur", context="room1")
@when("nehmen tastatur", context="room1")
@when("tastatur öffnen", context="room1")
@when("öffne tastatur", context="room1")
@when("öffnen tastatur", context="room1")
def tastatur():
    global wartungsklappe_offen
    if (wartungsklappe_offen == True):
        print("Das funktioniert nicht mit der [Tastatur].")
    else:
        print("Welche Tastatur?")

@when("benutzen tastatur", context="room1")
@when("benutze tastatur", context="room1")
@when("tastatur benutzen", context="room1")
def beutze_tastatur():
    global wartungsklappe_offen
    global ransomware_passwort_eingegeben
# Abfrage Passwort einbauen und Abfrage Firewall
    if (wartungsklappe_offen == True and ransomware_passwort_eingegeben == False):
        print("Der Bildschirm zeigt weiterhin den Totenkopf und die Nachricht der Erpresser.")
        print("Unter der Mitteilung erscheint ein Eingabefeld, welches mit Passwort beschriftet ist.")
        print("Du benutzt die [Tastatur] an den alten [Kontrollrechner] und tippst das Passwort ein:")
        print("Sorry hier fehlt noch die Abfrage...")
# Passwort abfrage aufrufen
    elif (ransomware_passwort_eingegeben == True):
        print("Nun möchtest du das System absichern und suchst nach der Firewall.")
        print("Du findest deren Einstellungen und entdeckst ein Problem:")
        print("Die Firewall hat auffällig viele Lücken, kannst du sie alle schließen?")
        print("Irgendwo in der Nähe muss es doch einen Hinweis geben ;-)")
# Rästsel Firewall aufrufen
    else:
        print("Welche Tastatur?")


# Wartungsklappe anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue wartungsklappe an", context="room1")
@when("wartungsklappe", context="room1")
@when("anschauen wartungsklappe", context="room1")
@when("schaue klappe an", context="room1")
@when("klappe", context="room1")
@when("anschauen klappe", context="room1")
def zeige_wartungsklappe():
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    if (hinweis_wartungsklappe == True and wartungsklappe_offen == False):
        say("""Unter dem Terminal findest du eine alte rostige [Wartungsklappe]. Mal sehen, was sich dahinter verbirgt.""")
    elif (wartungsklappe_offen == True):
        say("""Hinter der alten rostigen Wartungsklappe findest du eine [Tastatur]. Mal sehen, ob sie noch funktioniert.""")
    else:
        print("Welche Wartungsklappe?")

@when("wartungsklappe benutzen", context="room1")
@when("benutze wartungsklappe", context="room1")
@when("benutzen wartungsklappe", context="room1")
@when("wartungsklappe öffnen", context="room1")
@when("öffne wartungsklappe", context="room1")
@when("öffnen wartungsklappe", context="room1")
@when("klappe öffnen", context="room1")
@when("öffne klappe", context="room1")
@when("öffnen klappe", context="room1")
def oeffne_wartungsklappe():
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    if (hinweis_wartungsklappe == True and wartungsklappe_offen == False):
        print("Die [Wartungsklappe] klemmt, du kannst sie mit bloßen Händen nicht öffnen.")
    elif (wartungsklappe_offen == True):
        print("Du hast die [Wartungsklappe] schon geöffnet.")
    else:
        print("Welche Wartungsklappe?")

@when("wartungsklappe nehmen", context="room1")
@when("nimm wartungsklappe", context="room1")
@when("nehme wartungsklappe", context="room1")
@when("nehmen wartungsklappe", context="room1")
def nehme_wartungsklappe():
    print("Du kannst die Sicherheitstür nicht nehmen.")

# Sicherheitstür anschauen nehmen benutzen öffnen, kein verwende mit
# Tastenfeld Kamera

@when("schaue sicherheitstür an", context="room1")
@when("sicherheitstür", context="room1")
@when("anschauen sicherheitstür", context="room1")
def zeige_sicherheitstuer():
    global sicherheitstuer_offen
    if (sicherheitstuer_offen == True):
        print("Die Sicherheitstür ist offen. Du kannst den Raum verlassen.")
    else:
        say("""Du entdeckst die riesige meterdicke Sicherheitstür. Direkt neben der Tür befindet sich ein [Tastenfeld] und darüber eine [Kamera].""")

@when("sicherheitstür nehmen", context="room1")
@when("nimm sicherheitstür", context="room1")
@when("nehme sicherheitstür", context="room1")
@when("nehmen sicherheitstür", context="room1")
def nehme_sicherheitstuer():
    print("Du kannst die Sicherheitstür nicht nehmen.")

@when("sicherheitstür benutzen", context="room1")
@when("benutze sicherheitstür", context="room1")
@when("benutzen sicherheitstür", context="room1")
def benutze_sicherheitstuer():
    print("Du kann die Sicherheitstür nicht benutzen. Versuche das Tastenfeld ;-)")

@when("sicherheitstür öffnen", context="room1")
@when("öffne sicherheitstür", context="room1")
@when("öffnen sicherheitstür", context="room1")
def oeffne_sicherheitstuer():
    global sicherheitstuer_offen
    if (sicherheitstuer_offen == True):
        print("Die Sicherheitstür ist schon offen.")
    else:
        print("Du rüttelst an der Tür, doch sie bewegt sich keinen Zentimeter.")

# Tastenfeld anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue tastenfeld an", context="room1")
@when("tastenfeld", context="room1")
@when("anschauen tastenfeld", context="room1")
def zeige_tastenfeld():
    print("Die ist ein Tastenfeld mit den Zahlen 0-9, 'Abbruch' und 'Start'")

@when("tastenfeld nehmen", context="room1")
@when("nimm tastenfeld", context="room1")
@when("nehme tastenfeld", context="room1")
@when("nehmen tastenfeld", context="room1")
def nehme_tastenfeld():
    print("Du kannst das Tastenfeld nicht nehmen.")

@when("tastenfeld öffnen", context="room1")
@when("öffne tastenfeld", context="room1")
@when("öffnen tastenfeld", context="room1")
def oeffne_tastenfeld():
    print("Du kannst das Tastenfeld nicht öffnen.")

@when("tastenfeld benutzen", context="room1")
@when("benutze tastenfeld", context="room1")
@when("benutzen tastenfeld", context="room1")
def benutze_tastenfeld():
    global sicherheitstuer_offen
    global gesichtsscan_erforderlich
    global gesichtsscan_erfolgreich
    if (sicherheitstuer_offen == True):
        print("Die Sicherheitstür ist schon offen. Du brauchst das Tastenfeld niht mehr zu benutzen.")
    elif (gesichtsscan_erfolgreich == True):
        say("""Das Display zeigt immer noch: * * * * * *.""")
        pin = input("PIN: ******: ")
        if (pin == "160364"):
            print("Eingabe korrekt")
            sicherheitstuer_offen = True
            print("Du hörst ein Klacken und die Sicherheitstür öffnet sich mit einem leisen Surren.")
        elif (pin == "abbruch" or pin == "Abbruch"):
            print("Du verlässt die Eingabe und überlegst woher du den PIN bekommen könntest.")
        else:
            print("'Fehler: eingabe falsch'")
            gesichtsscan_erfolgreich = False
            print("'Bitte Gesicht scannen'")
            gesichtsscan_erforderlich = True
            say("""„Mist, wo krieg ich denn jetzt den PIN her?“, fragst du dich und überlegst.""")
    else:
        print("Du drückst die Grüne Starttaste und die Meldung: 'Bitte Gesicht scannen' erscheint.")
        gesichtsscan_erforderlich = True

# Kamera anschauen nehmen benutzen öffnen, kein verwende mit

@when("schaue kamera an", context="room1")
@when("kamera", context="room1")
@when("anschauen kamera", context="room1")
def zeige_kamera():
    print("Du siehst ein Kameraobjekt. Wozu das wohl da ist?")

@when("kamera nehmen", context="room1")
@when("nimm kamera", context="room1")
@when("nehme kamera", context="room1")
@when("nehmen kamera", context="room1")
def nehme_kamera():
    print("Du kannst die Kamera nicht nehmen.")

@when("kamera öffnen", context="room1")
@when("öffne kamera", context="room1")
@when("öffnen kamera", context="room1")
def oeffne_kamera():
    print("Du kannst die Kamera nicht öffnen.")

@when("kamera benutzen", context="room1")
@when("benutze kamera", context="room1")
@when("benutzen kamera", context="room1")
def benutze_kamera():
    global sicherheitstuer_offen
    global problem_gesichtsscan
    global gesichtsscan_erfolgreich
    global gesichtsscan_erforderlich
    if (sicherheitstuer_offen == True):
        print("Die Sicherheitstür ist schon offen. Du brauchst das Tastenfeld nicht mehr zu benutzen.")
    elif (gesichtsscan_erfolgreich == True):
        print("Das Gesichtsscan war erfolgreich. Ich sollte den PIN auf dem Tastenfeld eingeben.")
    elif (gesichtsscan_erforderlich == False):
        print("Die Kamera ist scheinbar nicht aktiviert.")
    else:
        while 1:
            print("Du hast folgende Optionen. Bitte Nummer wählen:")
            print("(1) eigenes Gesicht scannen")
            if (inventory.find("foto_herr_solar") is not None):
                print("(2) Foto vom Herrn Solar auf Smartphone benutzen")
            option = input("")
            if (option == "2"):
                say("""„Guten Tag Herr Solar! Bitte geben Sie Ihren PIN ein!“, ertönt eine roboterartige Stimme aus dem Terminal. Dir fällt ein Stein vom Herzen, dass dieses System so alt ist, dass solch einfache Präsentationsangriffe funktionieren.""")
                gesichtsscan_erfolgreich = True
                gesichtsscan_erforderlich = False
                break
            if (option == "1"):
                print("Fehler: Gesicht unbekannt. Vorgang wird abgebrochen!")
                problem_gesichtsscan = True
                gesichtsscan_erforderlich = False
                print("Wessen Gesicht könnte wohl im System hinterlegt sein?")
                break

### Personen Raum 1 ###
# rede mit ist gleich benutzen
# Ministerin Schrader, Herr Solar, Fernsehteam
# alle Funktionen mit context="room1", falls die noch in andere Räume wandern, dann bitte anpassen

# Ministerin Schrader anschauen nehmen benutzen/reden öffnen, kein verwende mit

@when("ministerin schrader anschauen", context="room1")
@when("schaue ministerin schrader an", context="room1")
@when("ministerin schrader", context="room1")
@when("schrader anschauen", context="room1")
@when("schaue schrader an", context="room1")
@when("schrader", context="room1")
@when("ministerin anschauen", context="room1")
@when("schaue ministerin an", context="room1")
@when("ministerin", context="room1")
def zeige_schrader():
    global problem_smartphone_oeffnen
    say("""Dies ist [Ministerin Schrader] vom BMI. Sie sollte heute das letzte deutsche AKW abschalten. Dieses feierliche Ereigniss sollte vom [Fernsehteam] für die Nachrichten festgehalten werden. Dazu hat sie sich extra eine Hochsteckfrisur stylen lassen. Als Ministerin ist sie eine intelligente Person und kann dir sicherlich bei dem einen oder anderen Problem weiterhelfen ;-)""")
    if (problem_smartphone_oeffnen == True and inventory.find("haarnadel") is None):
        say("""Nun fallen dir die feinen Haarnadeln in ihrer Frisur auf. Vielleicht könntest du eine bekommen?""")
    say("""Du kannst mit [Ministerin Schrader reden].""")

@when("ministerin schrader nehmen", action = "nehmen", context="room1")
@when("nimm ministerin schrader", action = "nehmen", context="room1")
@when("nehmen ministerin schrader", action = "nehmen", context="room1")
@when("nehme ministerin schrader", action = "nehmen", context="room1")
@when("ministerin schrader öffnen", action = "öffnen", context="room1")
@when("öffnen ministerin schrader", action = "öffnen", context="room1")
@when("öffne ministerin schrader", action = "öffnen", context="room1")
@when("ministerin nehmen", action = "nehmen", context="room1")
@when("nimm ministerin", action = "nehmen", context="room1")
@when("nehmen ministerin", action = "nehmen", context="room1")
@when("nehme ministerin", action = "nehmen", context="room1")
@when("ministerin öffnen", action = "öffnen", context="room1")
@when("öffnen ministerin", action = "öffnen", context="room1")
@when("öffne ministerin", action = "öffnen", context="room1")
@when("schrader nehmen", action = "nehmen", context="room1")
@when("nimm schrader", action = "nehmen", context="room1")
@when("nehmen schrader", action = "nehmen", context="room1")
@when("nehme schrader", action = "nehmen", context="room1")
@when("schrader öffnen", action = "öffnen", context="room1")
@when("öffnen schrader", action = "öffnen", context="room1")
@when("öffne schrader", action = "öffnen", context="room1")
def schrader(action):
    print(f"Du kannst [Ministerin Schrader] nicht {action}!")

@when("ministerin schrader reden", context="room1")
@when("rede ministerin schrader", context="room1")
@when("rede mit ministerin schrader", context="room1")
@when("reden ministerin schrader", context="room1")
@when("ministerin reden", context="room1")
@when("rede ministerin", context="room1")
@when("rede mit ministerin", context="room1")
@when("reden ministerin", context="room1")
@when("schrader reden", context="room1")
@when("rede schrader", context="room1")
@when("rede mit schrader", context="room1")
@when("reden schrader", context="room1")
@when("ministerin schrader benutzen", context="room1")
@when("benutze ministerin schrader", context="room1")
@when("benutzen ministerin schrader", context="room1")
@when("ministerin benutzen", context="room1")
@when("benutze ministerin", context="room1")
@when("benutzen ministerin", context="room1")
@when("schrader benutzen", context="room1")
@when("benutze schrader", context="room1")
@when("benutzen schrader", context="room1")
def rede_schrader():
    global sicherheitstuer_offen
    global problem_gesichtsscan
    global gesichtsscan_erfolgreich
    global kontrollrechner_neugestartet
    global problem_smartphone_oeffnen
    print("Du beginnst ein Gespräch mit [Ministerin Schrader]")
    while 1:
            print("\nDu hast folgende Optionen:")
            print("- Über [nichts] reden (Gespräch beenden)")
            if (sicherheitstuer_offen == False and problem_gesichtsscan == True and gesichtsscan_erfolgreich == False):
                print("- [Gesichtsscan]")
            if (sicherheitstuer_offen == False and gesichtsscan_erfolgreich == True):
                print("- [PIN] von Herr Solar")
            if (kontrollrechner_neugestartet == False):
                print("- [Ransomware]")
            if (problem_smartphone_oeffnen == True and inventory.find("haarnadel") is None):
                print("- [Haarnadel]")
            option = input("")
            if (option == "nichts"):
                say("""Du möchtest nicht weiter reden. Dann vielleicht ein anderes Mal.""")
                break
            if (option == "gesichtsscan"):
                say("""Vielleicht kann man dieses uralte System mit einem Präsentationsangriff (Foto) überlisten?""")
            if (option == "pin"):
                say("""Den PIN von Herrn Solar weiß ich auch nicht. Aber meistens wird ja eine Zahlenkombination benutzt, die man nicht vergisst, wie ein Geburtstag.""")
            if (option == "ransomware"):
                say("""Wie kann man nur ein AKW überfallen und Lösegeld verlangen? Haben die nicht an die Folgen gedacht??? Vielleicht ist die Ransomeware nicht persistent und liegt nur im RAM. Dann würde eine Neustart des Computers helfen.""")
            if (option == "haarnadel"):
                say("""Du fragst sie, ob du dir ihre Haarnadel kurz ausleihen kannst. Sie nickt aufgeregt und übergibt sie dir schnell.""")
                inventory.add(haarnadel)
# weitere Hilfen einbauen, wenn man nicht weiter kommt.

# Herr Solar anschauen nehmen benutzen/reden öffnen, kein verwende mit

@when("herr solar anschauen", context="room1")
@when("schaue herr solar an", context="room1")
@when("herr solar", context="room1")
@when("solar anschauen", context="room1")
@when("schaue solar an", context="room1")
@when("solar", context="room1")
def zeige_solar():
    global herr_solar_wach
    print("Dies ist Herr Solar, der Chef vom hiesigen AKW.")
    if (herr_solar_wach == False):
        say("""Er ist derzeit ohnmächtig. [Ministerin Schrader] hat ihn in die stabile Seitenlage gebracht. Mehr kannst du aktuell auch nichts weiteres für ihn tun, aber vielleicht kannst du ihn irgendwie wecken.""")
    else:
        say("""Er ist inzwischen wach und sitzt sichtlich erschöpft auf dem Stuhl vor dem [Kontrollrechner] und schaut fassungslos auf die Erpresserbotschaft. Er ist noch etwas zerstreut, aber du kannst mit [Herr Solar reden].""")

@when("herr solar nehmen", action = "nehmen", context="room1")
@when("nimm herr solar", action = "nehmen", context="room1")
@when("nehmen herr solar", action = "nehmen", context="room1")
@when("nehme herr solar", action = "nehmen", context="room1")
@when("herr solar öffnen", action = "öffnen", context="room1")
@when("öffnen herr solar", action = "öffnen", context="room1")
@when("öffne herr solar", action = "öffnen", context="room1")
@when("solar nehmen", action = "nehmen", context="room1")
@when("nimm solar", action = "nehmen", context="room1")
@when("nehmen solar", action = "nehmen", context="room1")
@when("nehme solar", action = "nehmen", context="room1")
@when("solar öffnen", action = "öffnen", context="room1")
@when("öffnen solar", action = "öffnen", context="room1")
@when("öffne solar", action = "öffnen", context="room1")
def solar(action):
    print(f"Du kannst [Herr Solar] nicht {action}!")

@when("herr solar reden", context="room1")
@when("rede herr solar", context="room1")
@when("rede mit herr solar", context="room1")
@when("reden herr solar", context="room1")
@when("solar reden", context="room1")
@when("rede solar", context="room1")
@when("rede mit solar", context="room1")
@when("reden solar", context="room1")
@when("herr solar benutzen", context="room1")
@when("benutze herr solar", context="room1")
@when("benutzen herr solar", context="room1")
@when("solar benutzen", context="room1")
@when("benutze solar", context="room1")
@when("benutzen solar", context="room1")
def rede_solar():
    global herr_solar_wach
    global hinweis_wartungsklappe
    global wartungsklappe_offen
    if (herr_solar_wach == False):
        print("Er ist derzeit ohnmächtig. Er reagiert nicht auf deine Worte.")
    else:
        print("Du beginnst ein Gespräch mit [Herr Solar]")
        while 1:
            print("\nDu hast folgende Optionen:")
            print("- Über [nichts] reden (Gespräch beenden)")
            if (wartungsklappe_offen == False):
                print("- [Bedienung] Kontrollrechner ohne Eingabegerät")
            option = input("")
            if (option == "nichts"):
                say("""Du möchtest nicht weiter reden. Dann vielleicht ein anderes Mal.""")
                break
            if (option == "bedienung"):
                say("""Du fragst ihn, wie denn der [Kontrollrechner] bedient wird, so ganz ohne Eingabegeräte. Er weiß es leider auch nicht. Dafür erinnert er sich an ein Gespräche mit dem Bediener. Dieser hatte über Knieschmerzen geklagt, weil er immer unter das Terminal vom Kontrollrechner kriechen musste, wenn der Touchscreen ausfiel.""")
                hinweis_wartungsklappe = True

# Fernsehteam anschauen nehmen benutzen/reden öffnen, kein verwende mit
# Hinweis Scooter
# Hinweis Maschinenraum

@when("fernsehteam anschauen", context="room1")
@when("schaue fernsehteam an", context="room1")
@when("fernsehteam", context="room1")
def zeige_fernsehteam():
    print("In der steht das Fernsehteam gelangweilt herum. Du kannst mit ihnen [reden].")

@when("fernsehteam nehmen", action = "nehmen", context="room1")
@when("nimm fernsehteam", action = "nehmen", context="room1")
@when("nehmen fernsehteam", action = "nehmen", context="room1")
@when("nehme fernsehteam", action = "nehmen", context="room1")
@when("fernsehteam öffnen", action = "öffnen", context="room1")
@when("öffnen fernsehteam", action = "öffnen", context="room1")
@when("öffne fernsehteam", action = "öffnen", context="room1")
def fernsehteam(action):
    print(f"Du kannst das [Fernsehteam] nicht {action}!")

@when("fernsehteam reden", context="room1")
@when("rede fernsehteam", context="room1")
@when("rede mit fernsehteam", context="room1")
@when("reden fernsehteam", context="room1")
@when("fernsehteam benutzen", context="room1")
@when("benutze fernsehteam", context="room1")
@when("benutzen fernsehteam", context="room1")
def rede_fernsehteam():
    global kontrollrechner_neugestartet
    global sicherheitstuer_offen
    global hinweis_maschinenraum
    print("Du beginnst ein Gespräch mit dem [Fernsehteam]")
    while 1:
            print("\nDu hast folgende Optionen:")
            print("- Über [nichts] reden (Gespräch beenden)")
            if (sicherheitstuer_offen == False):
                print("- Herr [Solar]")
            if (kontrollrechner_neugestartet == True and hinweis_maschinenraum == False):
                print("- Problem mit den [Pumpen]")
            option = input("")
            if (option == "nichts"):
                say("""Du möchtest nicht weiter reden. Dann vielleicht ein anderes Mal.""")
                break
            if (option == "solar"):
                say("""Ihr kommt ins Gespräch über den AKW Chef. Das Team hat auf dem Weg durch das Kraftwerk lange mit ihm gesprochen. Dabei hat er viel von Sooter erzählt und das er wohl deren größter Fan ist, was ja auch kein Wunder ist. Denn er ist am gleichen Tag geboren wie deren Frontmann.""")
            if (option == "pumpen"):
                say("""Du fragst nach einer Idee, wie man die Pumpen wieder starten könnte. Ein Neustart des Kontrollrechners hat leider nicht funktioniert. Dieser zeigt immer noch nur die Erpresserbotschaft an. Das Team hat schon viel gedreht und viele Filme geschaut. Im Film wird meist im Notfall in den Maschinenraum gegangen und alles von Hand gesteuert.""")
                say(""""Gute Idee" denkst du, auf zum Maschinenraum!""")
                hinweis_maschinenraum = True

### Ende Raum 1 ####

#########################
# RAUM 2: MASCHINENRAUM #
#########################
@when("umschauen", context="room2")
@when("schaue um", context="room2")
@when("schau dich um", context="room2")
def look_around_room2():
    say("""Du befindest dich im Maschinenraum und entdeckst die Pumpenventile der riesigen Kühlpumpen und einen Zettel auf einem Tisch in der Nähe. Die Ventile scheinen beschriftet zu sein. Bestimmt muss eine Reihenfolge eingehalten werden.""")

def ueberleitung_room2():
    say("""---------------------------------------------------------------------------------""")
    say("""Sehr gut. Du konntest die Sicherheitstür öffnen und rennst so schnell du kannst los. Dabei folgst du stur dem Warnsignal, welches dich direkt zum Maschinenraum führt, während es immer lauter wird.""")
    input("...")
    say("""Beim Betreten des Raums nimmst du eine Durchsage einer Computerstimme aus den Lautsprechern wahr: „Noch 20 Minuten bis zur Kernschmelze!“ Die vielen blinkenden Lichter vor Ort werden alle von dem immer noch rot-pulsierenden Licht überdeckt. Das laute Brummen der großen Maschinen ist ohrenbetäubend. Mittig im Raum stehen 5 riesige Pumpen. „Das müssen sie sein!“ Vorsichtshalber ziehst du das Netzwerkkabel des Kontrollrechners des Kühlsystems. Die Hacker dürften jetzt wenigstens keinen Zugriff mehr darauf haben. Was nun?""")
    say("""""")






### Ende der Raume ### nun nur noch Debug und der Start-Aufruf

# Debug #


@when("debugraum")
def debug():
    global room_number
    print("RAUMNAMEN GENAU EINGEBEN!")
    print("1,2,3,4,5,6")
    debug_input = input("In welchen Raum springen? ")
    if debug_input == "1":
        set_context("room1")
        room_number = 1
    elif debug_input == "2":
        room_number = 2
        set_context("room2")
    elif debug_input == "3":
        room_number = 3
        set_context("room3")
    elif debug_input == "4":
        room_number = 5
        set_context("room4")
    elif debug_input == "5":
        room_number = 5
        set_context("room5")
    elif debug_input == "6":
        room_number = 6
        set_context("room6")


@when("debugitem")
def debug2():
    print("ITEMNAMEN GENAU EINGEBEN!")
    print("brecheisen, smartphone, haarnadel, simkarte, foto_herr_solar")
    debug_input = input("Welches ITEM hinzufügen: ")
    if debug_input == "brecheisen":
        inventory.add(brecheisen)
    elif debug_input == "smartphone":
        inventory.add(smartphone)
    elif debug_input == "haarnadel":
        inventory.add(haarnadel)
    elif debug_input == "simkarte":
        inventory.add(simkarte)
    elif debug_input == "foto_herr_solar":
        inventory.add(foto_herr_solar)

@when("debugstatus")
def debug3():
    global herr_solar_wach
    print("STATUS GENAU EINGEBEN!")
    print("herr_solar_wach")
    debug_input = input("Welche STATUS ändern: ")
    if debug_input == "herr_solar_wach":
        if (herr_solar_wach == False):
            herr_solar_wach = True
            print("Herr Solar ist nun wach")
        else:
            herr_solar_wach = False
            print("Herr Solar ist wieder ohnmächtig")


## start ###

### Startumgebung festlegen ###
inventory.add(smartphone)
set_context("room1")
room_number = 1

start()
# start(help = False) um den Help Befehl auszuschalten

