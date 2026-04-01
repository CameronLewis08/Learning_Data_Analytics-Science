-- Stored Procedures
-- A way to save sql code that you can use over and over again, when saved you can call the procedure and it will run all the written code within its scopeUSE parks_and_recreations -- not neccessary but a good practice


select * from employee_salary
where salary >= 50000;


-- this example is not a best practice it is best for more complex queries with multiple layers

USE parks_and_recreations; -- not neccessary but a good practice
create procedure large_salaries()
	select * from employee_salary
	where salary >= 50000;

CALL large_salaries();

-- better example
-- changes delimiter (;) and makes it so the procedure runs both select statements instead of one or the other and you need to change it back after
DELIMITER $$ 
create procedure large_salaries2()
	BEGIN
	select * from employee_salary
	where salary >= 50000;
    select * from employee_salary
    where salary >=10000;
	END $$
    
DELIMITER ;  -- You can edit these procedures from anywhere by right clicking on the procedure in the list of stored procedures


-- this call will create two resulting tables one named result 6 and the other 7 in order of the select statements from the procedure 

CALL large_salaries2()

-- you can also right click stored procedures and create a new one that way


-- parameters can be passed into the stored procedure similar to a function/method when calling them
DELIMITER $$ 
create procedure large_salaries3(selected_id_param INT)
	BEGIN
		select salary from employee_salary
        where employee_id = selected_id_param;
	END $$
DELIMITER ;

call large_salaries3(1)