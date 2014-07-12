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