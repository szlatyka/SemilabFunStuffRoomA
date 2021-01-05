CREATE TABLE groups (
    Id   INTEGER PRIMARY KEY AUTOINCREMENT
                 NOT NULL,
    Name STRING
);

CREATE TABLE users (
    Id      INTEGER PRIMARY KEY AUTOINCREMENT
                    NOT NULL,
    Name    STRING,
    [Group] INTEGER REFERENCES groups (Id) ON DELETE SET NULL
);

CREATE TABLE questions (
    Id       INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL,
    Question STRING,
    Image    BLOB,
    Answer   STRING
);