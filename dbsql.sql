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

create table user(
    userid integer primary key autoincrement, 
    username text not null, 
    password text not null,
    gender text check(gender in ('male', 'female')),
    create_at timestamp default CURRENT_TIMESTAMP
);