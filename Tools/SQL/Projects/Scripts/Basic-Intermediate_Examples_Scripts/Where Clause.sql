-- Where clause

select 
	* 
from 
	employee_salary
where
	-- first_name = "Leslie";
	salary > 50000;
    
select 
	*
from 
	employee_demographics
where
	-- gender != 'Female';
    birth_date > '1985-01-01'
    -- and gender = "Male";
    or not gender = "Male";
    
select * from employee_demographics
where (first_name = "Leslie" and age = 44) or age > 55;

select * from employee_demographics
where 
	-- first_name like "%er%";
    -- first_name like "a__";
    -- first_name like "a___%";
    birth_date like "1989%";
    
