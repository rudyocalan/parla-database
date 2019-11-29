COPY users(userid,username)
FROM '/test-data/users.csv' DELIMITER ',' CSV HEADER;

COPY hikes(hikeid,hikename)
FROM '/test-data/hikes.csv' DELIMITER ',' CSV HEADER;

COPY labels(labelid,labelinfo)
FROM '/test-data/labels.csv' DELIMITER ',' CSV HEADER;

COPY landtypes(landid,landtype)
FROM '/test-data/landtypes.csv' DELIMITER ',' CSV HEADER;

COPY ratings(userid,hikeid,rating,timestamp)
FROM '/test-data/ratings.csv' DELIMITER ',' CSV HEADER;

COPY haslabeled(userid,hikeid,labelid,timestamp)
FROM '/test-data/hike-labels.csv' DELIMITER ',' CSV HEADER;

COPY hasalandtype(hikeid,landid)
FROM '/test-data/hike-landtypes.csv' DELIMITER ',' CSV HEADER;
