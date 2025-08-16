import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Margin calc",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={}
    )
    st.divider()
