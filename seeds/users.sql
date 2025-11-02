
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    admin boolean DEFAULT false,
    password text
);

INSERT INTO users (name, email, admin, password) VALUES ('John', 'john@makers.tech', false, 'password1');
INSERT INTO users (name, email, admin, password) VALUES ('Oana', 'oana@makers.tech', true, 'pa$$word');
INSERT INTO users (name, email, admin, password) VALUES ('Jake', 'jake@makers.tech', false, '123456');
INSERT INTO users (name, email, admin, password) VALUES ('Nadia', 'nadia@makers.tech', false, 'qwerty');
