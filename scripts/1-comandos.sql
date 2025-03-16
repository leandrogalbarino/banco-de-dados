Proj(idP, nome, duracao, custo, idD)
	idD refecencia depto
Func(idF, nome, salario, idD, idChefe)
	idD refecencia depto
    idChefe refecencia Func
Depto(idD, nome, predio, idDiretor)
	idDiretor referecencia Func
Aloc(idP,idF, funcao)
	idP refecencia proj
    idF referencia func
    
#Select
select nome,duracao from proj;
select nome, salario*12 from func;

#Form
select * from depto, proj;
select depto.nome, proj.nome 
where depto.idD = proj.idD;

select depto.nome, proj.nome 
where depto.idD = proj.idD and proj.duracao = 3;

select depto.nome as DEPTO, func.nome as DIRETOR 
from depto, func where depto.idDiretor = func.idF;

#Tuplas

select p.nome, f.nome, a.funcao from proj as p, f as func, aloca as a
where a.idP = p.idP and a.idF = f.idF;

#Like
select * from depto where predio like '%centro%';

select * from proj p, depto d where p.idD = d.idD and d.nome = 'TI' order by duracao;

#Agregação
#avg - média, min, max, sum, count

select avg(salario) from func;
select count(*) from depto;
select count(distinct idF) from aloc;
select idD, avg(salario) from func group by idD;

select d.nome, avg(salario) from func f, depto d where f.idD = p.idD group by d.nome having avg(salario) > 7000;


#Junção
#(Inner) join
#Natural join 
#Cross join - tudo igual em ambos tabelas

select * from proj p INNER JOIN depto d on p.idD = d.idD;
select * from proj p INNER JOIN depto d USING (idD);
select * from proj p NATURAL JOIN depto d