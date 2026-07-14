SELECT

    category,

    COUNT(*) AS total_products

FROM products

GROUP BY category

ORDER BY total_products DESC;

SELECT

    c.customer_id,

    c.product_id,

    c.purchase_date,

    p.review_date,

    p.category,

    c.review_similarity_score

FROM customer_reviews c

JOIN products p

ON c.product_id = p.product_id;

SELECT

    product_id,

    category,

    purchase_date,

    review_date,

    (review_date - purchase_date) AS review_gap,

    CASE

        WHEN category IN ('Books','Kindle_Store')
             AND (review_date - purchase_date) < 7
        THEN 100

        WHEN category = 'Clothing_Shoes_and_Jewelry'
             AND (review_date - purchase_date) < 2
        THEN 80

        WHEN category = 'Movies_and_TV'
             AND (review_date - purchase_date) = 0
        THEN 30

        ELSE 0

    END AS timing_fraud_score

FROM products;

select * from