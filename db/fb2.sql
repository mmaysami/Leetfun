/*
'you have a table Submissions with the submission_id, the body, and the parent_id.
Submissions can be posts, or comments to a post. In posts, parent_id is null, and in comments, the parent_id is the post
the comment is commenting about. How would you go and make a histogram of number of posts per comment_count?'
*/
use testdb;
--create table subs(
--sub_id integer,
--parent_id integer
--)

--insert into subs values(1,null);
--insert into subs values(2,null);
--insert into subs values(3,null);
--insert into subs values(4,null);
--commit;

--insert into subs values(5,1);
--insert into subs values(6,1);
--insert into subs values(7,1);
--insert into subs values(8,1);

--insert into subs values(9,2);
--insert into subs values(10,2);
--insert into subs values(11,3);
--insert into subs values(12,3);

--insert into subs values(12,4);
--commit;

-- All Entries
select *
from subs

-- Parent - Childs
select *
from subs sl
         left join subs sr
                   on sl.sub_id = sr.parent_id

-- Count of Comments per Sub ID
select sl.sub_id, count(sr.parent_id) as 'comments'
from subs sl
         left join subs sr
                   on sl.sub_id = sr.parent_id
group by sl.sub_id


-- Histogram
select tmp.comments, count(tmp.comments) as 'hist'
from (select sl.sub_id, count(sr.parent_id) as 'comments'
      from subs sl
               left join subs sr
                         on sl.sub_id = sr.parent_id
      group by sl.sub_id) AS tmp
group by tmp.comments

