while True:
    # ------------------------
    # Menu voor interactie
    # ------------------------
    print("\nKeuzemenu:")
    print("1. Waarde knop uitlezen")
    print("2. Led aan- / uitzetten")
    print("3. Programma stoppen")

    keuze = input("Maak een keuze: ")

    if keuze == "3":
        print("Programma stoppen...")
        exit()