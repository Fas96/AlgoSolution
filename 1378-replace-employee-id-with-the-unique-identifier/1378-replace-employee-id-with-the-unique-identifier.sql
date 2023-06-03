# Write your MySQL query statement below

SELECT uid.unique_id, e.name 
FROM Employees e LEFT JOIN EmployeeUNI uid ON  e.id = uid.id 