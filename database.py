import psycopg2

class DatabaseHandler:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as e:
            st.error(f"Error: Unable to connect to the database.\n{e}")
            return None

    def check_credentials(self, email, password):
        connection = self.connect()
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

    def sign_up(self, name, email, password):
        connection = self.connect()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO public.users (username, email, password) VALUES (%s, %s, %s);",
                                   (name, email, password))
                connection.commit()
                return True

            except Exception as e:
                connection.rollback()
                st.error(f"Error: Unable to sign up the user.\n{e}")
                return False

            finally:
                connection.close()
