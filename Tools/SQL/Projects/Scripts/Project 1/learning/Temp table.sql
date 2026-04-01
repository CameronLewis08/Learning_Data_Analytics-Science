-- temp table
-- lives in memory and is useable again and again also it will not appear in the schema 
-- this table is useable in other files as well but if you exit the workbench it will delete the temp table

create temporary table temp_table
(
	first_name varchar(50),
    last_name varchar(50),
    favorite_movie varchar(100)
);

select * from temp_table;

insert into temp_table
values( 'Cam', 'Lewis', 'Star Wars: The Empire Strikes Back');

select * from employee_salary;

create temporary table salary_over_50k
select * from employee_salary 
where salary >=50000;

select * from salary_over_50k;

  