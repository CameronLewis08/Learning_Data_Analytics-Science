-- Having vs Where

-- having comes after group by and allows filtering with aggregate functions

select gender, avg(age) 
from employee_demographics
group by gender
having avg(age)>40
;

-- where is before the group by to filter out results before grouping

select occupation, avg(salary)
from employee_salary
where occupation like "%manager%"
group by occupation
having avg(salary) > 75000
;
\
