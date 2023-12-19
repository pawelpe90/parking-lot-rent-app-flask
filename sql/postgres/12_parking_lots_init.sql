CREATE TABLE parking_lots (
    id	                SERIAL PRIMARY KEY,
    parking_lot_number  INTEGER NOT NULL,
    taken               INTEGER NOT NULL DEFAULT 0,
    taken_by            TEXT,
    start_date          DATE NOT NULL,
    end_date            DATE NOT NULL,
);