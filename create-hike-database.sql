/**
 * CREATES HIKE DATABASE TABLES
 * 
 * To execute the script:
 *  psql -U <groupeXX> -d groupeXXdb -a -f create-hike-database.sql
 */

/**
 * DROP TABLES, if exists to start fresh on every script exec.
 */

DROP TABLE IF EXISTS hikes CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS label CASCADE;
DROP TABLE IF EXISTS landtypes CASCADE;
DROP TABLE IF EXISTS ratings CASCADE;
DROP TABLE IF EXISTS hasbeenlabeled CASCADE;
DROP TABLE IF EXISTS hasalandtype CASCADE;

/**
 *
 * users: userid (int, primary key), username (text)
 *
 * hikes: hikeid (int, primary key), hikename (text)
 *
 * label: labelid (int, primary key), labelinfo (text)
 *
 * landtypes: landid (int, primary key), landtype (text)
 *
 * ratings: userid (int, foreign key), hikeid (int, foreign key), rating (numeric), timestamp (bigint, seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970)
 *
 * hasbeenlabeled: userid (int, foreign key), hikeid (int, foreign key), labelid (int, foreign key), timestamp (bigint, seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970).
 *
 * hasalandtype: hikeid (int, foreign key), landid (int, foreign key)
 */
CREATE TABLE hikes (
  hikeid INT PRIMARY KEY,
  hikename TEXT NOT NULL
);

CREATE TABLE users (
  userid INT PRIMARY KEY,
  username TEXT NOT NULL
);

CREATE TABLE label (
  labelid INT PRIMARY KEY,
  labelinfo TEXT NOT NULL
);

CREATE TABLE landtypes (
  landid INT PRIMARY KEY,
  landtype TEXT NOT NULL
);

CREATE TABLE ratings (
  userid INT REFERENCES users(userid) ON DELETE NO ACTION,
  hikeid INT REFERENCES hikes(hikeid) ON DELETE NO ACTION,
  rating NUMERIC NOT NULL CHECK (rating >= 0 AND rating <= 5),
  timestamp INT NOT NULL CHECK (timestamp >= 0),
  PRIMARY KEY (userid, hikeid)
);

CREATE TABLE hasbeenlabeled (
  userid INT REFERENCES users(userid) ON DELETE NO ACTION,
  hikeid INT REFERENCES hikes(hikeid) ON DELETE NO ACTION,
  labelid INT REFERENCES label(labelid) ON DELETE NO ACTION,
  timestamp INT NOT NULL CHECK (timestamp >= 0),
  PRIMARY KEY (userid, hikeid, labelid)
);

CREATE TABLE hasalandtype (
  hikeid INT REFERENCES hikes(hikeid),
  landid INT REFERENCES landtypes(landid),
  PRIMARY KEY (hikeid, landid)
);
