import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
   user="postgres",
   password="postgres",
   host="localhost",
   port="5432",
   database="postgres"
)

# Create a cursor object
cur = conn.cursor()

# Function to create a user table if it doesn't exist
def create_user_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()

# Function to insert a new user into the database
def insert_user(username, email, phone, password):
    cur.execute("""
        INSERT INTO users (username, email, phone, password)
        VALUES (%s, %s, %s, %s)
    """, (username, email, phone, password))
    conn.commit()

# Example usage: sign up a new user
def signup(username, email, phone, password):
    create_user_table()  # Ensure the user table exists
    insert_user(username, email, phone, password)

# Close cursor and connection
cur.close()
conn.close()
