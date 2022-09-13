-- lists all records of the table `second_table` OF THE DATABASE HBTN_0C_0
SELECT score, name  FROM second_table WHERE name IS NOT NULL ORDER BY score DESC, name ASC;
