-- Table cleaned / typed
DROP TABLE IF EXISTS flights;

CREATE TABLE flights AS
SELECT
  index AS id,
  airline,
  flight,
  source_city,
  datetime(departure_time) AS departure_time,
  stops,
  datetime(arrival_time) AS arrival_time,
  destination_city,
  class,
  duration,
  days_left,
  price
FROM flights_raw
WHERE price IS NOT NULL;

-- Useful index
CREATE INDEX IF NOT EXISTS idx_flights_airline ON flights(airline);
CREATE INDEX IF NOT EXISTS idx_flights_price ON flights(price);
CREATE INDEX IF NOT EXISTS idx_flights_departure ON flights(departure_time);
