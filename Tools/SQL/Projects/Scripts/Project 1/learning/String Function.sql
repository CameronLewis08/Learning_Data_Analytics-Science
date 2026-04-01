-- String Functions

-- determine length of string

select LENGTH('skyfall');

select first_name, last_name, LENGTH(first_name) + LENGTH(last_name) as length_name from employee_demographics
order by length_name asc;

-- capitalizes

select UPPER('sky');

-- lowercase 

select LOWER('SKY');

select first_name, last_name, UPPER(first_name), UPPER(last_name) from employee_demographics
order by first_name;

-- trim gets rid of leading and trailing white spaces, you can also choose to get rid of the right or left trim

select TRIM('      sky          ');
select LTRIM('      sky          ');
select RTRIM('      sky          ');

-- substring   finds the specified starting point in a string and goes to the specified end point and returns the string gathered
-- left/right  finds the characters starting from the specified side and to the length specified

select first_name, LEFT(first_name,4), right(first_name,4), substring(first_name,3, 2), birth_date, substring(birth_date,6,2) as birth_month
from employee_demographics;

-- replace will replace specific characts with those you want and is caps sensitive

select first_name, replace(first_name, 'A', 'z')
from employee_demographics;

-- locate will return position of the specified character and is not caps sensitive

select LOCATE('x',"alexander");

select first_name, locate('an',first_name) from employee_demographics;

-- concat will combine cols/strings
select first_name, last_name, concat(first_name,' ', last_name) as full_name from employee_demographics;
 


