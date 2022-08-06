# Write your MySQL query statement below
SELECT name as Customers FROM Customers
WHERE id not IN(
SELECT c.id
FROM Customers c INNER JOIN Orders o on c.id=o.customerId);
