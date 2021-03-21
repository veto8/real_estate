#!/bin/bash
export PGPASSWORD=dev2original
/usr/bin/psql -U root btredb -c  'DROP SCHEMA public CASCADE; CREATE SCHEMA public'
echo "...Import init/btredb.sql.gz to postgress"
gunzip < init/btredb.sql.gz | /usr/bin/pgsql -U root btredb
