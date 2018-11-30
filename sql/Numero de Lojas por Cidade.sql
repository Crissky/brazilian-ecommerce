SELECT seller_state, seller_city, COUNT(*)
FROM sellers
GROUP BY seller_state, seller_city
ORDER BY COUNT(*) DESC