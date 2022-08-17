DROP TABLE IF EXISTS teams;

CREATE TABLE IF NOT EXISTS logos
(
    team_abr VARCHAR(3)
    , team_logo VARCHAR(150)
    , logos_pkey SERIAL PRIMARY KEY
);