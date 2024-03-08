import streamlit as st
import subprocess
from database import DatabaseHandler
from config import get_db_config

# Get database configuration
db_config = get_db_config()

# Database handler
db_handler = DatabaseHandler(**db_config)

# Function to check user credentials
def check_credentials(email, password):
    return db_handler.check_credentials(email, password)

# Function to sign up a new user
def sign_up(name, email, password):
    return db_handler.sign_up(name, email, password)

# Function to open app.py in a separate window
def open_app_in_new_window():
    subprocess.Popen(["streamlit", "run", "app.py"])

# Streamlit app
def main():
    # Title and instructions
    st.title("Streamlit PostgreSQL Integration")
    st.sidebar.title("Select the desired action:")

    # Sidebar selection for Login and Signup
    tabs = st.sidebar.selectbox("", ["Login", "Sign Up"])

    if tabs == "Login":
        # User input for login form
        email = st.text_input("Email:")
        password = st.text_input("Password:", type="password")

        # Login button
        if st.button("Log In"):
            if check_credentials(email, password):
                st.success("Login successful! You are now logged in.")
                open_app_in_new_window()  # Open app.py in a new window
            else:
                st.error("Invalid email or password. Please try again.")

    elif tabs == "Sign Up":
        # User input for sign-up form
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        password = st.text_input("Password:", type="password")

        # Signup button
        if st.button("Sign Up"):
            if sign_up(name, email, password):
                st.success("User signed up successfully!")

if __name__ == "__main__":
    if 'is_logged_in' not in st.session_state:
         st.session_state.is_logged_in = False

    main()
