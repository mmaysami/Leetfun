/* 
185. Department Top Three Salaries
https://leetcode.com/problems/department-top-three-salaries/
*/
select td.Name as 'Department', te1.Name as 'Employee', te1.Salary from Employee te1
join Department td 
on te1.DepartmentId = td.Id
where  
    3 > (select count(distinct te2.Salary) from Employee te2
        where te2.Salary > te1.Salary
        and te1.DepartmentId = te2.DepartmentId)
order by td.Name asc, te1.Salary desc;