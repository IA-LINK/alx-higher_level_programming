-- Get the database name from the first argument
-- Create table id_not_null (if not exists)

CREATE TABLE IF NOT EXISTS `@db_name`.`id_not_null` (
  `id` INT NOT NULL DEFAULT 1,
  `name` VARCHAR(256),
  PRIMARY KEY (`id`)
);
