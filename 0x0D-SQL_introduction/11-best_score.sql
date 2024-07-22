-- Lists all records in the table second_table with score >= 10 in MySQL server.
-- Records are in decsending order of score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
