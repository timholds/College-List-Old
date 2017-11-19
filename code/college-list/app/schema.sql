drop table if exists users;
create table users (
  id integer primary key AUTOINCREMENT ,
  nickname text not null,
  email text not null,
  college text not null
);


drop table if exists college;
create table college (
  id integer primary key AUTOINCREMENT ,
  CollegeName text not null
);

