#!/bin/bash
echo "Deleate all table from btredb"
export PGPASSWORD=dev2original
/usr/bin/psql -U root btredb -c  'DROP SCHEMA public CASCADE; CREATE SCHEMA public'

echo "...Import init/btredb.sql.gz to postgres"
gunzip < init/btredb.sql.gz | /usr/bin/psql -U root btredb
