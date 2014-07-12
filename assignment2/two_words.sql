/*
(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.

What to turn in: Run your query against your local database and determine the number of records returned as described above. On the assignment page, turn in a text file two_words.txt that contains the number of records.

*/

SELECT COUNT(*) FROM
(
 select docid from frequency where term="transactions"
 INTERSECT
 select docid from frequency where term="world"
);