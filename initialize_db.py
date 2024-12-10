import sqlite3

def create_tables():
    connection = sqlite3.connect("brew_calculator.db")
    cursor = connection.cursor()

    # Table pour les fermentescibles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fermentables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        yield REAL NOT NULL,
        color REAL NOT NULL
    )
    """)

    # Table pour les houblons
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        alpha_acid REAL NOT NULL,
        type TEXT NOT NULL
    )
    """)

    # Table pour les levures
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS yeasts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        attenuation REAL NOT NULL,
        flocculation TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
