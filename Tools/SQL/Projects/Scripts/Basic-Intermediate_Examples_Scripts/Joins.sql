-- joins 

select * from employee_demographics;

select * from employee_salary;

-- inner joins, the common cols of the salary table into the demographics table combining the information with, since employee id is not in the demo table it will not be in the join
select demo.employee_id, age, occupation
from employee_demographics as demo
inner join employee_salary as sal
	on demo.employee_id = sal.employee_id;
    
-- outter joins, left join - take everything from left table even if there is no match in the join and then return the matches from the right table and the opposite is true for a right join

select *
from employee_demographics as demo
left join employee_salary as sal
	on demo.employee_id = sal.employee_id;
    
-- adds employee 2 but only has the information from the salary table and the other missing information is null

select *
from employee_demographics as demo
right join employee_salary as sal
	on demo.employee_id = sal.employee_id;
    
-- self join/cross join, table joined with itself
select emp1.employee_id as santa, emp1.first_name as first_name_santa, emp1.last_name as last_name_santa,
emp2.employee_id as reciever_id, emp1.first_name as first_name_reciever, emp1.last_name as last_name_reciever
from employee_salary as emp1
cross join employee_salary as emp2
	on emp1.employee_id + 1 = emp2.employee_id
;

-- join multiple table

select *
from employee_demographics as demo
inner join employee_salary as sal
	on demo.employee_id = sal.employee_id
inner join parks_departments pd
	on sal.dept_id = pd.department_id
order by gender asc, salary desc
    ;

-- reference table 

select * from parks_departments;




