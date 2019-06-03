/*
178. Rank Scores
https://leetcode.com/problems/rank-scores/submissions/
*/
select Score, (
    select 1+count(distinct ts1.Score) from Scores as ts1
    where ts1.Score > ts2.Score
    ) as Rank
from Scores as ts2
order by Score desc;