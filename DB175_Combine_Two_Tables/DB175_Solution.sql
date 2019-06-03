
-- 175. Combine Two Tables
-- https://leetcode.com/problems/combine-two-tables/

select tp.FirstName, tp.LastName, ta.City, ta.State from Person as tp
left join Address as ta
on tp.PersonId = ta.PersonId
