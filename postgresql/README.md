# PostgreSQL

PostgreSQL is a relationnal database system.

This is a development setup to play around with SQL.

## PgAdmin

PgAdmin is a simple web app providing a UI to manage your postgreSQL.

## Start postgreSQL and PgAdmin

Use the `docker-compose` file provided:

```bash
# Create a docker network for pgadmin to contact postgresql
docker networks create pgadmin
# Start both PostgreSQL and PgAdmin in background
docker-compose up -d
```

You should be able to access PgAdmin on http://localhost:8040/
usermail: arla@sigl.fr
password: sigl2020

For postgreSQL instance running locally, credentials are:
user: sigl2020
password: sigl2020

Once logged in add the local postgres:
1. Add server
2. Enter a connection name (e.g. local)
![create-server](doc/create-server.png)
3. Add the PostgreSQL containers info (user, password are both sigl2020)
![create-server-connection](doc/create-server-connection.png)


## Use PosgreSQL CLI

> Note: You should have your `docker-compose`'s container up and running

If you wish to visualized your data directly using postgres CLI,
you can enter the PostgreSQL running container:

```bash
docker exec -it postgres-12 psql --username sigl2020 --password
# enter sigl2020 as password
# >
# Password: 
# psql (12.1)
# Type "help" for help.
# 
# sigl2020=# 
```

## Restarting postgreSQL and PgAdmin

To restart without data loss:
```bash
docker-compose down
# ...
docker-compose up -d
```

To restart and wipe out all data:
```bash
docker-compose down
# remove data volumes, you might need sudo
rm -rf data pgadmin
# restart
docker-compose up -d
```
