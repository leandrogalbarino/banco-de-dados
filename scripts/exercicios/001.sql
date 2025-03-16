select release_year, count(*) as num 
from movie group by release_year 
order by count(*) desc;

select m.title as titulo, count(*) as quantidade 
from movie as m INNER JOIN movie_cast as mc 
ON m.movie_Id = mc.movie_id group by mc.movie_id;

SELECT p.person_name, min(m.release_year) AS PF, max(m.release_year) AS UF
FROM person AS p 
INNER JOIN movie_cast AS mc ON p.person_id = mc.person_id
INNER JOIN movie m ON mc.movie_id = m.movie_id
GROUP BY p.person_id
ORDER BY UF DESC;