#Exibir nomes de artistas que contracenaram em filmes.
#Só deve ser exibido o nome se todos os seus filmes
#forem anteriores a 1950
use moviesx;

SELECT p.person_name FROM person p INNER JOIN movie_cast mc
ON p.person_id = mc.person_id INNER JOIN movie m
ON mc.movie_id = m.movie_id GROUP BY p.person_id
HAVING max(m.release_year) < 1950;

SELECT p.person_name
FROM person p
WHERE EXISTS (
    SELECT 1
    FROM movie_cast mc
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE mc.person_id = p.person_id
    AND m.release_year < 1950
) AND NOT EXISTS (
    SELECT 1
    FROM movie_cast mc
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE mc.person_id = p.person_id
    AND m.release_year > 1950
);

#Exibir a quantidade de atores que contracenaram em mais do que 5 filmes
SELECT count(*) as QUANTIDADE FROM ( 
SELECT p.person_id FROM person p INNER JOIN movie_cast mc ON p.person_id = mc.person_id
GROUP BY p.person_id HAVING count(*) > 5) as subquery;

#Nomes personagens que são nomes de filmes
SELECT mc.character_name FROM movie_cast mc INNER JOIN movie m ON m.title = mc.character_name; 

