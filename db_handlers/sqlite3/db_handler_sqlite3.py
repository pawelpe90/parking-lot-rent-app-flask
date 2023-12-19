from utils.db_utils import get_connection


def reserve_parking_lot_handler_sqlite3(username, parking_lot_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""UPDATE "parking_lots" SET "taken" = 1, "taken_by" = ? WHERE "id" = ?""", (username, parking_lot_id))
    conn.commit()
