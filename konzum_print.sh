#!/usr/bin/env sh

sqlite3 -column -header konzum.db "select * from products"
