# master.py
# Interaktiv historie – Erling som prosjektleder
# Basert på storyline fra oppgave 1

def start():
    print("Velkommen til prosjektspillet!")
    print("Du spiller som Erling, prosjektleder for et team som har flere ulmende konflikter.")
    print("Du må ta tre viktige valg som avgjør hvordan prosjektet ender.\n")

    # Første beslutning: Sivert og Silje
    valg1 = input("Konflikten mellom Sivert og Silje øker. Hva gjør du?\n"
                  "A: Samle teamet for åpen diskusjon og finne felles løsning.\n"
                  "B: Gjennomføre avstemning for å bestemme raskt.\n"
                  "Velg A eller B: ").lower()

    # Andre beslutning: Hamdi og Jabir
    valg2 = input("\nEn annen konflikt oppstår mellom Hamdi og Jabir. Hva gjør du?\n"
                  "A: Gi dem et lite delprosjekt sammen for å bygge tillit raskt.\n"
                  "B: Bruke tid på å finne en vinn-vinn-løsning gjennom dialog.\n"
                  "Velg A eller B: ").lower()

    # Tredje beslutning: Motivasjon i teamet
    valg3 = input("\nEtter en periode med konflikter er teamet slitent. Hva gjør du?\n"
                  "A: Arrangere en kort sosial samling for å senke stress og bygge trivsel.\n"
                  "B: Ha et strukturmøte og sette tydelige delmål for effektivitet.\n"
                  "Velg A eller B: ").lower()

    # Sluttresultater basert på kombinasjon av valg
    print("\n--- RESULTAT ---")

    # Endepunkt 1: Tillit gjenopprettes (dialog, vinn-vinn, sosial samling)
    if valg1 == "a" and valg2 == "b" and valg3 == "a":
        print("Teamet opplever åpenhet og gjensidig respekt. Konfliktene håndteres på en moden måte.")
        print("Silje og Sivert finner balansen mellom design og sikkerhet, Hamdi og Jabir samarbeider godt.")
        print("Den sosiale samlingen styrker tilliten, og teamet går inn i norming-fasen med ny energi.")
        print("Prosjektet leverer en solid prototype i tide. 🎉")

    # Endepunkt 2: Konfliktene delvis løst (rask avgjørelse, vinn-vinn, struktur)
    elif valg1 == "b" and valg2 == "b" and valg3 == "b":
        print("Prosjektet går fremover med god struktur, men relasjonene er fortsatt sårbare.")
        print("Silje føler seg overkjørt, selv om løsningen ble effektiv. Hamdi og Jabir finner balanse.")
        print("Teamet leverer i tide, men motivasjonen er lav. Prosjektet er 'godt nok', men uten entusiasme.")

    # Endepunkt 3: Prosjektet mister samhold (rask avgjørelse, kortsiktig tiltak, struktur)
    elif valg1 == "b" and valg2 == "a" and valg3 == "b":
        print("Du prioriterte raske løsninger og tydelige mål, men konfliktene blusser opp igjen.")
        print("Silje trekker seg unna, Hamdi og Jabir mistror hverandre, og motivasjonen stuper.")
        print("Prosjektet blir forsinket, og teamet sitter fast i storming-fasen. ⚠️")

    # Kombinasjon av blandede valg → Delvis positivt resultat
    else:
        print("Du håndterte noen konflikter godt, men andre fortsatt uløste.")
        print("Teamet klarte å levere, men stemningen er ustabil. Det er læringspotensial for neste prosjekt.")

    print("\nTakk for at du spilte! Vil du prøve igjen og se et annet utfall?")

# Kjører programmet
if __name__ == "__main__":
    start()
