import streamlit as st
import pandas as pd

def render_table(data_dict):
    df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['Wartości']).transpose()
    st.data_editor(
        df,
        column_order=['zakup netto', 'zakup brutto', 'VAT', 'marża brutto', 'zysk', 'cena netto', 'cena brutto'],
        column_config={
            "zakup netto": st.column_config.NumberColumn("Cena zakupu netto", format="%.2f zł"),
            "zakup brutto": st.column_config.NumberColumn("Cena zakupu brutto", format="%.2f zł"),
            "VAT": st.column_config.NumberColumn("Stawka VAT", format="%.0f %%"),
            "marża brutto": st.column_config.NumberColumn("Marża brutto", format="%.0f %%"),
            "zysk": st.column_config.NumberColumn("Zysk netto", format="%.2f zł"),
            "cena netto": st.column_config.NumberColumn("Cena sprzedaży netto", format="%.2f zł"),
            "cena brutto": st.column_config.NumberColumn("Cena sprzedaży brutto", format="%.2f zł"),
        }
    )
