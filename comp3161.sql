create database compustore;
create database branch1;
create database branch2;
create database brabch3;
use compustore;


/*======================= CREATING TABLES ===================================================*/

/* customer(cus_id, fname, lname, age, gender, date_of_birth, street, city, parish, telephone) */
create table customer(
	cus_id int auto_increment not null,
	fname varchar(20),
	lname varchar(20),
	age int,
	gender varchar(20),
	date_of_birth Date,
	street varchar(20),
	city varchar(20),
	parish varchar(20),,
	telephone varchar(50),

	primary key(cust_id) 
);

/* customerAccount(acc_id, cus_id) */
create table customerAccount(
	acc_id varchar(5),
	cus_id varchar(3),
	primary key(acc_id,cus_id),
	foreign key(acc_id) references account(acc_id) on delete cascade on update cascade,
	foreign key(cus_id) references customer(cus_id) on delete cascade on update cascade
);

/* account(acc_id, email, password, created_on) */
create table account(
	acc_id int auto_increment not null,
	email varchar(20),
	password varchar(255),
	created_on Date,
	primary key(acc_id) 
);

/*creditCard(acc_id, card_num)*/
create table creditCard(
	acc_id varchar(5),
	card_num varchar(3),
	primary key(acc_id,card_num),
	foreign key(acc_id) references account(acc_id) on delete cascade on update cascade,
	foreign key(card_num) references creditCardDetails(card_num) on delete cascade on update cascade
);

/*creditCardDetails(card_num, expiration_date, cvc, billing_street, billing_city, billing_parish)*/
create table creditCardDetails(
	card_num int,
	expiration_date Date,
	cvc varchar(255),
	billing_street varchar(20),
	billing_city varchar(20),
	billing_parish varchar(20),
	primary key(card_num) 
);

create table branch(
br_id varchar(20) not null,
name varchar(20), 
street varchar(20),
city varchar(20),
parish varchar(20),
telephone int(10),
primary key(br_id)
);


create table purchase(
acc_id int(10) not null,
br_id int(10),
serial_num int(10),
date_purchased date


)

/*purchaseItem(pi_id, br_id, acc_id)

/*laptop(serial_num, model, brand, description, image)*/
create table laptop(
	serial_num int,
	model varchar(255),
	brand varchar(20),
	description varchar(20),
	image varchar(20),
	primary key(serial_num) 
);

/* customerCart(cart_id, name) */
create table customerCart(
	cart_id varchar(5),
	name varchar(3),
	primary key(acc_id),
);

/* addToCart(cart_id, acc_id, br_id, serial_num, date_added) */
create table addToCart(
	cart_id varchar(5),
	acc_id varchar(3),
	br_id varchar(3),
	primary key(acc_id,card_num),
	foreign key(acc_id) references account(acc_id) on delete cascade on update cascade,
	foreign key(card_num) references creditCardDetails(card_num) on delete cascade on update cascade
);


create database branch1;
use branch1;


create table sells(
serial_num int(10) not null, 
price int(10), 
quantity int(10),
primary key(serial_num)
);



create database branch2;
use branch1;


create table sells(
serial_num int(10) not null, 
price int(10), 
quantity int(10),
primary key(serial_num)
);


create database branch2;
use branch1;


create table sells(
serial_num int(10) not null, 
price int(10), 
quantity int(10),
primary key(serial_num)
);





