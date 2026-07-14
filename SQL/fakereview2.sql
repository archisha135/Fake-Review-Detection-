CREATE TABLE customer_reviews (

    customer_id VARCHAR(50),

    product_id VARCHAR(50),

    product_rating NUMERIC,

    review_comments TEXT,

    purchase_date DATE,

    return_date DATE );

	CREATE TABLE products (

    product_id VARCHAR(50),

    product_rating NUMERIC,

    review_comments TEXT,

    purchase_date DATE,

    return_date DATE,

    review_date DATE,

    category VARCHAR(100)

);
DROP TABLE IF EXISTS customer_reviews;
CREATE TABLE customer_reviews (

    customer_id VARCHAR(50),

    product_id VARCHAR(50),

    product_rating INTEGER,


    purchase_date VARCHAR(50),

    return_date VARCHAR(50),

    clean_review TEXT,

    duplicate_count INTEGER,

    duplicate_score INTEGER,

    max_similarity NUMERIC(10,2),

    similarity_score INTEGER,

    keyword_count INTEGER,

    keyword_score INTEGER,

    review_similarity_score NUMERIC(10,2),

    review_flag VARCHAR(50)

);
DROP TABLE IF EXISTS products;

CREATE TABLE products (

    product_id VARCHAR(50),

    product_rating INTEGER,

    

    purchase_date VARCHAR(100),

    return_date VARCHAR(100),

    review_date VARCHAR(100),

    category VARCHAR(100)

);

SELECT *
FROM products
LIMIT 10;