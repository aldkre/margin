def calculate_values(zakup_netto=None, zakup_brutto=None, cena_brutto=None, VAT=0.23, marza=0.5):

    # --- walidacja wejścia ---
    provided = [zakup_netto, zakup_brutto, cena_brutto]
    if sum(v is not None for v in provided) != 1:
        raise ValueError("Podaj dokładnie jedną wartość: zakup_netto, zakup_brutto lub cena_brutto.")

    # --- obliczenia ---
    if zakup_netto is not None:
        zakup_brutto = zakup_netto * (1 + VAT)

    elif zakup_brutto is not None:
        zakup_netto = zakup_brutto / (1 + VAT)

    elif cena_brutto is not None:
        zakup_brutto = cena_brutto * (1 - marza)
        zakup_netto = zakup_brutto / (1 + VAT)

    # cena sprzedaży
    cena_brutto = zakup_brutto / (1 - marza)
    cena_netto = cena_brutto / (1 + VAT)

    zysk = cena_netto - zakup_netto

    return {
        'zakup netto': round(zakup_netto, 2),
        'zakup brutto': round(zakup_brutto, 2),
        'VAT': round(VAT * 100, 0),
        'marża brutto': round(marza * 100, 0),
        'zysk': round(zysk, 2),
        'cena netto': round(cena_netto, 2),
        'cena brutto': round(cena_brutto, 2)
    }
