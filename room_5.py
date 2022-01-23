################
# RAUM 5: BÜRO #
################

#imports
from PIL import Image
import time
import random
from adventurelib import Room, when, say, start, Bag, Item, set_context
import sys
from room_6 import *
from inventory import *


#global vars
passwort_gefunden = False


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
                        cd       -   (ohne Eingabe) wechselt ins Home-Verzeichnis des aktuellen Nutzers"""
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
