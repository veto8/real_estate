#!/bin/bash
docker run -i --rm  --net=host -e PGPASSWORD=dev2original  postgres /usr/bin/pg_dump -h localhost -U root btredb | gzip -9 -f > init/btredb.sql.gz

