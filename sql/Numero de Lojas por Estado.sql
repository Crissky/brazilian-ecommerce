SELECT seller_state, COUNT(*)
FROM sellers
GROUP BY seller_state
ORDER BY COUNT(*) DESC