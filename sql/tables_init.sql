DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "parking_lots";

CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT not null,
    "password" TEXT not null,
    "name" TEXT not null,
    "surname" TEXT not null,
    "parking_lot_number" INTEGER not null,
    "email" TEXT not null,
    "phone" INTEGER not null,
    FOREIGN KEY ("parking_lot_number") REFERENCES "parking_lots" ("parking_lot_number")
);

CREATE TABLE "parking_lots" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "parking_lot_number" INTEGER not null,
    "taken" INTEGER DEFAULT 0,
    "taken_by" TEXT,
    "start_date" TEXT not null,
    "end_date" TEXT not null,
    FOREIGN KEY ("parking_lot_number") REFERENCES "users" ("parking_lot_number")
);
