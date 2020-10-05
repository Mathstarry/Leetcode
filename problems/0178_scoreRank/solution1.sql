# Write your MySQL query statement below
select s1.score, count(distinct s2.score) as 'rank'
from Scores as s1, Scores as s2
where s1.score <= s2.score
group by s1.id
order by s1.score desc
