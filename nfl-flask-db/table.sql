CREATE TABLE test_table (
    col1 INT
    , col2 INT
);


SELECT
    *
FROM teams
WHERE full_name = 'Arizona Cardinals'

SELECT
    *
FROM games
WHERE week > 17
LIMIT 500

SELECT
    *
FROM logos
WHERE team_abr = 'CHI'