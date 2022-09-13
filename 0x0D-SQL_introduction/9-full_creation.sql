-- Create a table `second_table` IN TTHE DATABASE `HBTN_0C_0`
-- and adds multiples rows
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(255), score INT);
INSERT INTO second_table VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
