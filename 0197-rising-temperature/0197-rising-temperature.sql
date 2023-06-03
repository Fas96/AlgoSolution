# Write your MySQL query statement below
select A.id from weather A, weather B
where datediff(A.recordDate, B.recordDate) = 1 and A.temperature > B.temperature;