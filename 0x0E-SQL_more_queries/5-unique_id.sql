-- Get the database name from the first argument
-- Create table unique_id (if not exists)

CREATE TABLE IF NOT EXISTS(
  	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
