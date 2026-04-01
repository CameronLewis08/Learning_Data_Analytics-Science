-- Group By

-- works because answers are binary and because the select is the same as the group by

select gender
from employee_demographics
group by gender;

-- will not work because the select is not aggregated and is not the same as the group by

select first_name
from employee_demographics
group by gender;

-- will now work

select first_name
from employee_demographics
group by first_name;

-- the age is aggregated and will be split into the different genders the select returns therefore you can group by gender

select gender, avg(age)
from employee_demographics
group by gender;

-- when running this you will notice that there is only one office manager

select occupation
from employee_salary
group by occupation
;

-- now you will notice there are two this is because the job is not unique and the different office managers have different salaries which is unknown in the first query
select occupation,salary
from employee_salary
group by occupation,salary
;

-- aggregate functions include avg, max, min, count, etc

select gender, avg(age), MAX(age), MIN(age), count(gender)
from employee_demographics
group by gender
;

-- Order by

-- will print the first name in ascending order
select *
from employee_demographics
order by first_name asc
;

-- ordering by gender then age and by default it is ascending

select *
from employee_demographics
order by gender,age
;

-- you can also have it so gender is asc and age is desc 
select *
from employee_demographics
order by gender,age desc
;

-- order of order by matters because if age is first the genders will not be ordered correctly

select *
from employee_demographics
order by age,gender
;

-- in order by you can also use the position of the columns but it is not very recommended but is just a lil hack

select *
from employee_demographics
order by 5,4
;

