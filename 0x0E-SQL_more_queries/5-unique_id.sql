i-- script that creates the table unique_id on your MySQL server
-- creates a  table
-- default value must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
