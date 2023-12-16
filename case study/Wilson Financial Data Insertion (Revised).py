import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1qaz!QAZ1qaz!QAZ",
    "database": "willson_financial"
}

conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()

# last name, first name, email, street address, state, zip code, enrollment date, enrollment time
clients_data = [
    ("Smith", "Jerry", "jerrysmith@gmail.com", "12 First Street", "San Bernardino", "California", "92325", "555-925-5476", "2023-01-01", "17:57"),
    ("King", "Ethan", "ethanking@gmail.com", "345 Broad Street", "Fontana", "California", "92407", "555-926-6987", "2023-04-01", "09:56"),
    ("Book", "Julie", "juliebook@gmail.com", "427 S Sparrow Ave", "Rialto", "California", "92407", "555-925-7829", "2023-07-25", "14:14"),
    ("McGuire", "Fred", "fredmcguire@gmail.com", "27 Crest Forest Dr", "Fontana", "California", "92336", "555-925-6934", "2023-01-10", "16:29"),
    ("Jensen", "Sally", "sallyjensen@gmail.com", "1254 Sparrow Circle", "Hesperia", "California", "92335", "555-926-0097", "2023-06-10", "14:01"),
    ("Pinkman", "Thomas", "thomaspinkman@gmail.com", "30 Pheasant Lane", "Big Bear", "California", "92399", "555-926-1121", "2023-03-10", "09:40"),
    ("Porter", "Grace", "graceporter@gmail.com", "28 Grass Valley Rd", "Palmdale", "California", "92325", "555-925-4747", "2023-09-10", "08:30"),
    ("Williams", "Christopher", "christopherwilliams@gmail.com", "678 Fairfield Dr", "Running Springs", "California", "92509", "555-925-9997", "2023-09-15", "10:15")
]

# balance, open date, open time, type (FK), client (FK)
accounts_data = [
    (7500, "2023-04-01", "16:47", 1, 6),
    (255, "2023-04-10", "09:49", 1, 2),
    (522, "2023-05-01", "08:16", 3, 4),
    (654, "2023-02-02", "09:19", 1, 1),
    (12214, "2023-01-05", "13:45", 2, 1),
    (1443, "2023-08-02", "14:14", 2, 3),
    (2100, "2023-01-15", "09:11", 3, 4),
    (3324, "2023-06-25", "08:23", 2, 5),
    (4056, "2023-10-20", "09:30", 1, 6),
    (2000, "2023-10-15", "10:15", 2, 7),
    (3499, "2023-09-27", "11:37", 3, 8)
]

# amount, date, time, type (FK), account (FK)
transactions_data = [
    (6000, "2023-05-08", "04:54:46", 2, 1),
    (120, "2023-12-30", "21:11:25", 2, 1),
    (1500, "2023-10-06", "09:33:11", 2, 1),
    (522, "2023-04-06", "08:48:31", 2, 1),
    (700, "2023-12-25", "23:43:04", 2, 2),
    (46, "2023-04-28", "08:08:17", 2, 2),
    (135, "2023-06-01", "06:57:57", 1, 2),
    (2000, "2023-06-17", "08:38:04", 2, 2),
    (1755, "2023-10-21", "08:38:13", 2, 2),
    (2368, "2023-08-24", "06:15:05", 2, 3),
    (4000, "2023-05-12", "05:06:15", 2, 3),
    (750, "2023-11-13", "12:08:46", 1, 3),
    (1443, "2023-08-16", "08:44:23", 2, 7),
    (50, "2023-11-01", "03:54:39", 1, 7),
    (75, "2023-01-20", "09:26:24", 2, 7),
    (123, "2023-03-02", "04:34:28", 2, 7),
    (211, "2023-05-01", "02:09:26", 2, 7),
    (34, "2023-09-14", "11:34:56", 3, 7),
    (89, "2023-06-28", "03:21:03", 1, 7),
    (777, "2023-03-26", "09:29:46", 2, 7),
    (500, "2023-06-16", "11:43:42", 2, 4),
    (55, "2023-06-23", "04:34:17", 2, 4),
    (75, "2023-10-23", "02:05:35", 1, 4),
    (80, "2023-09-19", "13:50:07", 2, 4),
    (45, "2023-06-20", "07:24:26", 2, 4),
    (333, "2023-06-23", "07:52:57", 1, 4),
    (20, "2023-04-12", "11:04:02", 2, 4),
    (10, "2023-04-24", "14:13:10", 2, 1),
    (125, "2023-11-23", "12:29:14", 1, 1),
    (225, "2023-10-25", "14:28:38", 2, 1),
    (30, "2023-03-28", "09:53:23", 2, 5),
    (22, "2023-03-28", "14:47:47", 2, 5),
    (65, "2023-03-14", "08:03:49", 2, 5),
    (10, "2023-03-07", "15:47:13", 2, 5),
    (15, "2023-03-15", "13:02:17", 3, 5),
    (93, "2023-03-07", "09:02:47", 2, 5),
    (58, "2023-03-14", "13:15:53", 2, 5),
    (26, "2023-03-13", "06:38:00", 2, 5),
    (60, "2023-03-05", "16:49:56", 1, 5),
    (57, "2023-03-20", "16:18:17", 2, 5),
    (78, "2023-10-16", "11:42:31", 2, 6),
    (21, "2023-08-19", "13:45:59", 2, 6),
    (34, "2023-05-15", "11:13:49", 2, 8),
    (2122, "2023-08-26", "09:38:13", 2, 8),
    (1202, "2023-07-03", "15:07:14", 2, 8),
    (374, "2023-09-15", "10:15:39", 2, 10),
    (325, "2023-09-17", "11:27:27", 2, 10),
    (334, "2023-09-23", "10:15:30", 2, 10),
    (319, "2023-09-26", "12:22:26", 2, 10),
    (322, "2023-09-02", "11:01:15", 2, 10),
    (326, "2023-09-09", "09:32:44", 2, 10),
    (200, "2023-09-27", "10:20:34", 1, 10),
    (150, "2023-09-28", "09:27:45", 1, 10),
    (200, "2023-09-29", "12:12:32", 1, 10),
    (100, "2023-09-29", "12:45:32", 2, 10),
    (662, "2023-10-15", "11:37:40", 2, 9),
    (567, "2023-10-16", "10:15:20", 2, 9),
    (575, "2023-10-02", "09:30:45", 2, 9),
    (565, "2023-10-05", "11:30:39", 2, 9),
    (577, "2023-10-09", "12:32:52", 2, 9),
    (553, "2023-10-15", "12:49:27", 2, 9),
    (400, "2023-10-17", "10:23:50", 2, 9),
    (340, "2023-10-18", "08:30:01", 2, 9),
    (400, "2023-10-19", "08:22:35", 1, 9),
    (340, "2023-10-19", "10:50:21", 1, 9)
]

# 1=withdrawal, 2=deposit, 3=transfer
transaction_type_data = [
    ("withdrawal",),
    ("deposit",),
    ("transfer",)
]

# 1=checking, 2=savings, 3=investment
account_type_data = [
    ("checking",),
    ("savings",),
    ("investment",)
]

insert_client_query = """
INSERT INTO client (client_last_name, client_first_name, email, street, city, state, zip, phone_number, client_join_date, client_join_time)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_account_type_query = """
INSERT INTO account_type (account_type_name)
VALUES (%s)
"""

insert_transaction_type_query = """
INSERT INTO transaction_type (transaction_type_name)
VALUES (%s)
"""

insert_account_query = """
INSERT INTO account (account_balance, account_open_date, account_open_time, account_type_id, client_id)
VALUES (%s, %s, %s, %s, %s)
"""

insert_transaction_query = """
INSERT INTO transaction (transaction_amount, transaction_date, transaction_time, transaction_type_id, account_id)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(insert_client_query, clients_data)

cursor.executemany(insert_account_type_query, account_type_data)

cursor.executemany(insert_transaction_type_query, transaction_type_data)

cursor.executemany(insert_account_query, accounts_data)

cursor.executemany(insert_transaction_query, transactions_data)

conn.commit()
