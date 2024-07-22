-- Lists all records of the table second_table having a name value in MySQL server.
-- Records are in descending order 
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
