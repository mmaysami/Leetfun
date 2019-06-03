/* 
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/ 
*/

-- Solution A (Fails for Null)
-- select top(1) Salary as SecondHighestSalary from 
-- (select top(2) Salary from Employee order by Salary Desc) as TopTable
-- order by Salary Asc


-- Solution B (Slower)
-- select max(Salary) as SecondHighestSalary from Employee 
-- where Salary < (select Max(Salary) from Employee);


-- Solution C (Faster)
select max(salary) as SecondHighestSalary from Employee 
where Salary not in (select max(Salary) from Employee);