/*
Write an SQL query that makes recommendations using the pages that your friends liked.
Assume you have two tables:
 - a two-column table of users and their friends, and
 - a two-column table of users and the pages they liked.

It should not recommend pages you already like.
*/

use testdb;

--CREATE table likes
--(
--    userid int not null,
--    pageid int not null
--)

--CREATE table friends
--(
--    userid int not null,
--    friendid int not null
--)

--insert into likes VALUES
-- (1, 101), (1, 201),
-- (2, 201), (2, 301),
-- (3, 301), (3, 401);

--insert into friends VALUES
-- (1, 2), (1, 4), (1, 5),
-- (2, 4), (2, 3),
-- (3, 5), (3, 6);


-- All Tables
select *
from friends
select *
from likes


-- Common Friends
select *
from friends f1
         inner join friends f2
                    on f1.friendid = f2.friendid
where f1.userid = 3
  and f2.userid = 2

-- Recommend New Pages
select f.userid, f.friendid, p1.pageid
from friends f
         left join likes p1
                   on f.friendid = p1.userid
where p1.pageid not in
      (select pageid from likes p2 where p2.userid = f.userid)


-- Recommend New Pages (Alt)
select f.userid, l.pageid, r.pageid
from friends f
         join likes l ON l.userid = f.friendid
         LEFT JOIN likes r ON (r.userid = f.userid AND r.pageid = l.pageid)
where r.pageid IS NULL;

select sum(Null + 10) -- Null