/*
(c) union: Write a SQL statement that is equivalent to the following relational algebra expression.
(Hint: you can use the UNION keyword in SQL)
πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
*/

SELECT COUNT(*) FROM
(
 select * from frequency where docid="10398_txt_earn" and count=1
 UNION
 select * from frequency where docid="925_txt_trade" and count=1
);