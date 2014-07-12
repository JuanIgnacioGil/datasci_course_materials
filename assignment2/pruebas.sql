select sum(d1.count*d2.count)
from (select term,count from frequency where docid='10080_txt_crude') d1
left join (select term, count from frequency where docid='17035_txt_earn') d2
on d1.term=d2.term;