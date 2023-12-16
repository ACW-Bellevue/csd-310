import mysql.connector

host = "localhost"
user = "root"
password = "1qaz!QAZ1qaz!QAZ"
database_name = "Willson_Financial"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database="Willson_Financial"
)

cursor = connection.cursor()

create_client_table = """
CREATE TABLE client(  
    client_id INT NOT NULL AUTO_INCREMENT,
    client_last_name VARCHAR(25) NOT NULL,
    client_first_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(60) NOT NULL,
    state VARCHAR(20) NOT NULL,
    zip INT(5) NOT NULL,
    phone_number VARCHAR(12) NOT NULL,
    client_join_date DATE NOT NULL,
    client_join_time TIME NOT NULL,
    PRIMARY KEY(client_id)
)
"""

create_account_type_table = """
CREATE TABLE account_type (  
    account_type_id INT NOT NULL AUTO_INCREMENT,
    account_type_name VARCHAR(25) NOT NULL,
    PRIMARY KEY(account_type_id)
)
"""

create_account_table = """
CREATE TABLE account(  
    account_id INT NOT NULL AUTO_INCREMENT,
    account_type_id INT,
    account_balance DOUBLE NOT NULL,
    account_open_date DATE NOT NULL,
    account_open_time TIME NOT NULL,
    client_id INT,
    PRIMARY KEY(account_id),
    FOREIGN KEY(account_type_id) REFERENCES account_type (account_type_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
)
"""

create_transaction_type_table = """
CREATE TABLE transaction_type (  
    transaction_type_id INT NOT NULL AUTO_INCREMENT,
    transaction_type_name VARCHAR(15) NOT NULL,
    PRIMARY KEY(transaction_type_id)
)
"""

create_transaction_table = """
CREATE TABLE transaction (  
    transaction_id INT NOT NULL AUTO_INCREMENT,
    transaction_type_id INT,
    transaction_amount DOUBLE NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_time TIME NOT NULL,
    account_id INT,
    PRIMARY KEY(transaction_id),
    FOREIGN KEY(transaction_type_id) REFERENCES transaction_type (transaction_type_id),
    FOREIGN KEY(account_id) REFERENCES account (account_id)
)
"""

cursor.execute(create_client_table)
cursor.execute(create_account_type_table)
cursor.execute(create_account_table)
cursor.execute(create_transaction_type_table)
cursor.execute(create_transaction_table)

connection.commit()

cursor.close()
connection.close()

