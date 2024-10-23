import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Margin calc",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={}
)

st.divider()


def table_formatting(temp_data):
    temp_df = pd.DataFrame.from_dict(data=temp_data, orient='index', columns=['Wartości']).transpose()
    st.data_editor(
        temp_df,
        column_order=['zakup netto', 'zakup brutto', 'VAT', 'marża brutto', 'zysk', 'cena netto', 'cena brutto'],
        column_config={
            "zakup netto": st.column_config.NumberColumn(
                "Cena zakupu netto",
                help="Cena zakupu netto wyrażona w złotówkach",
                format="%.2f zł"),
            "zakup brutto": st.column_config.NumberColumn(
                "Cena zakupu brutto",
                help="Cena zakupu brutto wyrażona w złotówkach",
                format="%.2f zł"),
            "VAT": st.column_config.NumberColumn(
                "Stawka VAT",
                help="Stawka podatku VAT wyrażona procentowo",
                format="%.2f %%"),
            "marża brutto": st.column_config.NumberColumn(
                "Stawka marży brutto",
                help="Marża brutto wyrażona procentowo",
                format="%.2f %%"),
            "zysk": st.column_config.NumberColumn(
                "Zysk netto",
                help="Zysk wyrażony w złotówkach, stanowiący różnicę między ceną sprzedaży netto a ceną zakupu netto",
                format="%.2f zł"),
            "cena netto": st.column_config.NumberColumn(
                "Cena sprzedaży netto",
                help="Cena sprzedaży netto wyrażona w złotówkach",
                format="%.2f zł"),
            "cena brutto": st.column_config.NumberColumn(
                "Cena sprzedaży brutto",
                help="Cena sprzedaży brutto wyrażona w złotówkach",
                format="%.2f zł"),
        }
    )


def create_table_from_zakup_netto(zakup_netto, VAT, marza):
    return ({'zakup netto': round(zakup_netto, 2),
                'zakup brutto': round(zakup_netto * (1 + VAT), 2),
                'VAT': round(VAT_display, 0),
                'marża brutto': round(marza * 100, 0),
                'zysk': round((zakup_netto*(1 + VAT)/(1 - marza)/(1 + VAT)) - zakup_netto, 2),
                'cena brutto': round(zakup_netto*(1 + VAT) / (1 - marza), 2),
                'cena netto': round((zakup_netto*(1 + VAT)/(1 - marza)) / (1 + VAT), 2)})


def print_table_from_zakup_netto():
    temp_data = create_table_from_zakup_netto(zakup_netto= st.session_state.zakup_netto_value, VAT=st.session_state.VAT/100, marza=st.session_state.marza_value/100)
    table_formatting(temp_data)


def create_table_from_zakup_brutto(zakup_brutto, VAT, marza):
    return ({'zakup netto': round(zakup_brutto/(1 + VAT), 2),
                'zakup brutto': round(zakup_brutto, 2),
                'VAT': round(VAT_display, 0),
                'marża brutto': round(marza * 100, 0),
                'zysk': round((zakup_brutto/(1 - marza)/(1 + VAT)) - (zakup_brutto/(1 + VAT)), 2),
                'cena brutto': round(zakup_brutto / (1 - marza), 2),
                'cena netto': round(zakup_brutto/(1 - marza) / (1 + VAT), 2)})


def print_table_from_zakup_brutto():
    temp_data = create_table_from_zakup_brutto(zakup_brutto= st.session_state.zakup_brutto_value, VAT=st.session_state.VAT/100, marza=st.session_state.marza_value/100)
    table_formatting(temp_data)


def create_table_from_marza(zakup_brutto, VAT, marza):
    return ({'zakup netto': round(zakup_brutto / (1 + VAT), 2),
             'zakup brutto': round(zakup_brutto, 2),
             'VAT': round(VAT_display, 0),
             'marża brutto': round(marza * 100, 0),
             'zysk': round((zakup_brutto/(1 - marza) / (1 + VAT)) - (zakup_brutto / (1 + VAT)), 2),
             'cena brutto': round(zakup_brutto / (1 - marza), 2),
             'cena netto': round(zakup_brutto/(1 - marza) / (1 + VAT), 2)})


def print_table_from_marza():
    temp_data = create_table_from_zakup_brutto(zakup_brutto= st.session_state.zakup_brutto_value, VAT=st.session_state.VAT/100, marza=st.session_state.marza_value/100)
    table_formatting(temp_data)


def create_table_from_cena_brutto(cena_brutto, VAT, marza):
    return ({'zakup netto': round(-(marza*cena_brutto-cena_brutto) / (1+VAT),2),
             'zakup brutto': round(-(marza*cena_brutto-cena_brutto),2),
             'VAT': round(VAT_display, 0),
             'marża brutto': round(marza * 100, 0),
             'zysk': round((cena_brutto / (1 + VAT)) - (-(marza*cena_brutto-cena_brutto) / (1+VAT)), 2),
             'cena brutto': round(cena_brutto, 2),
             'cena netto': round(cena_brutto / (1 + VAT), 2)})


def print_table_from_cena_brutto():
    temp_data = create_table_from_cena_brutto(cena_brutto= st.session_state.cena_brutto_value, VAT=st.session_state.VAT/100, marza=st.session_state.marza_value/100)
    table_formatting(temp_data)


VAT_display = st.selectbox("Wybierz stawkę VAT", options=[0., 5., 8., 23.], index=3, key='VAT')
VAT = VAT_display/100

zakup_brutto, zakup_netto, marza, cena_brutto = st.columns(4)
with zakup_netto:
    zakup_netto = st.number_input("Wprowadź cenę zakupu netto", step=0.01, key='zakup_netto_value', on_change=print_table_from_zakup_netto)
with zakup_brutto:
    zakup_brutto = st.number_input("Wprowadź cenę zakupu brutto", step=0.01, key='zakup_brutto_value', on_change=print_table_from_zakup_brutto)
with marza:
    marza = st.number_input("Wprowadź marżę brutto", step=0.01, value=50., key='marza_value', on_change=print_table_from_marza)
with cena_brutto:
    cena_brutto = st.number_input("Wprowadź cenę sprzedaży brutto", step=0.01, key='cena_brutto_value', on_change=print_table_from_cena_brutto)
