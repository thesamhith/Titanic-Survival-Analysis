SELECT name,
    age,
    age_category,
    sex,
    pclass,
    ship_class,
    survived,
    survivor
FROM titanic_data;
-- Survival rate by sex and passenger class
SELECT sex,
    ship_class,
    COUNT(*) AS passengers,
    ROUND(AVG(survived)::numeric, 3) AS survival_rate
FROM titanic_data
GROUP BY sex,
    ship_class
ORDER BY ship_class,
    sex;
-- Overall survival rate by passenger class
SELECT ship_class,
    COUNT(*) AS passengers,
    ROUND(AVG(survived)::numeric, 3) AS survival_rate
FROM titanic_data
GROUP BY ship_class
ORDER BY ship_class;