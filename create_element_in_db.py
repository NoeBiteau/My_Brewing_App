import sqlite3

# Function to create tables in the database
def create_tables():
    connection = sqlite3.connect("brew_calculator.db")
    cursor = connection.cursor()

    # Table for fermentables (malt ingredients)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fermentables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        supplier TEXT,
        source TEXT,
        type TEXT,
        color REAL,
        potential REAL,
        yield_value REAL,
        diastatic_power REAL,
        moisture REAL,
        protein REAL
    )
    """)

    # Table for hops (hop ingredients)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source TEXT,
        alpha_acid REAL NOT NULL,
        hop_type TEXT NOT NULL
    )
    """)

    # Table for diverse ingredients (adjuncts)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS divers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        unit TEXT,
        ingredient_type TEXT,
        usage TEXT,
        time REAL
    )
    """)

    # Table for yeasts (yeast strains)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS yeasts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        laboratory TEXT,
        identifier TEXT,
        unit TEXT,
        attenuation REAL,
        yeast_type TEXT,
        form TEXT,
        temperature REAL,
        attenuation_range REAL,
        abv_max REAL,
        flocculation TEXT
    )
    """)

    connection.commit()
    connection.close()
    print("Tables created successfully.")

# Function to insert test data into the tables
def insert_test_data():
    connection = sqlite3.connect("brew_calculator.db")
    cursor = connection.cursor()

    # Test data for fermentables (malt ingredients)
    fermentables = [
        ("Pale Malt", "Base", "MaltCo", "France", "Pale Ale", 8.0, 1.038, 0.75, 300, 5.0, 12.0),
        ("Caramel Malt", "Specialty", "SpecialMalt", "Belgium", "Caramel", 40.0, 1.030, 0.7, 500, 5.5, 10.0),
        ("Wheat Malt", "Base", "WheatBrew", "Germany", "Wheat", 6.0, 1.040, 0.8, 300, 6.0, 11.0)
    ]
    cursor.executemany("""
        INSERT INTO fermentables (name, category, supplier, source, type, color, potential, yield_value, diastatic_power, moisture, protein)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, fermentables)

    # Test data for hops (hop ingredients)
    hops = [
        ("Cascade", "USA", 5.0, "Bittering"),
        ("Saaz", "Czech Republic", 3.5, "Aroma"),
        ("Centennial", "USA", 7.0, "Dual Purpose")
    ]
    cursor.executemany("""
        INSERT INTO hops (name, source, alpha_acid, hop_type)
        VALUES (?, ?, ?, ?)
    """, hops)

    # Test data for diverse ingredients (adjuncts)
    divers = [
        ("Lactose", "g", "Sugar", "Adjunct", 15.0),
        ("Fruit Puree", "ml", "Fruit", "Adjunct", 30.0),
        ("Cracked Wheat", "g", "Grain", "Adjunct", 60.0)
    ]
    cursor.executemany("""
        INSERT INTO divers (name, unit, ingredient_type, usage, time)
        VALUES (?, ?, ?, ?, ?)
    """, divers)

    # Test data for yeasts (yeast strains)
    yeasts = [
        ("US-05", "Safale", "US-05", "g", 75.0, "Ale", "Dry", 18.0, 70.0, 11.0, "Medium"),
        ("Wyeast 1056", "Wyeast Labs", "1056", "ml", 74.0, "Ale", "Liquid", 20.0, 72.0, 10.5, "Medium"),
        ("London Ale 3", "White Labs", "WLP013", "ml", 72.0, "Ale", "Liquid", 19.0, 73.0, 10.0, "High")
    ]
    cursor.executemany("""
        INSERT INTO yeasts (name, laboratory, identifier, unit, attenuation, yeast_type, form, temperature, attenuation_range, abv_max, flocculation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, yeasts)

    connection.commit()
    connection.close()
    print("Test data inserted successfully.")

if __name__ == "__main__":
    # Create the tables
    create_tables()

    # Insert test data
    insert_test_data()
