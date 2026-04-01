-- Case statements

-- you can have multiple when statements in your case statement and it is the same idea as a switch case 

select first_name, last_name,
case
	when age<=30 then 'Young' 
    when age between 31 and 50 then 'Old'
    when age>=50 then 'Senior'
end as age_bracket
	from employee_demographics;

-- pay increase and bonus
-- < 50000 = 5%
-- > 50000 = 7%
-- finance dept bonus = 10%

select first_name, last_name, salary, dept_id,
case 
	when salary < 50000 then salary * 1.05
    when salary > 50000 then salary * 1.07
end as new_salary,
case 
	when dept_id = 6 then salary * 0.10
end as Bonus
from employee_salary;

-- find finance dept id 
select * from parks_departments;
