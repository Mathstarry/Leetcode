CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
        select salary 
        from Employee 
        group by salary
        order by salary desc
        limit 1 offset N
  );
END
