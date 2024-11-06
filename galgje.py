import random

def laad_woorden(woorden):
   #laadt woorden uit het bestand en retourneert een lijst van woorden.
    with open(woorden, 'r') as file:
        woorden = file.read().splitlines()
    return woorden

def kies_willekeurig_woord(woorden):
    #kiest een willekeurig woord uit de woordenlijst.
    return random.choice(woorden)

def toon_status(woord, geraden_letters, pogingen_over):
    #toont de huidige status van het geraden woord en het aantal resterende pogingen
    toon_woord = ''.join([letter if letter in geraden_letters else '_' for letter in woord])
    print(f"Woord: {toon_woord}") #tussenstand
    print(f"Je hebt nog {pogingen_over} pogingen over.")
    print(f"Geraden letters: {', '.join(geraden_letters)}")

def vraag_geldige_letter(prompt):
    #vraagt de gebruiker om een geldige letter
    while True:
        gok = input(prompt).lower()
        if len(gok) == 1 and gok.isalpha():
            return gok
        else:
            print("Vul een enkele geldige letter in.")

def vraag_geldig_getal(prompt, min_waarde=1):
    #vraagt de gebruiker hoevaak hij wilt raden
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
    # Vraag de gebruiker om de naam en het aantal pogingen met validatie
    naam = input("Wat is je naam? ")
    max_pogingen = vraag_geldig_getal("Hoeveel keer wil je mogen raden? ", min_waarde=1)

    # Laad woorden en kies een willekeurig woord
    woorden = laad_woorden("woorden.txt")
    woord = kies_willekeurig_woord(woorden)

    #spelstatus
    geraden_letters = set()
    pogingen_over = max_pogingen
    print(f"\nWelkom, {naam}! Laten we galgje spelen.")

    #start raden
    while pogingen_over > 0:
        toon_status(woord, geraden_letters, pogingen_over)
        gok = vraag_geldige_letter("Raad een letter: ")

        # Controleer of de letter al geraden is
        if gok in geraden_letters:
            print(f"Je hebt de letter '{gok}' al geraden.")
        else:
            geraden_letters.add(gok)

            # Controleer of de geraden letter in het woord zit
            if gok in woord:
                print(f"Goed gedaan! De letter '{gok}' zit in het woord.")
                # Controleer of het hele woord geraden is
                if all(letter in geraden_letters for letter in woord):
                    print(f"Gefeliciteerd, {naam}! Je hebt het woord '{woord}' geraden!")
                    return
            else:
                print(f"Helaas, de letter '{gok}' zit niet in het woord.")
                pogingen_over -= 1

    #geen pogingen meer
    print(f"Je hebt geen pogingen meer over. Het woord was '{woord}'. Bedankt voor het spelen, {naam}!")

#start
if __name__ == "__main__":
    start_spel()