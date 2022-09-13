-- displays the avergate temperature by city
SELECT city, AVG(value) FROM temperatures WHERE city IS NOT NULL AND VALUE IS NOT NULL GROUP BY CITY;
