# import streamlit as st
# import re
# import psycopg2
# import psycopg2.extras

# def is_valid_email(email):
#     # Email validation using regular expression
#     pattern = r"[^@]+@[^@]+\.[^@]+"
#     return bool(re.match(pattern, email))

# def is_existing_user(username, password, connection):
#     # Check if the entered username and password match a record in the users table
#     with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("SELECT 1 FROM users WHERE username = %s AND password = %s", (username, password))
#         return cursor.fetchone() is not None

# def login(connection):
#     st.subheader("Login")

#     # Create input fields for username and password
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     # Check if the login button is clicked
#     if st.button("Login"):
#         if not username or not password:
#             st.warning("Please enter both username and password.")
#         else:
#             # Check if the entered username and password match a record in the users table
#             if not is_existing_user(username, password, connection):
#                 st.error("Invalid username or password. Please try again.")
#             else:
#                 # Replace the following lines with your authentication logic
#                 # In this example, we just print the username and a success message
#                 st.success(f"Hello, {username}! Login successful!")

# def signup(connection):
#     st.subheader("Signup")

#     # Create input fields for username, email, and password
#     username = st.text_input("Username")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")

#     # Check if the signup button is clicked
#     if st.button("Signup"):
#         if not username or not email or not password or not confirm_password:
#             st.warning("Please fill in all the fields.")
#         elif len(username) < 4:
#             st.warning("Username must be at least 4 characters long.")
#         elif not is_valid_email(email):
#             st.warning("Invalid email address. Please enter a valid email.")
#         elif password != confirm_password:
#             st.error("Passwords do not match. Please try again.")
#         elif is_existing_username(username, connection):
#             st.warning("Username already exists. Please choose a different username.")
#         else:
#             # Insert the new user into the registered users table
#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
#                     (username, email, password)
#                 )
#                 connection.commit()

#             # Replace the following lines with your signup logic
#             # In this example, we just print the username and a success message
#             st.success(f"Hello, {username}! Signup successful! Now you can login.")

# def main():
#     st.title("Login and Signup Pages")

#     try:
#         # Connect to the PostgreSQL database
#         connection = psycopg2.connect(
#             host="localhost",
#             database="altmed",
#             user="adempiere",
#             password="adempiere"
#         )

#         # Get the page parameter from the URL
#         page = st.sidebar.radio("Choose a page:", ("Login", "Signup"), index=0)

#         if page == "Login":
#             login(connection)
#         elif page == "Signup":
#             signup(connection)
#     except psycopg2.OperationalError as e:
#         st.error("Error connecting to the database. Please check your database settings.")
#         st.stop()

# if __name__ == "__main__":
#     main()














import streamlit as st
import psycopg2

# Database connection function
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname="altmed",
            user="postgres",
            password="postgres",
            host="localhost",  # Change this to your PostgreSQL host
            port="5432"        # Change this to your PostgreSQL port
        )
        return connection
    except Exception as e:
        st.error(f"Error: Unable to connect to the database.\n{e}")
        return None

# Function to check user credentials
def check_credentials(email, password):
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT email FROM public.users WHERE email = %s AND password = %s;",
                               (email, password))
                result = cursor.fetchone()

            if result:
                return True
            else:
                return False

        except Exception as e:
            st.error(f"Error: Unable to check credentials.\n{e}")

        finally:
            connection.close()

# Streamlit app
def main():
    # Title and instructions
    st.title("Streamlit PostgreSQL Integration")
    st.write("Enter your email and password to log in.")

    # User input for login form
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Log In"):
        if check_credentials(email, password):
            st.success("Login successful! You are now logged in.")
            # Set session state to indicate the user is logged in
            st.session_state.is_logged_in = True
        else:
            st.error("Invalid email or password. Please try again.")

# Streamlit app redirection
if __name__ == "__main__":
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if st.session_state.is_logged_in:
        
        app.py()
        # Redirect to app.py class
        # st.write("You are logged in. Redirect to app.py class here.")
        # Replace the line above with your code to redirect to the desired page/class.
    else:
        main()
