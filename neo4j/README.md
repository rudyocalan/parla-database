# Neo4j

Neo4j is a NoSQL database system, graph oriented.

Find out more about uses cases Neo4j is good for:
- https://neo4j.com/use-cases/

## Start Neo4j

Use the `docker-compose` provided:

```bash
docker-compose up -d
```

A web documentation can walk you thru using Graph databases:
- http://localhost:7474

Default credentials are:
- user: neo4j
- password: neo4j

You are asked to reset your password on first login.

> Feel free to follow the starting tutorial to get started with concepts of this kind of 
> database systems (Nodes, Relationship and properties).

## Using Cypher shell (Neo4j CLI)

Cypher is the query language for Neo4j. 

If you wish to interact with the database system using the cypher shell
rather than the web ui provided, you can run the cypher shell by running:

```bash
docker exec -it --tty neo4j-3.5 bin/cypher-shell
# >
# username: neo4j
# password: ********
# Connected to Neo4j 3.5.8 at bolt://localhost:7687 as user neo4j.
# Type :help for a list of available commands or :exit to exit the shell.
# Note that Cypher queries must end with a semicolon.
# neo4j> 
```
Credentials are by default:
- username: neo4j
- password: neo4j

## Restart

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
rm -rf data
# restart
docker-compose up -d
```
