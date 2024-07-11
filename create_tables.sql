create table if not exists users (
    id serial primary key,
    fullname varchar(100),
    email varchar(100) unique
);

create type status_type as enum ('new', 'in progress', 'completed');

create table if not exists status (
    id serial primary key,
    name status_type unique
);

create table if not exists tasks (
    id serial primary key,
    title varchar(100),
    desription text,
    status_id int,
    user_id int,
    foreign key (status_id) references status (id) on update cascade on delete set null,
    foreign key (user_id) references users (id) on update cascade on delete set null
);