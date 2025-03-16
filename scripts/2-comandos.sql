#Codigo aula 2
#JUNCAO EXTERNA
SELECT * FROM proj p INNER JOIN depto d ON p.idD = d.idD;
SELECT * FROM proj p LEFT OUTER JOIN depto d ON p.idD = d.idD;
SELECT * FROM proj p NATURAL RIGHT OUTER JOIN depto d;

#CONJUNTOS
#(SELECT idChefe FROM func) INTERSECT (SELECT idDiretor FROM depto); 
#(SELECT idChefe FROM func) EXCEPT (SELECT idDiretor FROM depto); 
(SELECT idChefe FROM func) UNION (SELECT idDiretor FROM depto); 
(SELECT idChefe FROM func) UNION ALL (SELECT idDiretor FROM depto); 

#SUBCONSULTAS
#DENTRO DO SELECT
SELECT nome,
(SELECT count(*) FROM aloc a WHERE f.idF = a.idF) AS proj, 
(SELECT count(*) FROM func sub WHERE f.idF = sub.idChefe) AS sub 
FROM func f;

#DENTRO DO FROM
SELECT MAX(tab.media) AS maior_media FROM 
(SELECT AVG(salario) AS media FROM func f 
GROUP BY idD) AS tab;

#DENTRO DO WHERE
#COMPARACAO DIRETA 
SELECT nome FROM func WHERE 
salario > (SELECT MAX(custo) FROM proj); 
#um unico valor na selecao

SELECT nome FROM func f WHERE 2 = 
(SELECT COUNT(*) FROM aloc a WHERE f.idFunc = a.idFunc);

#IN/EXISTS
SELECT DISTINCT nome FROM func NATURAL JOIN aloc; #JUNCAO NORMAL

SELECT nome FROM func WHERE idF IN (SELECT idF FROM aloc);
SELECT nomeP from proj p WHERE custo IN
(SELECT salario FROM func);

SELECT nomeP FROM proj p WHERE EXISTS
(SELECT 1 FROM func f WHERE p.custo < f.salario);
SELECT nome FROM func f WHERE EXISTS (SELECT * FROM aloc a
WHERE f.idF = a.idF);

#NOT IN NOT EXISTS
SELECT nome FROM func NATURAL LEFT JOIN aloc a
WHERE a.idP IS NULL; #JUNCAO EXTERNA

SELECT nome FROM func WHERE idF NOT IN 
(SELECT idF FROM aloc);

SELECT nome FROM func f WHERE NOT EXISTS
(SELECT * FROM aloc WHERE f.idF = a.idF);
#A consulta com NOT IN devolve um registro vazio se 
#ouver valores nulos em uma das compaçoes

#SUBCONSULTAS
SELECT idF FROM func WHERE idF IN 
(SELECT idChefe FROM func) OR
idF IN (SELECT idDiretor FROM depto);

SELECT DISTINCT f.idF FROM func f, func sub, depto dir
WHERE f.idF = sub.idChefe OR f.idF = dir.idDiretor;

SELECT idChefe FROM func WHERE idChefe IN 
(SELECT idDiretor FROM depto);

SELECT DISTINCT idChefe FROM func JOIN depto
ON idChefe = idDiretor;

SELECT idChefe FROM func WHERE idChefe NOT IN
(SELECT idDiretor FROM depto);

SELECT idChefe FROM func LEFT JOIN depto ON idChefe = idDiretor
WHERE idDiretor IS NULL AND idChefe IS NOT NULL;

