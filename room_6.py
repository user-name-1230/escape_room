########################
# RAUM 6: KONTROLLRAUM #
########################

# imports
import time
from adventurelib import when, say, set_context
import sys
from termcolor import colored


# global vars
klappe_gesehen = False
klappe_offen = False
kontrollrechner_entsperrt = False
firewall_gesehen = False
zettel_gesehen = False
help_counter_room6 = 0

# objects
zettel = colored("Zettel", "yellow", attrs=["underline"])
wartungsklappe = colored("Wartungsklappe", "yellow", attrs=["underline"])
tastatur = colored("Tastatur", "yellow", attrs=["underline"])
firewall = colored("Firewall", "yellow", attrs=["underline"])

def ueberleitung_room6():
    time.sleep(2.0)
    say(
        colored(
            """---------------------------------------------------------------------""",
            "yellow"
        )
    )
    say(
        colored(
            """Du konntest tatsächlich das Passwort entschlüsseln. Jetzt aber schnell
            zurück zum Kontrollrechner und die Kühlpumpen wieder hochfahren. Ihr lauft
            gemeinsam los und betretet den Kontrollraum durch die Sicherheitstür.
            Du wendest dich direkt dem Rechner zu. Verdammt...wo ist die Tastatur?
            Es gibt keine Eingabemöglichkeit. Die Tastaturen der anderen Rechner
            würden nicht funktionieren. Die haben alle einen USB-Anschluss.""",
            "yellow"
        )
    )
    set_context("room6")


@when("umschauen", context="room6")
@when("schau um", context="room6")
@when("schau dich um", context="room6")
@when("umsehen", context="room6")
@when("um", context="room6")
def look_around_room6():
    global klappe_gesehen
    if firewall_gesehen:
        say(
            colored(
                """In einer Ecke des Kontrollpultes liegt ein """, "yellow") + zettel + colored(""". Vielleicht
                hilft dir dieser ja weiter.""",
                "yellow"
            )
        )
    elif klappe_gesehen:
        say(
            colored(
                """Leider liegt im Raum nichts mehr herum, womit du die Klappe aufbekommen könntest.""",
                "yellow"
            )
        )
    else:
        say(
            colored(
                """Du schaust dich fragend um. Der Kraftwerkchef kommt auf euch zu und
                fragt nach dem Status. Ihr erläutert ihm kurz das Problem und er zeigt auf
                eine """, "yellow") + wartungsklappe + colored(""" neben dem Kontrollpult. Dort muss eine Tastatur drin
                sein, die mit dem alten DIN-AT-Anschluss kompatibel ist. Doch die Klappe
                ist so verrostet, dass du sie mit bloßen Händen nicht aufbekommst.""",
                "yellow"
            )
        )
        klappe_gesehen = True


@when("klappe anschauen", context="room6")
@when("wartungsklappe anschauen", context="room6")
@when("klappe an", context="room6")
@when("wartungsklappe an", context="room6")
@when("klappe öffnen", context="room6")
@when("wartungsklappe öffnen", context="room6")
def klappe_oeffnen():
    if klappe_offen:
        say(colored("""Die Wartungsklappe ist bereits geöffnet.""","yellow"))
    else:
        say(
            colored(
                """Die Wartungsklappe ist leider so verrostet, dass man sie mit
                bloßen Händen nicht aufbekommt.""",
                "yellow"
            )
        )


@when("zettel nehmen", context="room6")
@when("zettel anschauen", context="room6")
@when("zettel an", context="room6")
@when("zettel anzeigen", context="room6")
def zettel_anschauen2():
    say(colored("""                  2022:                   """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" ORP.3.A7                |    5 '...-...' """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" APP.3.4         | 2.2   |   14           """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" G 0.28                  |   19 + 'ern'   """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" ISMS.1.A11              |    4           """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" OPS.1.1.4.A14           |    5           """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    say(colored(""" SYS.2.1.A1              |    5           """, "grey", "on_white"))
    say(colored("""                                          """, "grey", "on_white"))
    global zettel_gesehen
    zettel_gesehen = True



@when("benutze brecheisen", context="room6")  # brecheisen, benutzen
@when("benutz brecheisen", context="room6")
@when("brecheisen benutzen", context="room6")
@when("nutze brecheisen", context="room6")  # brecheisen, nutzen
@when("nutz brecheisen", context="room6")
@when("brecheisen nutzen", context="room6")
@when("nutze brechstange", context="room6")  # brechstange, benutzen
@when("nutz brechstange", context="room6")
@when("benutze brechstange", context="room6")
@when("benutz brechstange", context="room6")
@when("brechstange benutzen", context="room6")  # brechstange, nutzen
@when("brechstange nutzen", context="room6")
@when("mit brecheisen öffnen", context="room6")
@when("klappe mit brecheisen öffnen", context="room6")
@when("wartungsklappe mit brecheisen öffnen", context="room6")
@when("mit brechstange öffnen", context="room6")
@when("klappe mit brechstange öffnen", context="room6")
@when("wartungsklappe mit brechstange öffnen", context="room6")
def brecheisen_benutzen3():
    global klappe_offen
    klappe_offen = True
    say(
        colored(
            """Gut, dass du das Brecheisen vom Anfang noch bei dir hast. Du brichst
            die Klappe auf und dahinter versteckt sich tatsächlich eine passende """,
            "yellow") + tastatur + colored(""".""",
            "yellow"
        )
    )


@when("tastatur nehmen", context="room6")
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
        say(
            colored(
                """Du nimmst die Tastatur und steckst sie an den alten Kontrollrechner an.""",
                "yellow"
            )
        )
        say("""""")
        while (True):
            input_tastatur = input(colored("Passwort eingeben: ", "white", "on_grey"))
            if input_tastatur == "30JahreBSI1991!":
                say(colored("""...""", "yellow"))
                time.sleep(4.0)
                say("""""")
                say(
                    colored(
                        """Du tippst das Passwort ein: 3...0...J...a...h...r...e...B...S...I...1...9...9...1...!\n
                        ENTER!\n""",
                        "yellow"
                    )
                )
                time.sleep(5.0)
                say("""""")
                say(
                    colored(
                        """Der Totenkopf verschwindet. Du hast es geschafft. Doch dir fällt
                        etwas ein: „Wir müssen irgendetwas tun, um die Hacker aus dem
                        System zu werfen und das System besser.aBSIchern!“, rufst du.
                        Du wendest dich wieder dem Kontrollrechner zu um dir den Status
                        der """, "yellow") + firewall + colored(""" anzuschauen.""",
                        "yellow"
                    )
                )
                global kontrollrechner_entsperrt
                kontrollrechner_entsperrt = True
                return
            elif input_tastatur == "exit":
                return
            else:
                say(colored("""Falsches Passwort. Tippe "exit" um abzubrechen.""", "red"))
    else:
        say(
            colored(
                """Du hast leider keine passende Tastatur mit DIN-AT-Anschluss parat!""",
                "yellow"
            )
        )


@when("firewall anschauen", context="room6")
@when("firewall an", context="room6")
@when("status anschauen", context="room6")
@when("status an", context="room6")
@when("status firewall", context="room6")
@when("status der firewall anschauen", context="room6")
@when("status der firewall anzeigen", context="room6")
@when("firewall reparieren", context="room6")
@when("firewall schließen", context="room6")
@when("lücken schließen", context="room6")
def firewall_schliessen():
    if kontrollrechner_entsperrt:
        global firewall_gesehen
        firewall_gesehen = True
        print(colored(
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

                """, "red"))
        say(
            colored(
                """Ohje...jede Menge Lücken! Wir müssen irgendetwas tun, um die Lücken
                zu schließen:""",
                "yellow"
            )
        )
        say("""""")
        loesungen = [
            "IT-GRUNDSCHUTZ: DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN!", # mit allen Satzzeichen
            "IT-Grundschutz: Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzen!",
            "it-grundschutz: den einstieg meistern und sicherheitskonzepte mit mehrwert nutzen!",
            "IT-GRUNDSCHUTZ: DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN", # ohne !
            "IT-Grundschutz: Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzen",
            "it-grundschutz: den einstieg meistern und sicherheitskonzepte mit mehrwert nutzen",
            "IT-GRUNDSCHUTZ DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN", # ohne : und !
            "IT-Grundschutz Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzen",
            "it-grundschutz den einstieg meistern und sicherheitskonzepte mit mehrwert nutzen",
            "IT GRUNDSCHUTZ DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN", # ohne Satzzeichen
            "IT Grundschutz Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzen",
            "it grundschutz den einstieg meistern und sicherheitskonzepte mit mehrwert nutzen",
        ]
        while (True):
            input_loesung = input(colored(
                "Richtigen Satz eingeben ([zurück] um zurückzugehen): ", "red"))
            if (input_loesung in loesungen):
                print_loesung_firewall()
                time.sleep(4.0)
                abspann()
            elif input_loesung == "exit":
                return
            else:
                say(
                    colored(
                        """Das ist leider die falsche Antwort. Die Firewall ist
                        immer noch offen. Hast du eventuell etwas überesehen?""",
                        "yellow"
                    )
                )


def print_loesung_firewall():
    print(colored(
        r"""
+---------------+---------------+-----------------------+---------------+
|               |               |                       |               |
|       IT      |       -       |       GRUNDSCHUTZ     |       :       |
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

            """, "green"))


def abspann():
    say(
        colored(
            """Super. Du hast die Angreifer ausgesperrt und die Lücken in der
            Firewall geschlossen. Ab hier übernimmt der Kraftwerkchef. In letzter
            Sekunde fährt er über den Kontrollrechner die Pumpen des Kühlsystems wieder
            hoch. Das rote Notlicht erlischt und das Warnsignal aus dem Maschinenraum
            ist auch nicht mehr zu hören. GESCHAFFT!""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
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
            Das DACS-Praktikantenteam\n""",
            "yellow"
        )
    )
    say("""""")
    say("""""")
    input(colored("[Abenteuer beenden...]", "yellow"))
    say("""""")
    sys.exit()


@when("hilfe", context="room6")
@when("help", context="room6")
def help_room6():
    if firewall_gesehen and zettel_gesehen:
        global help_counter_room6
        if help_counter_room6 == 0:
            say(
                colored(
                    """Guck dir den """, "yellow") + zettel + colored(""" noch einmal genau an. Das sieht doch
                    aus wie Anforderungs-Bausteine aus dem IT-Grundschutz-Kompendium...
                    doch was haben die Zahlen dahinter zu bedeuten?""",
                    "yellow"
                )
            )
            help_counter_room6 += 1
        elif help_counter_room6 == 1:
            say(
                colored(
                    """Die Zahlen könnten doch für ein Wort in dem angegebenen
                    Anforderungs-Abschnitt stehen. Nur der zweite und dritte Punkt
                    auf dem Zettel weicht etwas von den anderen ab.""",
                    "yellow"
                )
            )
        else:
            say(
                colored(
                    """Beim zweiten Wort ist keine Anforderung des Bausteins angegeben.
                    Allerdings ein Gliederungspunkt.
                    Der dritte Punkt sieht aus wie eine Elementare Gefährdung.
                    Schau dir diese Sachen noch einmal genau im Kompendium an.""",
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
