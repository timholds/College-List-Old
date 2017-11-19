drop table if exists users;
create table users (
  id integer primary key AUTOINCREMENT ,
  title text not null,
  email text not null,
  'College' text not null
);

drop table if exists usersnocollege;
create table usersnocollege (
  id integer primary key AUTOINCREMENT ,
  title text not null,
  'College' text
);

drop table if exists college_no_title;
create table college_no_title (
  id integer primary key AUTOINCREMENT ,
  title text not null
);

drop table if exists college;
create table college (
  id integer primary key AUTOINCREMENT ,
  'CollegeName' text not null
);