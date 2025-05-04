CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_first_name VARCHAR(50) NOT NULL,
    user_surname VARCHAR(50),
    user_username VARCHAR(50) UNIQUE NOT NULL,
    user_password_hash VARCHAR(200) NOT NULL,
    user_insert_datetime DATETIME NOT NULL DEFAULT GETDATE(),
    user_is_active BOOLEAN NOT NULL DEFAULT true,
)

CREATE TABLE files (
    file_id SERIAL PRIMARY KEY,
    file_user_id INTEGER NOT NULL,
    file_file_path VARCHAR (100) NOT NULL,
    file_file_extension VARCHAR(10) NOT NULL,
    file_description VARCHAR (100),
    file_insert_datetime DATETIME NOT NULL DEFAULT GETDATE(),
)

CREATE TABLE tokens (
    token_id SERIAL PRIMARY KEY,
    token_user_id INTEGER NOT NULL,
    token_expiration_date DATETIME NOT NULL,
    token_is_active BOOLEAN NOT NULL DEFAULT true,
    token_value VARCHAR(100) NOT NULL,
    token_insert_datetime DATETIME, NOT NULL DEFAULT GETDATE()
)