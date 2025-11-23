def hent_valg(sporsmal):
    """
    Spør brukeren om et valg og godtar bare 'a' eller 'b'.
    """
    while True:
        svar = input(sporsmal).strip().lower()
        if svar in ("a", "b"):
            return svar
        print("Ugyldig valg. Skriv a eller b og trykk Enter.\n")


def main():
    print("=== ERLING I STORMING-FASEN ===\n")
    print("Du spiller Erling, prosjektleder for den digitale medborgerportalen.")
    print("Teamet er i storming-fasen, og du må ta tre viktige valg.\n")

    # Beslutning 1: Sivert og Silje
    valg1 = hent_valg(
        "1) Konflikten mellom Sivert og Silje\n"
        "  a) Fellesmøte med åpen dialog\n"
        "  b) Kort diskusjon og avstemning\n"
        "Valg (a/b): "
    )

    if valg1 == "a":
        print("\nDu samler hele teamet. Konflikten blir tatt opp åpent.\n")
    else:
        print("\nDu velger avstemning. Saken avgjøres raskt, men stemningen er litt kjølig.\n")

    # Beslutning 2: Hamdi og Jabir
    valg2 = hent_valg(
        "2) Uenigheten mellom Hamdi og Jabir\n"
        "  a) Lite felles miniprosjekt med kort frist\n"
        "  b) Rolig samtale for å finne en kombinert løsning\n"
        "Valg (a/b): "
    )

    if valg2 == "a":
        print("\nDe får et miniprosjekt. Fokus er på å levere noe raskt.\n")
    else:
        print("\nDu setter av tid til en samtale. Begge får forklare seg grundig.\n")

    # Beslutning 3: Motivasjon i teamet
    valg3 = hent_valg(
        "3) Motivasjonen i teamet\n"
        "  a) Kort sosial pause med hele teamet\n"
        "  b) Stramt møte med mål og delmål\n"
        "Valg (a/b): "
    )

    if valg3 == "a":
        print("\nDere møtes uformelt. Folk prater mer avslappet.\n")
    else:
        print("\nDu kjører et strukturert møte. Planen blir tydelig, men presset øker.\n")

    print("=== SLUTT PÅ HISTORIEN ===\n")

    # Poengsystem: relasjonsorientert valg = +1, hardt/effektivitetsvalg = -1
    score = 0

    # valg1: a = dialog, b = avstemning
    if valg1 == "a":
        score += 1
    else:
        score -= 1

    # valg2: a = miniprosjekt (raskt), b = samtale (vinn-vinn)
    if valg2 == "b":
        score += 1
    else:
        score -= 1

    # valg3: a = sosialt tiltak, b = struktur og delmål
    if valg3 == "a":
        score += 1
    else:
        score -= 1

    # Bestem endepunkt basert på hvor relasjonsorientert Erling har vært totalt sett
    if score >= 2:
        print("SLUTT 1: TEAMET BEVEGER SEG MOT NORMING-FASEN\n")
        print(
            "I flere situasjoner har du valgt dialog, tid til samarbeid og tiltak som bygger trygghet.\n"
            "Konflikten mellom Sivert og Silje er ikke borte, men de forstår hverandre bedre og tar opp uenighet på en mer ryddig måte.\n"
            "Hamdi og Jabir opplever at de blir tatt på alvor, og motivasjonen i teamet får et løft.\n"
            "Teamet leverer prototypen innen fristen og er på vei ut av storming og inn i en tydeligere norming-fase.\n"
        )
    elif score <= -2:
        print("SLUTT 3: PROSJEKTET MISTER SAMHOLD OG BLIR FORSINKET\n")
        print(
            "Du har ofte valgt raske avklaringer, korte frister og stram styring.\n"
            "Silje føler seg overkjørt, Hamdi og Jabir får ikke ryddet ordentlig opp i uenigheten, "
            "og flere opplever mer press enn støtte.\n"
            "Tilliten svekkes, motivasjonen faller, og mer tid går med til friksjon enn til faktisk arbeid.\n"
            "Prototypen blir forsinket, og teamet blir værende i storming-fasen.\n"
        )
    else:
        print("SLUTT 2: KONFLIKTENE ER DELVIS LØST, MEN RELASJONENE ER SÅRBARE\n")
        print(
            "Du har gjort noen relasjonsorienterte valg, men også valg som først og fremst skulle spare tid og gi kontroll.\n"
            "Teamet klarer å jobbe videre og nærmer seg levering, men enkelte føler seg fortsatt litt overkjørt eller usikre.\n"
            "Prosjektet fungerer, men relasjonene er ikke helt stabile. Ved nytt press kan gamle konflikter lett dukke opp igjen.\n"
        )


if __name__ == "__main__":
    main()