drop table if exists entries;
create table colleges (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);