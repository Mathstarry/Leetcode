# Write your MySQL query statement below
select FirstName, LastName, City, state
from Person left join Address
on Person.PersonId = Address.PersonId;
