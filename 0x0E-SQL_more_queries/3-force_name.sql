-- get the database name from the first argument
-- data in tabl: id INT, name VARCHAR(256) can't be null
-- Create table force_name (if not exists)

CREATE TABLE IF NOT EXISTS '@db_name'.'force_name'(
	'id' INT NOT NULL,
	'name' VARCHAR(256) NOT NULL,
	PRIMARY KEY ('id')
	);
