-- Triggers and Events
-- A trigger is a block of code that executes automatically when a event takes place on specific table


select * from employee_demographics;

select * from employee_salary;


-- creating a trigger, Creating a trigger does not work like procedures in order to access your triggers you need to access the table schema and in this case its under Tables/employee_salary/Triggers

DELIMITER $$ 
CREATE TRIGGER employee_insert_trigger
	AFTER INSERT ON employee_salary   -- BEFORE is also an option mostly used with deleting information
	FOR EACH ROW 
BEGIN
	INSERT INTO employee_demographics (employee_id,first_name,last_name)
    VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);		-- OLD is also an option
END $$
DELIMITER ;

-- you cannot alter, change, or drop your triggers

INSERT INTO employee_salary(employee_id,first_name,last_name,occupation,salary,dept_id)
VALUES(13,'Jean','Sapaerstein','Entertainment',1000000,NULL);

-- Any missing information that the demographics table requires will not be filled in and will have a null value in its place requiring manual fixing after the fact

-- EVENTS 
-- a trigger happens when an event takes place but an event takes place when its scheduled

DELIMITER $$
CREATE EVENT retirements
ON SCHEDULE EVERY 30 SECOND
DO 
BEGIN
	DELETE 
    from employee_demographics
    where age >=60;
END $$

DELIMITER ;











