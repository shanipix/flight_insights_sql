DROP TABLE IF EXISTS flights_raw;

CREATE TABLE IF NOT EXISTS flights_raw (
  row_id INTEGER,
  airline TEXT,
  flight TEXT,
  source_city TEXT,
  departure_time TEXT,
  stops INTEGER,
  arrival_time TEXT,
  destination_city TEXT,
  class TEXT,
  duration TEXT,
  days_left INTEGER,
  price REAL
);
