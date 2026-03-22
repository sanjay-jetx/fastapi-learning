import mysql.connector;

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",      # MySQL host
        user="root",           # MySQL username
        password="sanjay2512",       # MySQL password
        database="test"        # Database name
    )

    print("Connected to MySQL successfully")

    conn.close()


if __name__ == "__main__":
    connect_to_mysql()


