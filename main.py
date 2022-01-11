def printChoices(choice1, choice2=False, choice3=False, choice4=False, choice5=False):
    print(">" + choice1)
    if choice2 != False:
        print(">" + choice2)
    if choice3 != False:
        print(">" + choice3)
    if choice4 != False:
        print(">" + choice4)
    if choice5 != False:
        print(">" + choice5)

def room1():
    print("Der Kontroll-Rechner reagiert nicht auf Eingaben.")
    printChoices("Axt benutzen", "Tastenkombinationen ausprobieren", "USB-Tastatur anschließen", "System neustarten")
    input_1 = input()
    if input_1 == "Axt benutzen" or input_1 == "1":
        print("Der Rechner ist nun kaputt. Du musst eine andere Lösung finden.")
    if input_1 == "Tastenkombination ausprobieren" or input_1 == "2":
        print("Nichts geschieht.")
    if input_1 == "USB-Tastatur anschließen" or input_1 == "3":
        print("Du hast die Tastatur heute leider nicht dabei.")
    if input_1 == "System neustarten" or input_1 == "4":
        print("Selbst der Neustart hat nichts geändert.")
    

#def room2():

#def room3():

#def room4():

#def room5():


###main###
room1()
