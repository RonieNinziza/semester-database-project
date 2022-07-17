import csv

from cs50 import SQL



event = set()
payments_types = set()

open("models.db", "w").close()

db = SQL("sqlite:///models.db")

db.execute("""CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    rating INTEGER,
    amount INTEGER
    );""")

db.execute("""CREATE TABLE models(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    size TEXT,
    gender TEXT
    );""")

db.execute("""CREATE TABLE payments(
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_type TEXT 
    );""")

db.execute("""CREATE TABLE event(
    function_id INTEGER PRIMARY KEY AUTOINCREMENT,
    function_type TEXT 
    );""")

db.execute("""CREATE TABLE receipts(
    c_id INTEGER,
    e_id INTEGER,
    p_id INTEGER,
    m_id INTEGER,
    FOREIGN KEY (c_id) REFERENCES customers(id),
    FOREIGN KEY (e_id) REFERENCES event(event_id),
    FOREIGN KEY (p_id) REFERENCES payments(payment_id),
    FOREIGN KEY (m_id) REFERENCES models(id)
    );""")

with open("models.csv", "r")as file:
    readers = csv.DictReader(file)   
    
    for row in readers:
        event.add(row["event"])
        payments_types.add(row["Payment"])
        
    for line in payments_types:
        db.execute("""INSERT INTO payments(payment_type) VALUES(?);""",line)
        
    for line in event:
        db.execute("""INSERT INTO event(event_type) VALUES(?);""",line)

with open("models.csv", "r")as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        email = row["Email"]
        type = row["Type"]
        event = row["Event"]
        amount = row["Amount"]
        payment = row["Payment"]
        rating = row["Rating"]
        size = row["Size"]
        name = row["Name"]
        
        db.execute("""INSERT INTO customers(e-mail,rating,amount) VALUES(?,?,?);""", email,rating,amount)
        db.execute("""INSERT INTO models(name,size,type) VALUES(?,?,?);""", name,size,type)
        db.execute("""INSERT INTO receipts(c_id,m_id,p_id,e_id) VALUES((SELECT id FROM customers WHERE  email = ?),(SELECT event_id FROM event WHERE event_type = ?),(SELECT id FROM models WHERE  type = ?),(SELECT payment_id FROM payments WHERE  payment_type = ?));""", emails,event,types,payments)


 
        

       
