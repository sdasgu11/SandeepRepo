-- Q: How many people have rented the film _Blanket Beverly_?

 SELECT COUNT(*)
 FROM customer
 WHERE customer_id IN
 (
  SELECT customer_id
  FROM payment
  WHERE rental_id IN
  (
   SELECT rental_id
   FROM rental
   WHERE inventory_id IN
   (
    SELECT inventory_id
    FROM inventory
    WHERE film_id IN
    (
     SELECT film_id
     FROM film
     WHERE title = 'Blanket Beverly'
    )
   )
  )
 );