CREATE TABLE books(
	isbn VARCHAR(20) PRIMARY KEY,
	title VARCHAR(255),
	author VARCHAR(255),
	qty_in_stock INT,
	price DECIMAL(10,2),
	year_published INT
);
INSERT INTO books VALUES('1dd3d', 'harry potter2', 'j.k.row', 100, 1001, 2002)
SELECT * FROM books
CREATE TABLE customers(
	cid INT PRIMARY KEY,
	cname VARCHAR(255),
	address TEXT
);
INSERT INTO customers VALUES (2, 'armin', 'shiraz')
SELECT * FROM customers
CREATE TABLE orders(
	order_id SERIAL PRIMARY KEY,
	cid INT REFERENCES customers(cid),
	order_date DATE,
	ship_date DATE,
	cardnum VARCHAR(20)
);
INSERT INTO orders VALUES (DEFAULT, 2, '2025-01-01', '2025-01-02', '1234567')
CREATE TABLE order_items(
	order_id INT REFERENCES orders(order_id),
	isbn VARCHAR(20) REFERENCES books(isbn),
	qty INT,
	PRIMARY KEY (order_id, isbn)
);
INSERT INTO order_items VALUES
(1, '123d', 2),
(1, '1dd3d', 1)