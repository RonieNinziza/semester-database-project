
CREATE DATABASE RN ;


CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    email TEXT,
    rating INTEGER,
    amount INTEGER
    );


CREATE TABLE models(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    names TEXT,
    size TEXT,
    gender TEXT
    );


CREATE TABLE payments(
    payment_id INTEGER PRIMARY KEY AUTO INCREMENT,
    payment_type TEXT 
    );

CREATE TABLE functions(
    event_id INTEGER PRIMARY KEY AUTO INCREMENT,
    event_type TEXT 
    );

CREATE TABLE receipts(
    c_id INTEGER,
    e_id INTEGER,
    m_id INTEGER,
    p_id INTEGER,
    FOREIGN KEY (c_id) REFERENCES customers(id),
    FOREIGN KEY (f_id) REFERENCES events(event_id),
    FOREIGN KEY (p_id) REFERENCES payments(payment_id),
    FOREIGN KEY (t_id) REFERENCES models(id)
    );