/*
178. Rank Scores
https://leetcode.com/problems/rank-scores/

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking.
Note that after a tie, the next ranking number should be the next consecutive integer value.
In other words, there should be no "holes" between ranks.

Important Note: For MySQL solutions, to escape reserved words used as column names,
                you can use an apostrophe before and after the keyword. For example `Rank`.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

For above example table, your query should generate the following report (order by highest score):
+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+
*/

select Score,
       (
           select 1 + count(distinct ts1.Score)
           from Scores as ts1
           where ts1.Score > ts2.Score
       ) as Rank
from Scores as ts2
order by Score desc;