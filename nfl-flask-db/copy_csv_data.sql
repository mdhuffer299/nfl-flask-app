COPY teams(season,team,nfl,nfl_team_id,espn,pfr,pff,pfflabel,fo,full_name,location,short_location,nickname,hyphenated,sbr,sbr_wins,sbr_name,draft_kings)
FROM '/Users/mhuffer-m1/Desktop/Projects/nfl-flask-app/raw-data/teams.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

COPY logos(team_abr, team_logo)
FROM '/Users/mhuffer-m1/Desktop/Projects/nfl-flask-app/raw-data/logos.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');