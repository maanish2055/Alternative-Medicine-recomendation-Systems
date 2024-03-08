def get_db_config():
    # Database configuration
    db_config = {
        "dbname": "altmed",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",  # Change this to your PostgreSQL host
        "port": "5432"        # Change this to your PostgreSQL port
    }
    return db_config
