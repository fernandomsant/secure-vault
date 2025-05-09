CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    user_first_name NVARCHAR(255) NOT NULL,
    user_surname NVARCHAR(255),
    user_username NVARCHAR(255) NOT NULL UNIQUE,
    user_password_hash NVARCHAR(255) NOT NULL,
    user_is_active BIT NOT NULL DEFAULT 1,
    user_insert_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);

CREATE TABLE files (
    file_id INT IDENTITY(1,1) PRIMARY KEY,
    file_user_id INT NOT NULL,
    file_file_path NVARCHAR(MAX) NOT NULL,
    file_file_extension NVARCHAR(10) NOT NULL,
    file_description NVARCHAR(MAX),
    file_insert_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    FOREIGN KEY (file_user_id) REFERENCES users(user_id)
);

CREATE TABLE tokens (
    token_id INT IDENTITY(1,1) PRIMARY KEY,
    token_user_id INT NOT NULL,
    token_expiration_date DATETIME2 NOT NULL,
    token_is_active BIT NOT NULL DEFAULT 1,
    token_value NVARCHAR(255) NOT NULL,
    token_insert_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    FOREIGN KEY (token_user_id) REFERENCES users(user_id)
);
