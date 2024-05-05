import mysql.connector


# Connect to MySQL
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="collage"
        )
        print("Connected to MySQL!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Insert new data into MySQL
def insert_data(conn, data):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s)"
        cursor.execute(sql, data)
        conn.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


# Update existing data in MySQL
def update_data(conn, data):
    try:
        cursor = conn.cursor()
        sql = "UPDATE your_table SET column2 = %s WHERE column1 = %s"
        cursor.execute(sql, data)
        conn.commit()
        print("Data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def main():
    # Connect to MySQL
    conn = connect_to_mysql()

    # Prompt user for data to insert
    new_data = (
        input("Enter your name: "),
        input("Enter your age: "),
        input("Enter your course: ")
    )

    # Close connection
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    main()
