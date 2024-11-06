import random

def vraag_geldig_getal(prompt="Voer een getal in: ", min_waarde=1):
    while True:
        try:
            waarde = int(input(prompt))
            if waarde >= min_waarde:
                return waarde
            else:
                print(f"Vul een geldig nummer in dat minimaal {min_waarde} is.")
        except ValueError:
            print("Vul een geldig nummer in.")


def start_spel():
    # Vraag om maximale waarde en aantal pogingen
    max_getal = vraag_geldig_getal("Tot en met welk getal wil je gokken? ")
    max_pogingen = vraag_geldig_getal("Hoeveel keer wil je mogen raden? ", min_waarde=1)

    #kiest een willekeurig getal tussen 1 en max_getal
    willekeurig_getal = random.randint(1, max_getal)

    print(f"Welkom bij het getallenspel! Je hebt {max_pogingen} pogingen om het getal van 1 tot en met {max_getal} te raden.")

    #for-loop voor het aantal pogingen
    for poging in range(1, max_pogingen + 1):
        gok = vraag_geldig_getal(f"Poging {poging}: Raad het getal: ", min_waarde=1)

        # Controleer de gok van de gebruiker
        if gok == willekeurig_getal:
            print(f"Gefeliciteerd! Je hebt het goed geraden! Het juiste getal was {willekeurig_getal}")
            return
        elif gok < willekeurig_getal:
            print("Het getal is hoger.")
        else:
            print("Het getal is lager.")

    #als de gebruiker alle pogingen heeft verbruikt zonder het getal te raden
    print(f"Helaas! Je hebt geen pogingen meer over. Het juiste getal was {willekeurig_getal}.")

#start
if __name__ == "__main__":
    start_spel()