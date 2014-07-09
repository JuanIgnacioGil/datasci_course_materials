/*
(d) count: Write a SQL statement to count the number of documents containing the word "parliament"
 
 What to turn in: Run your query against your local database and determine the count returned as described above. On the assignment page, enter the number of records returned.
*/

SELECT COUNT(*) FROM
(
 select docid from frequency where term="parliament"
);