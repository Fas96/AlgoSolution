# Write your MySQL query statement below

SELECT v.customer_id, count(v.visit_id) as count_no_trans
FROM Visits v WHERE v.visit_id NOT IN (SELECT t.visit_id FROM Transactions t )
GROUP BY v.customer_id