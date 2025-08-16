import pandas as pd

def calculate_values(zakup_netto=None, zakup_brutto=None, cena_brutto=None, VAT=0.23, marza=0.5):
    if zakup_netto is not None:
        zakup_brutto = zakup_netto * (1 + VAT)
    elif zakup_brutto is not None:
        zakup_netto = zakup_brutto / (1 + VAT)
    elif cena_brutto is not None:
        zakup_brutto = -(marza * cena_brutto - cena_brutto)
        zakup_netto = zakup_brutto / (1 + VAT)

    cena_netto = zakup_brutto / (1 - marza) / (1 + VAT)
    cena_brutto = zakup_brutto / (1 - marza)
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
