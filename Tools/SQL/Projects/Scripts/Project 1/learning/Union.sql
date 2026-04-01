-- unions
-- allows you to combine rows of data from seperate or the same table instead of rows

-- this combination doesnt work together the data should be the same/similar
select age,gender from employee_demographics
union 
	select first_name, last_name from employee_salary;

-- combines the rows since the data is the same and adds ron swanson since he was not in the demographics table, by default union is distinct

select first_name, last_name from employee_demographics
union DISTINCT
	select first_name, last_name from employee_salary;
    
-- Union all will allow for duplicates

select first_name, last_name from employee_demographics
union ALL
	select first_name, last_name from employee_salary;
    
-- union allows for multiple selects all combined 

select first_name, last_name,'Old Man' as LABLE from employee_demographics
where age > 40 and gender = "Male"
union 
	select first_name, last_name,'Old Female' as LABLE from employee_demographics
	where age > 40 and gender = "Female"
union
	select first_name, last_name, 'High Salary' as Label from employee_salary
	where salary > 70000
order by first_name, last_name;


    