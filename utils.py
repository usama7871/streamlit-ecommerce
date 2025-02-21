# utils.py
import streamlit as st
import streamlit.components.v1 as components
import os


def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_path, encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def get_filtered_products(products, search, category, min_p, max_p):
    return [p for p in products if 
            (search.lower() in p['name'].lower() or search.lower() in p['description'].lower()) and
            (category == "All" or p['category'] == category) and
            (min_p <= p['price'] <= max_p)]
