#Exibir nomes de artistas que contracenaram em filmes.
#Só deve ser exibido o nome se todos os seus filmes
#forem anteriores a 1950
use moviesx;
SELECT p.person_name from person p 
INNER JOIN movie_cast mc ON p.person_id = mc.person_id
INNER JOIN movie m ON mc.movie_id = m.movie_id group by p.person_id 
having max(m.release_year) <  1950;

#Exibir a quantidade de atores que contracenaram em mais do que 5 filmes
select count(*) from (
SELECT count(*) as quantidade FROM person p 
INNER JOIN movie_cast mc 
ON p.person_id = mc.person_id 
group by p.person_id having count(*) > 5
) AS subquery;

#Nomes personagens que são nomes de filmes
SELECT mc.character_name from movie_cast as mc 
INNER JOIN movie m ON mc.character_name = m.title;