-- write your queries here
SELECT * 
FROM vehicles 
FULL OUTER JOIN owners 
ON vehicles.owner_id = owners.id;

SELECT first_name, last_name, COUNT(owner_id) 
FROM owners
JOIN vehicles 
ON vehicles.owner_id = owners.id
GROUP BY(first_name,last_name)
ORDER BY(first_name);

SELECT first_name,last_name, ROUND(AVG(price)), COUNT(owner_id)
FROM owners
JOIN vehicles
ON vehicles.owner_id=owners.id
GROUP BY (first_name, last_name)
HAVING COUNT(owner_id)>1 AND ROUND(AVG(price)) > 10000
ORDER BY first_name DESC;