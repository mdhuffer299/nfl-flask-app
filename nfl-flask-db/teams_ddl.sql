DROP TABLE IF EXISTS teams;

CREATE TABLE IF NOT EXISTS teams (
    season INT
    , team VARCHAR(3)
    , nfl VARCHAR(3)
    , nfl_team_id INT
    , espn VARCHAR(3)
    , pfr VARCHAR(3)
    , pff VARCHAR(3)
    , pfflabel VARCHAR(3)
    , fo VARCHAR(5)
    , full_name VARCHAR(40)
    , location VARCHAR(30)
    , short_location VARCHAR(20)
    , nickname VARCHAR(20)
    , hyphenated VARCHAR(40)
    , sbr INT
    , sbr_wins VARCHAR(40)
    , sbr_name VARCHAR(40)
    , draft_kings VARCHAR(40)
    , teams_pkey SERIAL PRIMARY KEY
);