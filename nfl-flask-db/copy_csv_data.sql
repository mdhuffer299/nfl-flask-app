COPY teams(season,team,nfl,nfl_team_id,espn,pfr,pff,pfflabel,fo,full_name,location,short_location,nickname,hyphenated,sbr,sbr_wins,sbr_name,draft_kings)
FROM '/Users/mhuffer-m1/Desktop/Projects/nfl-flask-app/raw-data/teams.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

COPY logos(team_abr, team_logo)
FROM '/Users/mhuffer-m1/Desktop/Projects/nfl-flask-app/raw-data/logos.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

COPY games(game_id,season,game_type,week,gameday,weekday,gametime,away_team,away_score,home_team,home_score,location,result,total,overtime,old_game_id,gsis,nfl_detail_id,pfr,pff,espn,away_rest,home_rest,away_moneyline,home_moneyline,spread_line,away_spread_odds,home_spread_odds,total_line,under_odds,over_odds,div_game,roof,surface,temp,wind,away_qb_id,home_qb_id,away_qb_name,home_qb_name,away_coach,home_coach,referee,stadium_id,stadium)
FROM '/Users/mhuffer-m1/Desktop/Projects/nfl-flask-app/raw-data/games.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

COMMIT;