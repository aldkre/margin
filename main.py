import streamlit as st
from calculations import calculate_values
from ui import render_table
from config import setup_page

setup_page()

VAT_display = st.selectbox("Wybierz stawkę VAT", options=[0., 5., 8., 23.], index=3, key='VAT')
VAT = VAT_display / 100

zakup_brutto, zakup_netto, marza, cena_brutto = st.columns(4)

def update_table(source):
    marza_val = st.session_state.marza_value / 100
    VAT_val = st.session_state.VAT / 100

    if source == 'netto':
        data = calculate_values(zakup_netto=st.session_state.zakup_netto_value, VAT=VAT_val, marza=marza_val)
    elif source == 'brutto':
        data = calculate_values(zakup_brutto=st.session_state.zakup_brutto_value, VAT=VAT_val, marza=marza_val)
    elif source == 'marza':
        data = calculate_values(zakup_brutto=st.session_state.zakup_brutto_value, VAT=VAT_val, marza=marza_val)
    elif source == 'cena':
        data = calculate_values(cena_brutto=st.session_state.cena_brutto_value, VAT=VAT_val, marza=marza_val)

    render_table(data)

with zakup_netto:
    st.number_input("Cena zakupu netto", step=0.01, key='zakup_netto_value', on_change=update_table, args=('netto',))
with zakup_brutto:
    st.number_input("Cena zakupu brutto", step=0.01, key='zakup_brutto_value', on_change=update_table, args=('brutto',))
with marza:
    st.number_input("Marża brutto (%)", step=0.01, value=50., key='marza_value', on_change=update_table, args=('marza',))
with cena_brutto:
    st.number_input("Cena sprzedaży brutto", step=0.01, key='cena_brutto_value', on_change=update_table, args=('cena',))
