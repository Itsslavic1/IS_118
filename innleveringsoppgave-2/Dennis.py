# Interaktiv historie – Erling som prosjektleder
# Basert på poengsystem fra storyline-diagrammene.

def hent_valg(tekst):
    """Sikrer at brukeren kun kan skrive a eller b."""
    while True:
        valg = input(tekst).strip().lower()
        if valg in ("a", "b"):
            return valg
        print("Ugyldig valg. Vennligst skriv A eller B.")

# --- INITIALISERING ---
# Vi bruker en integer (heltall) for å telle poeng. Starter på 0.
total_poeng = 0 

print("\n=== PROSJEKTLEDER ERLING ===")
print("Dine valg gir 1 poeng (relasjon) eller 2 poeng (fremdrift).")
print("Total poengsum (3-6) avgjør prosjektets skjebne.\n")
print("-" * 40)


# ----------------------------------------------------------------------
# BESLUTNING 1: Konflikt mellom Sivert og Silje [cite: 338]
# ----------------------------------------------------------------------
print("SITUASJON 1: Konflikt om design vs. sikkerhet (Personkonflikt).")
print("Velg den beste metoden for å håndtere spenningen.")
print("\n[A] DIALOG (1 poeng): Åpen diskusjon for felles løsning. Tids-krevende.")
print("[B] AVSTEMNING (2 poeng): Rask avgjørelse. Risikerer å overkjøre Silje.")

valg_1 = hent_valg("\nDitt valg (A/B): ")

if valg_1 == 'a':
    total_poeng += 1 # 1 poeng [cite: 333]
    print("\n--> KONSEKVENS (1 poeng): Møtet tok tid, men luften renses. Teamet får bedre felles forståelse.")
else:
    total_poeng += 2 # 2 poeng [cite: 339]
    print("\n--> KONSEKVENS (2 poeng): Løsningen ble raskt avklart, men Silje trekker seg tilbake. Relasjonen er sårbar.")

print(f"Total poengsum så langt: {total_poeng} poeng.")
print("-" * 40)


# ----------------------------------------------------------------------
# BESLUTNING 2: Konflikt mellom Hamdi og Jabir [cite: 347]
# ----------------------------------------------------------------------
print("SITUASJON 2: Uenighet om digitale folkemøter (Ulmende konflikt).")
print("Du må avklare uenigheten før den blusser opp.")
print("\n[A] MINI-PROSJEKT (1 poeng): Kort, felles oppgave for å bygge rask tillit.")
print("[B] VINN-VINN FORHANDLING (2 poeng): Grundig dialog for varig, felles løsning. Tids-krevende.")

valg_2 = hent_valg("\nDitt valg (A/B): ")

if valg_2 == 'a':
    total_poeng += 1 # 1 poeng [cite: 344]
    print("\n--> KONSEKVENS (1 poeng): De når målet og finner tonen. Konflikten er dempet, men årsaken kan ulme i bakgrunnen.")
else:
    total_poeng += 2 # 2 poeng [cite: 350]
    print("\n--> KONSEKVENS (2 poeng): Dere fant en sterk hybrid løsning. Veldig solid samarbeid, men prosessen stjal tid fra fremdrift.")

print(f"Total poengsum så langt: {total_poeng} poeng.")
print("-" * 40)


# ----------------------------------------------------------------------
# BESLUTNING 3: Teamets motivasjon [cite: 356]
# ----------------------------------------------------------------------
print("SITUASJON 3: Teamet er slitent etter konfliktene.")
print("Du må velge hvordan du gjenoppretter energien.")
print("\n[A] SOSIAL SAMLING (1 poeng): Team-building for å senke stress og bygge teamfølelse.")
print("[B] TYDELIGE MÅL (2 poeng): Sett strenge delmål og struktur for å øke effektiviteten.")

valg_3 = hent_valg("\nDitt valg (A/B): ")

if valg_3 == 'a':
    total_poeng += 1 # 1 poeng
    print("\n--> KONSEKVENS (1 poeng): Stressnivået synker, og teamet får en nødvendig boost i energi og motivasjon.")
else:
    total_poeng += 2 # 2 poeng
    print("\n--> KONSEKVENS (2 poeng): Arbeidet går fremover med bedre struktur. Mange føler seg likevel utslitte og mikrostyrt.")

print("-" * 40)
print(f"\n=== SLUTTRESULTAT ===\nDin totale poengsum: {total_poeng} poeng.")
print("-" * 40)


# ----------------------------------------------------------------------
# KONKLUSJON: Basert på poengsummen 
# ----------------------------------------------------------------------

# Resultat 1: Best - 3 poeng (3 poeng eller mindre)
if total_poeng <= 3:
    print("\n**RESULTAT 1: TILITEN GJENOPPRETTES OG TEAMET GÅR MOT NORMING-FASEN**")
    print("Du valgte relasjonsbygging og dialog (lav poengsum).")
    print("Konfliktene ble løst gjennom dialog, og motivasjon/trygghet er styrket[cite: 364].")
    print("Prosjektet leverer og utvikler bedre samspill[cite: 365].")

# Resultat 3: Dårligst - 6 poeng (6 poeng eller mer)
elif total_poeng >= 6:
    print("\n**RESULTAT 3: PROSJEKTET MISTER SAMHOLD OG BLIR FORSINKET**")
    print("Du valgte rask fremdrift og struktur (høy poengsum).")
    print("Fremdrift skjedde uten relasjonsbygging. Silje trakk seg tilbake, og kommunikasjonen er dårlig[cite: 370, 371].")
    print("Prosjektet forsinkes eller leveres med dårlig kvalitet[cite: 371, 407].")

# Resultat 2: Middels - 4 eller 5 poeng (4-5 poeng)
else: # total_poeng er 4 eller 5
    print("\n**RESULTAT 2: KONFLIKTENE ER DELVIS LØST, MEN RELASJONENE ER SÅRBARE**")
    print("Du fant en balanse mellom relasjon og fremdrift (middels poengsum).")
    print("Fremdrift ble oppnådd, men noen relasjoner forblir spente[cite: 367, 368].")
    print("Teamet fungerer, men med risiko for nye problemer når presset øker[cite: 368, 404].")
