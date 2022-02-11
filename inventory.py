from adventurelib import when, Bag, Item
from termcolor import colored

# Inventar #
crowbar = Item("brecheisen")
smartphone = Item("smartphone")
hairpin = Item("haarnadel")
sim = Item("simkarte")
inventory = Bag()


@when("inventar")
@when("inventar anschauen")  # anschauen
@when("inventar an")  # anschauen
@when("inventar zeigen")  # zeigen
@when("zeige inventar")
@when("inventar anzeigen")  # anzeigen
@when("anzeige des inventars")
@when("öffne inventar")  # öffnen
@when("inventar öffnen")
def zeige_inventar():
    print(colored("Du hast: ", "green"))
    if not inventory:
        print(colored("nichts", "green"))
        return
    for item in inventory:
        print(colored(f"*{item}", "green"))
