use my_database;


create table if not exists my_table(
    user_id int not null auto_increment,
    user_name varchar(250),
    primary key(user_id)
);

insert into my_table (user_name)
values('sergei'),
      ('john');

select user_name as user from my_table
where user_id = 1;

create table if not exists users(
    id int not null auto_increment,
    username varchar(250),
    fullname varchar(250),
    email varchar(30),
    hashed_password varchar(70),
    disabled bool default False,
    language varchar(15),
    entry_date date default (CURRENT_DATE),
    primary key(id)
);

show tables;
