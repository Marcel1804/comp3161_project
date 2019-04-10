
/*======================= CompuStore Main Database ===================================================*/

create database CompuStore;
use CompuStore;

/* CustomerAccount(acc_id, email, password,  fname, lname, gender, date_of_birth, street, city, parish, telephone, created_on) */
create table CustomerAccount(
	acc_id int auto_increment not null,
	email varchar(100),
	password varchar(255),
	fname varchar(30),
	lname varchar(30),
	gender enum('Female','Male'),
	date_of_birth Date,
	street varchar(100),
	city varchar(100),
	parish varchar(100),
	telephone varchar(10),
	created_on Date,
	primary key(acc_id) 
);

/* CreditCardDetails(card_num, expiration_month, expiration_year, billing_street, billing_city, billing_parish) */
create table CreditCardDetails(
	card_num varchar(100),
	expiration_month tinyint(2),
	expiration_year smallint(4),
	billing_street varchar(100),
	billing_city varchar(100),
	billing_parish varchar(100),
	primary key(card_num) 
);

/*CustomerCreditCard(acc_id, card_num)*/
create table CustomerCreditCard(
	acc_id int,
	card_num varchar(100),
	primary key(acc_id, card_num),
	foreign key(acc_id) references CustomerAccount(acc_id) on DELETE cascade on UPDATE cascade,
	foreign key(card_num) references CreditCardDetails(card_num) on DELETE cascade on UPDATE cascade
);

/* Branch(br_id, name, street, city, parish, telephone) */
create table Branch(
	br_id int not null,
	name varchar(100), 
	street varchar(100),
	city varchar(100),
	parish varchar(100),
	telephone varchar(10),
	primary key(br_id)
);

/* Laptop(serial_num, model, brand, description, thumbnail, price) */
create table Laptop(
	serial_num varchar(100),
	model text,
	brand varchar(100),
	description text,
	thumbnail text,
	price double(10,2),
	primary key(serial_num) 
);

DELIMITER //
	CREATE PROCEDURE orderByPrice(IN ordr varchar(20))
	BEGIN
	IF ("ascending" like ordr) THEN SELECT * FROM Laptop order by price ASC;
	ELSE SELECT * FROM Laptop order by price DESC;
	END IF;
	END //
DELIMITER ;

DELIMITER //
	CREATE PROCEDURE getByName(IN Name varchar(100))
	BEGIN
	SELECT * FROM Laptop WHERE lower(name) LIKE CONCAT('%',Name,'%');
	END //
DELIMITER ;

DELIMITER //
	CREATE PROCEDURE getByModel(IN Model varchar(100))
	BEGIN
	SELECT * FROM Laptop WHERE lower(Model) LIKE CONCAT('%',Model,'%');
	END //
DELIMITER ;

DELIMITER //
	CREATE PROCEDURE getByBrand(IN Brand varchar(100))
	BEGIN
	SELECT * FROM Laptop WHERE lower(brand) LIKE  CONCAT('%',Brand,'%');
	END //
DELIMITER ;

/* CustomerCart(acc_id, item_count, value) */
create table CustomerCart(
	acc_id int,
	item_count int,
	value double(20,2),
	primary key(acc_id),
	foreign key(acc_id) references CustomerAccount(acc_id) on DELETE cascade on UPDATE cascade
);

/* CartItems(acc_id, serial_num, br_id, quantity, cost, purchasing, date_added) */
create table CartItems(
	acc_id int,
	serial_num varchar(100),
	br_id int,
	quantity int, 
	cost double(10, 2), 
	purchasing enum('Yes', 'No'),
	date_added date,
	primary key(acc_id),
	foreign key(acc_id) references CustomerCart(acc_id) on DELETE cascade on UPDATE cascade,
	foreign key(serial_num) references Laptop(serial_num) on DELETE cascade on UPDATE cascade,
	foreign key(br_id) references Branch(br_id) on DELETE cascade on UPDATE cascade
);

DELIMITER $$
	CREATE TRIGGER new_item
	AFTER INSERT ON CartItems
	FOR EACH ROW
	BEGIN
	UPDATE CustomerCart SET item_count = item_count + new.quantity, value = value + new.cost WHERE acc_id = new.acc_id;
	END $$
DELIMITER ;

DELIMITER $$
	CREATE TRIGGER update_item
	AFTER UPDATE ON CartItems
	FOR EACH ROW
	BEGIN
	UPDATE CustomerCart SET item_count = ((item_count - old.quantity) + new.quantity), value = ((value - old.cost) + new.cost) WHERE acc_id = new.acc_id;
	END $$
DELIMITER ;

/* Receipt(track_num, invoice) */
create table Receipt(
	track_num int,
	invoice blob,
	primary key(track_num)
);

/* Checkout(acc_id, track_num, total_cost, transaction_date) */
create table Checkout(
	acc_id int,
	track_num int,
	total_cost double(20,2),
	transaction_date date,
	primary key(acc_id, track_num),
	foreign key(acc_id) references CustomerCart(acc_id) on DELETE cascade on UPDATE cascade,
	foreign key(track_num) references Receipt(track_num) on DELETE cascade on UPDATE cascade
);

/* PurchasedItems(pur_id, acc_id, serial_num, br_id, quantity, cost, date_purchased) */
create table PurchasedItems(
	pur_id int auto_increment not null,
	acc_id int,
	serial_num varchar(100),
	br_id int,
	quantity int,
	cost double(20,2),
	date_purchased date,
	primary key(pur_id),
	foreign key(acc_id) references CustomerCart(acc_id) on DELETE cascade on UPDATE cascade,
	foreign key(serial_num) references Laptop(serial_num) on DELETE cascade on UPDATE cascade,
	foreign key(br_id) references Branch(br_id) on DELETE cascade on UPDATE cascade
);

DELIMITER $$
	CREATE TRIGGER Item_Purchased
	AFTER DELETE ON CartItems
	FOR EACH ROW
	BEGIN
	IF ('Yes' like old.purchasing) THEN INSERT INTO PurchasedItems VALUES (old.acc_id, old.serial_num, old.br_id, old.quantity, old.cost, curtime());
	ELSE UPDATE CustomerCart SET item_count = (item_count - old.quantity), value = (value - old.cost) WHERE acc_id = old.acc_id;
	END IF;
	END $$
DELIMITER ;

/* WriteReview(acc_id, serial_num, rev_text, date_written) */
create table WriteReview(
	acc_id int,
	serial_num varchar(100),
	rev_text text,
	date_written date,
	primary key(acc_id, serial_num),
	foreign key(acc_id) references CustomerAccount(acc_id) on DELETE cascade on UPDATE cascade,
	foreign key(serial_num) references Laptop(serial_num) on DELETE cascade on UPDATE cascade
);

/* Warehouse(wh_id, street, city, parish, telephone) */
create table Warehouse(
	wh_id int,
	street varchar(100),
	city varchar(100),
	parish varchar(100),
	telephone varchar(10),
	primary key(wh_id)
);

/* Stores(wh_id, serial_num, quantity) */
create table Stores(
	wh_id int,
	serial_num varchar(100),
	quantity int,
	primary key(wh_id, serial_num),
	foreign key(wh_id) references Warehouse(wh_id) on DELETE cascade on UPDATE cascade,
	foreign key(serial_num) references Laptop(serial_num) on DELETE cascade on UPDATE cascade
);





/*======================= Branch1 Database ===================================================*/

create database Branch1;
use Branch1;

/* Laptop(serial_num, model, brand, description, thumbnail) */
create table Laptop(
	serial_num varchar(100),
	model text,
	brand varchar(100),
	description text,
	thumbnail text,
	primary key(serial_num) 
);

/* ItemsInStock(serial_num, quantity) */
create table ItemsInStock(
	serial_num varchar(100),
	quantity int,
	primary key(serial_num)
);

create table ItemSold(
	serial_num varchar(100),
	amount int,
	primary key(serial_num),
	foreign key(serial_num) references ItemsInStock(serial_num) on DELETE cascade on UPDATE cascade
);

DELIMITER //
	CREATE PROCEDURE purchaseItem(IN serial varchar(100), amt int)
	BEGIN
	UPDATE ItemsInStock SET quantity = (quantity - amt) WHERE serial_num = serial;
	IF EXISTS (SELECT serial_num FROM ItemSold WHERE serial_num = serial LIMIT 1) THEN
		UPDATE ItemSold SET amount = (amount + amt) WHERE serial_num = serial;
	ELSE
		INSERT INTO ItemSold VALUES(serial, amt);
	END IF;
	END //
DELIMITER ;


/*======================= Branch2 Database ===================================================*/

create database Branch2;
use Branch2;

/* Laptop(serial_num, model, brand, description, thumbnail) */
create table Laptop(
	serial_num varchar(100),
	model text,
	brand varchar(100),
	description text,
	thumbnail text,
	primary key(serial_num) 
);

/* ItemsInStock(serial_num, quantity) */
create table ItemsInStock(
	serial_num varchar(100),
	quantity int,
	primary key(serial_num)
);

create table ItemSold(
	serial_num varchar(100),
	amount int,
	primary key(serial_num),
	foreign key(serial_num) references ItemsInStock(serial_num) on DELETE cascade on UPDATE cascade
);

DELIMITER //
	CREATE PROCEDURE purchaseItem(IN serial varchar(100), amt int)
	BEGIN
	UPDATE ItemsInStock SET quantity = (quantity - amt) WHERE serial_num = serial;
	IF EXISTS (SELECT serial_num FROM ItemSold WHERE serial_num = serial LIMIT 1) THEN
		UPDATE ItemSold SET amount = (amount + amt) WHERE serial_num = serial;
	ELSE
		INSERT INTO ItemSold VALUES(serial, amt);
	END IF;
	END //
DELIMITER ;


/*======================= Branch3 Database ===================================================*/

create database Branch3;
use Branch3;

/* Laptop(serial_num, model, brand, description, thumbnail) */
create table Laptop(
	serial_num varchar(100),
	model text,
	brand varchar(100),
	description text,
	thumbnail text,
	primary key(serial_num) 
);

/* ItemsInStock(serial_num, quantity) */
create table ItemsInStock(
	serial_num varchar(100),
	quantity int,
	primary key(serial_num)
);

create table ItemSold(
	serial_num varchar(100),
	amount int,
	primary key(serial_num),
	foreign key(serial_num) references ItemsInStock(serial_num) on DELETE cascade on UPDATE cascade
);

DELIMITER //
	CREATE PROCEDURE purchaseItem(IN serial varchar(100), amt int)
	BEGIN
	UPDATE ItemsInStock SET quantity = (quantity - amt) WHERE serial_num = serial;
	IF EXISTS (SELECT serial_num FROM ItemSold WHERE serial_num = serial LIMIT 1) THEN
		UPDATE ItemSold SET amount = (amount + amt) WHERE serial_num = serial;
	ELSE
		INSERT INTO ItemSold VALUES(serial, amt);
	END IF;
	END //
DELIMITER ;

use CompuStore;