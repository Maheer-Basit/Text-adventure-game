import sqlite3

connection = sqlite3.connect("player.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE stats(stats_id INTEGER PRIMARY KEY, health INTEGER, stamina INTEGER, xp INTEGER, location TEXT)")

cursor.execute("CREATE TABLE inventory(inv_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, is_equippable BOOLEAN, description TEXT)")

cursor.execute("CREATE TABLE logs(log_id INTEGER PRIMARY KEY, conversation TEXT, action TEXT)")

cursor.execute("CREATE TABLE rooms(room_id INTEGER PRIMARY KEY, name TEXT, description TEXT, exits TEXT)")


def get_inventory_string():
    name = cursor.execute("SELECT name FROM inventory").fetchall()
    quantity = cursor.execute("SELECT quantity FROM inventory").fetchall()
    return f"You are carrying {quantity, name}"

