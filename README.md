# Spark-House-price-prediction

Use Hadoop ecosystem (Hortonwork) to build regression model to predict house price by PySpark

## Step 1 Import data to MySQL

### Create database
create database housesales
use housesales

### Create Table
CREATE TABLE house_sales (
	id INT NOT NULL,
	bedrooms INT NULL,
	bathrooms DECIMAL(4,2) NULL,
	sqft_living INT NULL,
	sqft_lot INT NULL,
	floors DECIMAL(4,2) NULL,
	waterfront INT NULL,
	view INT NULL,
	house_condition INT NULL,
	grade INT NULL,
	sqft_above INT NULL,
	sqft_basement INT NULL,
	yr_built INT NULL,
	yr_renovated INT NULL,
	zipcode INT NULL,
	latitude DECIMAL(7,4) NULL,
	longitude DECIMAL(7,4) NULL,
	sqft_living15 INT NULL,
	sqft_lot15 INT NULL,
	price INT NULL,
	PRIMARY KEY (id)
);

### Import data from csv to MySQL
LOAD DATA LOCAL INFILE  '/home/maria_dev/Project6004/kc_house_data.csv'
INTO TABLE house_sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

## Step 2 Import data to hive by Sqoop
### Create Hive table
CREATE TABLE house_price (
ID INT,
bedrooms INT,
bathrooms FLOAT,
sqft_living INT,
sqft_lot INT,
floors FLOAT,
waterfront INT,
view INT,
house_condition INT,
grade INT,
sqft_above INT,
sqft_basement INT,
yr_built INT,
yr_renovated INT,
zipcode INT,
latitude FLOAT,
longitude FLOAT,
sqft_living15 INT,
sqft_lot15 INT,
price INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
lines terminated by '\n' STORED AS TEXTFILE;

### Import data from MySQL to Hive
sudo -u hive sqoop import --connect jdbc:mysql://localhost/housesales --driver com.mysql.jdbc.Driver --table house_sales --hive-import

## Step 3 Use PySpark to read data in hive and build regression model predict house price
spark-submit house_price_prediction.py
