# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE  NOT  referee_id='2' || referee_id is NULL ;