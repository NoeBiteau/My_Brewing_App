import sqlite3

def fetch_data():
    connection = sqlite3.connect("brew_calculator.db")
    cursor = connection.cursor()

    # Fetch all fermentables
    cursor.execute("SELECT * FROM fermentables")
    fermentables = cursor.fetchall()
    print("Fermentables:")
    for row in fermentables:
        print(row)

    # Fetch all hops
    cursor.execute("SELECT * FROM hops")
    hops = cursor.fetchall()
    print("\nHops:")
    for row in hops:
        print(row)

    # Fetch all divers
    cursor.execute("SELECT * FROM divers")
    divers = cursor.fetchall()
    print("\nDivers:")
    for row in divers:
        print(row)

    # Fetch all yeasts
    cursor.execute("SELECT * FROM yeasts")
    yeasts = cursor.fetchall()
    print("\nYeasts:")
    for row in yeasts:
        print(row)

    connection.close()

if __name__ == "__main__":
    fetch_data()
