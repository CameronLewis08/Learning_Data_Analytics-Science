-- CTEs

-- same idea as a subquery but with additional functionality and it is only immediatly useable not after because it is not a permanent object

-- cte table

with cte_example as(
select gender, avg(salary) avg_sal, max(salary) max_sal, min(salary) min_sal, count(salary) count_sal
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by gender
)
select avg(avg_sal) from cte_example;

-- cte but as a subquery 

select avg(avg_sal)
from 
	(select gender, avg(salary) avg_sal, max(salary) max_sal, min(salary) min_sal, count(salary) count_sal
		from employee_demographics dem
		join employee_salary sal
			on dem.employee_id = sal.employee_id
		group by gender
	) example_subq;

select avg(avg_sal) from cte_example; -- this will cause an error

-- multiple cte 

with cte_example as(
select employee_id, gender, birth_date
from employee_demographics dem
where birth_date > '1985-01-01'
),
cte_2 as(
select employee_id,salary
from employee_salary
where salary > 50000
)
select * from cte_example
join cte_2 
	on cte_example.employee_id = cte_2.employee_id
    
;

-- you can create col names in the cte declaration instead of using aliases in the select statement as well

with cte_example (gender, avg_sal,max_sal,min_sal,count_sal) as(
select gender, avg(salary), max(salary), min(salary) , count(salary) 
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by gender
)
select * from cte_example;

