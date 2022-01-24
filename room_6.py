########################
# RAUM 6: KONTROLLRAUM #
########################

# imports
import time
from adventurelib import when, say, set_context
import sys


# global vars
klappe_offen = False
kontrollrechner_entsperrt = False
firewall_gesehen = False


def ueberleitung_room6():
    time.sleep(6.0)
    say(
        colored(
            """---------------------------------------------------------------------------------""",
            "yellow"
        )
    )
    say(
        colored(
            """Ihr seid alle zurück im Kontrollraum angekommen. Du rennst zum
            Rechner. Verdammt...wo ist die Tastatur? Du findest keine Eingabemöglichkeit.
            Die Tastaturen der anderen Rechner würden nicht funktionieren. Die haben alle
            einen USB-Anschluss.""",
            "yellow"
        )
    )
    set_context("room6")


@when("umschauen", context="room6")
@when("schau um", context="room6")
@when("schau dich um", context="room6")
@when("umsehen", context="room6")
def look_around_room6():
    if firewall_gesehen:
        say(
            colored(
                """In einer Ecke des Kontrollpultes liegt ein Zettel. Vielleicht
                hilft dir dieser ja weiter.""",
                "yellow"
            )
        )
    else:
        say(
            colored(
                """Ihr schaut euch fragend um. Der Kraftwerkchef kommt auf euch zu und
                fragt nach dem Status. Ihr erläutert ihm kurz das Problem und er zeigt auf
                eine Wartungsklappe neben dem Kontrollpult. Dort muss eine Tastatur drin
                sein, die mit dem alten DIN-AT-Anschluss kompatibel ist. Doch die Klappe
                ist so verrostet, dass du sie mit bloßen Händen nicht aufbekommt.""",
                "yellow"
            )
        )


@when("zettel nehmen", context="room6")
@when("zettel anschauen", context="room6")
@when("zettel anzeigen", context="room6")
def zettel_anschauen2():
    say(
        colored("""
            ORP.3.A7                |   5\n
            APP.3.4         | 2.2   |   14\n
            ISMS.1.A11              |   4\n
            OPS.1.1.4.A14           |   5\n
            SYS.2.1.A1              |   5""",
            "grey", "on_white"
        )
    )


@when("brecheisen benutzen", context="room6")
@when("mit brecheisen öffnen", context="room6")
@when("brecheisen anwenden", context="room6")
@when("brecheisen verwenden", context="room6")
def brecheisen_benutzen3():
    global klappe_offen
    klappe_offen = True
    say(
        colored(
            """Gut, dass du das Brecheisen vom Anfang noch bei dir hast. Du brichst
            die Klappe auf und dahinter versteckt sich tatsächlich eine passende
            Tastatur.""",
            "yellow"
        )
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
    say(
        colored(
            """Du steckst die Tastatur an den alten Kontrollrechner an.""",
            "yellow"
        )
    )
    if klappe_offen:
        while (True):
            input_tastatur = input(colored("Passwort eingeben: ", "white", "on_grey"))
            if input_tastatur == "30JahreBSI1991!":
                say(
                    colored(
                        """Du tippst das Passwort ein: 3…0…J…a…h…r…e…B…S…I…1…9…9…1…!
                        ENTER!
                        Der Totenkopf verschwindet. Du hast es geschafft. Doch dir fällt
                        etwas ein: „Wir müssen irgendetwas tun, um die Hacker aus dem
                        System zu werfen und das System besser.aBSIchern!“, rufst du.
                        Du wendest dich wieder dem Kontrollrechner zu um dir den Status
                        der Firewall anzuschauen.""",
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

                """, "yellow"))
        say(
            colored(
                """Ohje…jede Menge Lücken! Wir müssen irgendetwas tun, um die Lücken
                zu schließen:""",
                "yellow"
            )
        )
        while (True):
            input_loesung = input(
                "Richtigen Satz eingeben (""exit"" um zurückzugehen): ")
            if (
                input_loesung == "IT-GRUNDSCHUTZ: DEN EINSTIEG MEISTERN UND SICHERHEITSKONZEPTE MIT MEHRWERT NUTZEN" or input_loesung == "IT-Grundschutz: Den Einstieg meistern und Sicherheitskonzepte mit Mehrwert nutzein"
            ):
                print_loesung_firewall()
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

            """, "yellow"))


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
            Das DACS-Praktikantenteam""",
            "yellow"
        )
    )
    sys.exit()
