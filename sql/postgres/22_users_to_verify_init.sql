CREATE TABLE users (
    id	                SERIAL PRIMARY KEY,
    username	        TEXT NOT NULL,
    password	        TEXT NOT NULL,
    name	            TEXT NOT NULL,
    surname             TEXT NOT NULL,
    parking_lot_number  INTEGER NOT NULL,
    email               TEXT NOT NULL,
    phone               INTEGER NOT NULL,
    registration_date   DATE NOT NULL,
    registration_status TEXT DEFAULT niezweryfikowany,
    approved_by         TEXT,
    attachment          TEXT
);