import streamlit as st
import hashlib

def show_login():
    st.header("🔑 Login")
    
    # Display demo credentials
    with st.expander("Demo Credentials"):
        st.write("**Admin Account**")
        st.write("Username: admin")
        st.write("Password: admin123")
        st.write("\n**User Account**")
        st.write("Username: user")
        st.write("Password: user123")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid username or password")

def show_profile():
    if st.session_state.authenticated:
        st.sidebar.success("Logged in")
        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()
    else:
        st.sidebar.warning("Not logged in")

def authenticate(username, password):
    # Simple authentication for demonstration
    # In a real application, use secure password hashing and database storage
    users = {
        "admin": hashlib.sha256("admin123".encode()).hexdigest(),
        "user": hashlib.sha256("user123".encode()).hexdigest()
    }
    
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return users[username] == hashed_password
    return False
