-- Script to rank country origins of bands, ordered by the total number of non-unique fans
-- The results display each country and the sum of its fans, sorted in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
