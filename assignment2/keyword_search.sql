/*
 Ejecutar como:
 sqlite3 reuters.db < keyword_search.sql|head -1|awk -F '|' '{print $2}' > keyword_search.txt
*/


/*
(i) keyword search: Find the best matching document to the keyword query "washington taxes treasury". You can add this set of keywords to the document corpus with a union of scalar queries:

SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
Then, compute the similarity matrix again, but filter for only similarities involving the "query document": docid = 'q'. Consider creating a view of this new corpus to simplify things.
What to turn in: On the assignment page, enter the maximum similarity score between the keyword query and any document. Your SQL query should return a list of (docid, similarity) pairs, but you will submit only a single number: the highest score in the list.
 */


/*Creamos una vista que incluye la query*/
CREATE VIEW [ks] AS
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

/*Calculamos las similitudes de todo la base de datos con la query*/
select d.docid,sum(d.count*q.count) as similitud from


(select term, count from [ks]) q
left join
(select docid,term,count from frequency) d
on q.term=d.term

group by d.docid
order by similitud desc;

/*Eliminamos la vista*/
DROP VIEW [ks];
