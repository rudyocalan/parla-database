use hikedb;
// clean db before re-importing test data
db.dropDatabase();

// load var labels is this script scope
load('/test-data/labels.js');
// load var users is this script scope
load('/test-data/users.js');
// load var ratings is this script scope
load('/test-data/ratings.js');
// load var hikes is this script scope
load('/test-data/hikes.js');


db.getCollection('labels').insert(labels);
db.getCollection('users').insert(users);
db.getCollection('ratings').insert(ratings);
db.getCollection('hikes').insert(hikes);