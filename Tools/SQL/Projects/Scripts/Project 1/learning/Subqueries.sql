-- Subqueries

-- select employee id from demo table when the id is also in the salary table and the dept id is 1
select * from employee_demographics   -- opertator
	where employee_id IN ( 
		select employee_id from employee_salary  -- operand (operand may only contain one column)
        where dept_id = 1);
        
-- allows you to use aggregated cols without where or having clause

select first_name,salary,(select avg(salary) from employee_salary) as avg_salary
from employee_salary
group by first_name,salary;

-- doesnt allow you to get the average of the max min or count 
select gender, avg(age), max(age), min(age), count(age) from employee_demographics
group by gender;

select gender, avg(max_age),avg(count_age)
from
	(select gender, 
    avg(age) as avg_age, 
    max(age) as max_age, 
    min(age) as min_age, 
    count(age) as count_age
    from employee_demographics
group by gender) as aggregated_table
group by gender;
