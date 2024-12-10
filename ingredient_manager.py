import sqlite3

DATABASE = "brew_calculator.db"

def add_fermentable(name, yield_value, color):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO fermentables (name, yield, color)
    VALUES (?, ?, ?)
    """, (name, yield_value, color))
    connection.commit()
    connection.close()

def get_fermentables():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fermentables")
    rows = cursor.fetchall()
    connection.close()
    return rows

def add_hop(name, alpha_acid, hop_type):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO hops (name, alpha_acid, type)
    VALUES (?, ?, ?)
    """, (name, alpha_acid, hop_type))
    connection.commit()
    connection.close()

def get_hops():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hops")
    rows = cursor.fetchall()
    connection.close()
    return rows
