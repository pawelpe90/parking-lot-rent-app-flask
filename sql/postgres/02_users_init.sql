CREATE TABLE users (
    id	                SERIAL PRIMARY KEY,
    username	        TEXT NOT NULL,
    password	        TEXT NOT NULL,
    name	            TEXT NOT NULL,
    surname             TEXT NOT NULL,
    parking_lot_number  INTEGER NOT NULL,
    email               TEXT NOT NULL,
    phone               INTEGER NOT NULL,
    user_status         TEXT NOT NULL,
    join_date           DATE NOT NULL,
    added_by            TEXT NOT NULL
);