SELECT COUNT(term) FROM (SELECT term FROM frequency GROUP BY term);
