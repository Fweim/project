-- CREATE TABLE IF NOT EXISTS product (
--     product_id INT NOT NULL,
--     name varchar(250) NOT NULL,
--     PRIMARY KEY (product_id)
-- );

CREATE TABLE IF NOT EXISTS model_cards (
    id serial NOT NULL PRIMARY KEY,
    cards json NOT NULL
);