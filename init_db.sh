psql -U postgres -c "CREATE DATABASE testdb;"
psql -U postgres -d testdb -c "CREATE TABLE counter (id serial,count integer); INSERT INTO counter (count) VALUES (0);"

