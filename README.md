# nfl-flask-app
This is an example Flask App that uses a postgres database as the backend database.
##### To Run App:
1. Install local postgres database using homebrew.
2. Set up virtual python environment and install requirements.txt
3. Include POSTGRES_DB_URL in your environment variables.
4. Run `psql dbname < ./nfl-flask-db/db_backup.txt` to load most recent database backup
5. Run App