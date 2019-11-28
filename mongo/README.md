# MongoDB

MongoDB is a NoSQL database, document oriented.

Find out more about some use cases Mongo is good for here:
- https://www.mongodb.com/use-cases

## Start Mongo and mongo-express

Use the `docker-compose` provided:

```bash
# create a network for mongo and mongo-express
docker network create mongo
# start containers
docker-compose up -d
```

You can visualize your (empty) local mongo using mongo-express on
http://localhost:8081/

## Using MongoDB shell (CLI)

> Note: You should have your `docker-compose`'s container up and running

If you wish to visualized your data directly using MongoDB shell (CLI),
you can enter the MongoDB running container:

```bash
docker exec -it mongo-4 mongo --username sigl2020 --password sigl2020
# >
# MongoDB shell version v4.0.13
# ...
# > 
```

Mongo CLI doc can be found on mongodb website:
- https://docs.mongodb.com/manual/mongo/#working-with-the-mongo-shell


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
