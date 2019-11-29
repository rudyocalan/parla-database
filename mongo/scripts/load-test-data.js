use hikedb

// load var hikes is this script scope
load('/test-data/hikes.js');

db.getCollection('hikes').insert(hikes);

