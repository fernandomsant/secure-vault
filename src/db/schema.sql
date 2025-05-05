CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_first_name TEXT NOT NULL,
    user_surname TEXT,
    user_username TEXT UNIQUE NOT NULL,
    user_password_hash TEXT NOT NULL,
    user_is_active BOOLEAN NOT NULL DEFAULT 1
    user_insert_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE files (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_user_id INTEGER NOT NULL,
    file_file_path TEXT NOT NULL,
    file_file_extension TEXT NOT NULL,
    file_description TEXT,
    file_insert_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tokens (
    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
    token_user_id INTEGER NOT NULL,
    token_expiration_date DATETIME NOT NULL,
    token_is_active BOOLEAN NOT NULL DEFAULT 1,
    token_value TEXT NOT NULL,
    token_insert_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
