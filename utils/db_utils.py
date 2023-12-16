import sqlite3


def get_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def get_parking_lot_number(username):
    conn = get_connection()
    c = conn.cursor()

    result = c.execute("""SELECT "parking_lot_number" FROM users where username = ? """, (username,))
    return result.fetchone()


def get_parking_lot_number_status(parking_lot_number):
    conn = get_connection()
    c = conn.cursor()

    result = c.execute("""SELECT "taken" FROM parking_lots where parking_lot_number = ? """, (parking_lot_number,))
    return result.fetchone()


def get_user_reservations(username):
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM parking_lots where taken_by = ?', (username,))
    return result.fetchall()


def get_free_parking_lots(username):
    conn = get_connection()
    c = conn.cursor()

    result = c.execute("""
    SELECT 
    parking_lots."id", parking_lots."parking_lot_number", parking_lots."start_date", parking_lots."end_date", users."username"
    FROM parking_lots 
    LEFT JOIN users ON parking_lots.parking_lot_number = users.parking_lot_number
    where parking_lots.taken = 0 and users.username <> ?""", (username,))
    return result.fetchall()
