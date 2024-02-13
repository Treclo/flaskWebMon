#!/bin/ksh

echo '.dump' |sqlite3 database.sql |sqlite3 repaired_database.sql
mv database.sql corruptDatabases/corrupt_database.sql_$(date "+%Y-%m-%d")
mv repaired_database.sql database.sql
