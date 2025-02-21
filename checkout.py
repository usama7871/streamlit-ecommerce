# checkout.py - Simulated Checkout System
import streamlit as st
import random
import re

if "order_history" not in st.session_state:
    st.session_state.order_history = []

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def generate_order_id():
    return f"ORD-{random.randint(1000, 9999)}-{random.randint(100, 999)}"

def show_checkout_form():
    st.header("💳 Checkout")

    if not st.session_state.cart:
        st.warning("⚠️ Your cart is empty! Add products before checking out.")
        return

    with st.form("checkout"):
        name = st.text_input("Your Name", value=st.session_state.user["name"] if st.session_state.authenticated else "")
        email = st.text_input("Your Email", value=st.session_state.user["email"] if st.session_state.authenticated else "")
        
        if st.form_submit_button("✅ Complete Purchase"):
            if not validate_email(email):
                st.error("❌ Invalid email format!")
            else:
                order_id = generate_order_id()
                st.session_state.order_history.append({
                    "id": order_id,
                    "name": name,
                    "email": email,
                    "items": st.session_state.cart,
                    "total": sum(p["price"] for p in st.session_state.cart)
                })
                st.session_state.cart = []
                
                st.success(f"🎉 Order Placed Successfully! Your Order ID: `{order_id}`")
                st.balloons()
