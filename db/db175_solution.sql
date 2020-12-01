/*
175. Combine Two Tables
https://leetcode.com/problems/combine-two-tables/


Write a SQL query for a report that provides the following information for each person in the Person table,
regardless if there is an address for each of those people:
FirstName, LastName, City, State

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
*/

select tp.FirstName, tp.LastName, ta.City, ta.State
from Person as tp
         left join Address as ta
                   on tp.PersonId = ta.PersonId
