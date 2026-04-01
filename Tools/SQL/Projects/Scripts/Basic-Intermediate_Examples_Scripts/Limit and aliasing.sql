-- limit and aliasing

-- limit will only allow the amount of entries you allow 

select * 
from employee_demographics
limit 3
;

select * 
from employee_demographics
order by age desc
limit 0, 3
;

-- aliasing is used to change the name of the col it also works without as (implied aliasing

select gender, avg(age) as average_age
from employee_demographics
group by gender
having average_age > 40
;





