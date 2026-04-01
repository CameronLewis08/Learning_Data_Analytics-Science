-- windows functions 
-- like group by but dont roll up into one row when grouping it allows us to look at a partition or group where they each keep their own unique row


select gender, avg(salary) as average_salary
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by gender
;

select gender, avg(salary) over(partition by gender) -- if you only specify gender and not partion it gives male/female and the average for each 
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
;

-- all salaries are the same due to partition

select dem.first_name,dem.last_name,gender, avg(salary) over(partition by gender) as avg_salary 
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
;

-- all salaries are different values cause of order by

select dem.first_name,dem.last_name,gender, avg(salary) as avg_salary
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by dem.first_name, dem.last_name,gender
;

-- all men together make 402000 and all females together make 215000

select dem.first_name,dem.last_name,gender, sum(salary) over(partition by gender) as sum_salary -- if you only specify gender and not partion it gives male/female and the average for each 
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
;

-- rolling total ( does not require partition by)
-- adds each salary to the total all the way to the grand total for women and then for men

select dem.first_name,dem.last_name,gender,salary, sum(salary) over(partition by gender order by dem.employee_id) as rolling_total 
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
;

-- row number (will not repeat without partition by)
-- counts row number and with partition will essentially create row numbers seperate for both women and men
-- rank (positional)
-- will apply a number based on the salary in this example and will assign the same number to duplicate salaries and skips a number on the next index 
-- dense_rank (numeric)
-- same as rank but will not skip next index number 

select 
dem.employee_id,
dem.first_name,
dem.last_name,
gender,
salary, 
row_number()over(partition by gender order by salary desc) as row_num,
rank()over(partition by gender order by salary desc) as rank_num,
dense_rank()over(partition by gender order by salary desc) as dense_rank_num
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
;
