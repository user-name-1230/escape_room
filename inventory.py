from adventurelib import when, Bag, Item

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
