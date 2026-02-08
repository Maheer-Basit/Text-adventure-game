import sqlite3

connection = sqlite3.connect("player.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS stats(stats_id INTEGER PRIMARY KEY, health INTEGER, stamina INTEGER, xp INTEGER, location TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS inventory(inv_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, is_equippable BOOLEAN, description TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS logs(log_id INTEGER PRIMARY KEY, conversation TEXT, action TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS rooms(room_id INTEGER PRIMARY KEY, name TEXT, description TEXT, exits TEXT)")

cursor.execute("INSERT OR IGNORE INTO stats (stats_id, health, stamina, xp, location) VALUES (1, 100, 100, 0, 'Starting Room')")

cursor.execute("INSERT OR IGNORE INTO rooms (room_id, name, description, exits) VALUES (1, 'Starting Room', 'You are in a dimly lit room with concrete walls and a single door to the north.', 'North: Hallway')")

def get_inventory_string():
    name = cursor.execute("SELECT name FROM inventory").fetchall()
    quantity = cursor.execute("SELECT quantity FROM inventory").fetchall()
    return f"You are carrying {quantity, name}"

def get_current_state():
    health = cursor.execute("SELECT health FROM stats").fetchone()[0]
    stamina = cursor.execute("SELECT stamina FROM stats").fetchone()[0]
    xp = cursor.execute("SELECT xp FROM stats").fetchone()[0]
    location = cursor.execute("SELECT location FROM stats").fetchone()[0]
    inventory = get_inventory_string()
    room_description = cursor.execute("SELECT description FROM rooms WHERE name=?", (location,)).fetchone()[0]
    return f"Health: {health}, Stamina: {stamina}, XP: {xp}, Location: {location}, Inventory: {inventory}, Room Description: {room_description}"