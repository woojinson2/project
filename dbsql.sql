-- create table user(

--     userid integer primary key autoincrement,
--     username text not null,
--     password text not null,
--     email text not null,
--     gender text check(gender in ('male','female')),
--     create_at timestamp defalult create_timestamp
-- );

-- insert into user(username, password, email, gender)
-- values('test','123','test@gmail.com','male')

CREATE TABLE user (
    userid INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('male', 'female')), -- 수정된 부분
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
