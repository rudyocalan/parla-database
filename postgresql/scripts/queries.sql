/**
 * Write a SQL query to return the total hikes of for each land types
 */
DROP VIEW IF EXISTS hikes_per_landtype;
CREATE VIEW hikes_per_landtype AS
SELECT
  landtypes.landtype,
  COUNT(hikes.hikeid) AS hikecount
FROM
  landtypes,
  hikes,
  hasalandtype
WHERE
  hasalandtype.hikeid = hikes.hikeid AND hasalandtype.landid = landtypes.landid
GROUP BY
  landtypes.landtype
ORDER BY
  hikecount;

/**
 * Write a SQL query to return the average rating per land types.
 * we want to see two fileds: 
 * landtype and rating (avg of all 1-5 ratings for this land type) 
 */
DROP VIEW IF EXISTS avg_rating_per_landtype;
CREATE VIEW avg_rating_per_landtype AS
SELECT
  landtypes.landtype,
  AVG(ratings.rating) as rating
FROM
  ratings,
  hasalandtype,
  landtypes
WHERE
  ratings.hikeid = hasalandtype.hikeid AND hasalandtype.landid = landtypes.landid
GROUP BY
  landtypes.landtype;

/**
 * TODO: Write a SQL query to return all hikes with 5 stars rated by at least 3 users
 */
