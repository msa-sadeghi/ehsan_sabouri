-- INSERT INTO employees VALUES 
-- ('12345', 'sara rezaei', 23),
-- ('12346', 'armin ahmadi', 12)
-- ;
-- INSERT INTO departments VALUES
-- (1, 'IT', 150000.00),
-- (2, 'HR', 90000.00)

-- INSERT INTO locations VALUES
-- 	('Tehran - saadat abad', 50),
-- 	('Shiraz - center', 40)

-- INSERT INTO works_in2 VALUES
-- 	('1234', 1, 'Tehran - saadat abad', '2022-01-01'),
-- 	('12345', 2, 'Shiraz - center', '2023-05-15'),
-- 	('12346', 1, 'Shiraz - center', '2023-03-15')

CREATE TABLE reports_to(
	subordinate_ssn VARCHAR(9),
	supervisior VARCHAR(9),
	PRIMARY KEY (subordinate_ssn),
	FOREIGN KEY (subordinate_ssn) REFER
	
)