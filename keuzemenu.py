import Raadhetnummerv
import galgje8

def menu():
    print("\nWelkom bij Game Market!\n")
    print("Kies een spel om te spelen:")
    print("1. Nummer Raadspel")
    print("2. Galgje")
    print("3. Afsluiten\n")

    while True:
        try:
            keuze = int(input("Voer je keuze in (1, 2 of 3): "))
            if keuze in [1, 2, 3]:
                return keuze
            else: #cijfers
                print("\nVoer een geldige keuze in (1, 2 of 3).\n")
        except ValueError: #letters/symbolen
            print("\nVul een geldig nummer in (1, 2 of 3).\n")


def start_game_market():
    while True:
        keuze = menu()

        if keuze == 1:
            print("\nJe hebt gekozen voor het Nummer Raadspel!\n")
            Raadhetnummerv.start_spel()  #start
            print("\n")  #extra lege regel
        elif keuze == 2:
            print("\nJe hebt gekozen voor Galgje!\n")
            galgje8.start_spel()  #start
            print("\n")  #extra lege regel
        elif keuze == 3:
            print("\nBedankt voor het spelen! Tot ziens!\n")
            break

        #vragen of de speler terug wil naar het menu of wil afsluiten
        while True:
            verder_gaan = input("Wil je terug naar het hoofdmenu? (ja/nee): ").strip().lower()
            if verder_gaan in ['ja', 'nee']:
                break
            else:
                print("Voer 'ja' of 'nee' in.")

        if verder_gaan != 'ja':
            print("\nBedankt voor het spelen! Tot ziens!\n")
            break


# Start de Game Market
if __name__ == "__main__":
    start_game_market()