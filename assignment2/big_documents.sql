/*
(e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)

What to turn in: Run your query against your local database and determine the number of records returned as described above. On the assignment page, enter the number of records returned.

*/

SELECT COUNT(*) FROM
(
 select docid, sum(count) as suma from frequency
 GROUP BY docid
 HAVING suma>300
);