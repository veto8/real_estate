#!/bin/bash
echo "...Delete all tables from the postgres db"
docker exec -i postgres /bin/bash -c "export PGPASSWORD=dev2original && /usr/bin/psql -U root btredb -c  'DROP SCHEMA public CASCADE; CREATE SCHEMA public'"
echo "...Import init/btredb.sql.gz to postgress"
gunzip < init/btredb.sql.gz | docker exec -i postgres /bin/bash -c "export PGPASSWORD=dev2original && /usr/bin/psql -U root btredb"
