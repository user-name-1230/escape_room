# TODO

# (Mehr möglichkeiten)



from termcolor import colored
import signal
import readchar
import time
import random
from adventurelib import when, say, start, set_context
import adventurelib
from inventory import *
import room_1


#Ctrl+C handler
def handler(signal_received, frame):
    msg = "Strg + C Eingabe wurde erkannt. Möchten Sie das Spiel wirklich beenden? [y/N] "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("")
        print("")
        print("Hinweis: Zum Kopieren von Inhalten den Rechtsklick verwenden.")
        print("")
        # print("", end="\r", flush=True)
        # print(" " * len(msg), end="", flush=True) # clear the printed line
        # print("    ", end="\r", flush=True)


signal.signal(signal.SIGINT, handler)


def no_command_matches(command):
    print(
        colored(
            random.choice([
                "Das habe ich nicht verstanden.",
                f"Ich verstehe '{command}' leider nicht.",
                "Tur mir leid, diese Aktion scheint nicht zur Verfügung zu stehen.",
                f"Tut mir leid, die Aktion '{command}' scheint nicht zur Verfügung zu stehen."
                ]
            ), "red"
        )
    )

adventurelib.no_command_matches = no_command_matches



# Start #
set_context("room0")

#print(colored("cmds for debug: debugraum, debugitem", "cyan"))
say(
    colored(
        """---------------------------------------------------------------------""",
        "yellow"
    )
)
say(
    colored(
        """Das Symbol [...] bedeutet, dass du Enter drücken sollst, um fortzufahren.\n
        Tipp: Mit einem größeren Terminal-Fenster spielt es sich leichter!\n
        Tippe "Start" ein, um zu beginnen""",
        "yellow"
    )
)



# Einleitungsstory
@when("start", context="room0")
def begin():
    say(
        colored(
            """---------------------------------------------------------------------""",
            "yellow"
        )
    )
    say(
        colored(
            """Einleitung: \n
            Zur feierlichen Abschaltung des letzten deutschen AKWs sind hochrangige Gäste
            eingeladen. Unter anderem das BMI und somit Ministerin Schrader. Du, als
            technischer Sachverständiger und IT-Spezialist darfst die Ministerin begleiten,
            welche den roten Knopf zur Abschaltung drücken soll. Der AKW-Chef Herr Solar
            führt Ministerin Schrader, das Fernsehteam und dich durch die Anlage. Nach
            einigen Minuten gelangt ihr in das Herzstück des AKWs – den Kontrollraum –
            welches sich hinter einer meterdicken Sicherheitstür befindet.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Ihr begebt euch gemeinsam zum Abschaltterminal. Über ein Mikrofon zählt
            Herr Solar den Countdown herunter. Die Journalisten außerhalb des Kraftwerks
            lauschen gespannt mit. Ministerin Schrader hat bereits die Hand auf dem großen
            roten Knopf, um das Kraftwerk vom Netz zu nehmen. 5...4...3...2........plötzlich völlige Dunkelheit.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Ihr hört ein lautes Surren und Klicken. Nach einer gefühlten Ewigkeit
            geht ein rot-pulsierendes Notlicht an und im Kontrollraum verhallt das
            Warnsignal aus dem Maschinenraum. Die Sicherheitstür wird mit einem Knall
            verriegelt. Der Bildschirm des Kontrollrechners leuchtet auf und ein Totenkopf
            erscheint mit folgender Mitteilung: "Die Evil Corp hat soeben das Kraftwerk
            übernommen. Wir haben das Kühlsystem der Brennstäbe gehackt und die Pumpen
            heruntergefahren.“""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(colored("""Ein Countdown startet: 30:00, 29:59, 29:58, ....""", "yellow"))
    say("""""")
    time.sleep(3.0)
    say(
        colored(
            """„Zur Entsperrung der Anlage müssen sie nur einen kleinen Betrag von
            100.000.000 Dogecoin auf die Wallet-Adresse einfach.aBSIchern überweisen.“""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Unter der Mitteilung erscheint ein Eingabefeld, welches mit "Encryption_Password"
            beschriftet ist. Na toll...Ransomware. Der Chef des Kraftwerks ist erschüttert und
            erklärt, dass es zu einer Kettenreaktion und letzten Endes zur Kernschmelze
            kommen wird, wenn die Kühlung länger als 30 Minuten stillsteht. Danach fällt er
            vor Schreck in Ohnmacht.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[...]", "yellow"))
    say("""""")
    say(
        colored(
            """Ministerin Schrader greift sofort zum Telefon um den
            Kanzler zu fragen, ob die Bezahlung eine Option darstellt. Aber sie hat keinen
            Empfang. Die Wände des Kontrollraums sind zu dick. Das Fernsehteam steht ratlos
            in der Ecke des Raumes. Du möchtest nicht warten und glaubst auch nicht, dass
            eine Bezahlung des Lösegelds wirksam ist. Also suchst du als einziger Anwesender
            mit breitem IT-Wissen - denn du hast ja DACS studiert ;) - nach einer
            Lösung.""",
            "yellow"
        )
    )
    say("""""")
    input(colored("[Abenteuer beginnen...]", "yellow"))

    #Start
    set_context("room1")
    room_1.ueberleitung_room1()



# Debug #

@when("debugraum")
def debug_room():
    debug_input = input(colored("In welchen Raum möchten Sie springen [1, 2, 3, 4, 5, 6]: ", "cyan"))
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
def debug_item():
    debug_input = input(colored("Welches ITEM hinzufügen [brecheisen, smartphone, haarnadel, simkarte]: ", "cyan"))
    if debug_input == "brecheisen":
        inventory.add(crowbar)
    elif debug_input == "smartphone":
        inventory.add(smartphone)
    elif debug_input == "haarnadel":
        inventory.add(hairpin)
    elif debug_input == "simkarte":
        inventory.add(sim)


# start
start()
