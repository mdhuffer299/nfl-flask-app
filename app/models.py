from app import db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db.database

class Teams(BaseModel):
    teams_pkey = PrimaryKeyField(null=False)
    season = IntegerField()
    team = CharField(3)
    nfl = CharField(3)
    nfl_team_id = IntegerField()
    espn = CharField(3)
    pfr = CharField(3)
    pff = CharField(3)
    pfflabel = CharField(3)
    fo = CharField(5)
    full_name = CharField(40)
    location = CharField(30)
    short_location = CharField(20)
    nickname = CharField(20)
    hyphenated = CharField(40)
    sbr = IntegerField()
    sbr_wins = CharField(40)
    sbr_name = CharField(40)
    draft_kings = CharField(40)

    @property
    def serialize(self):
        data = {
            'full_name': str(self.full_name).strip(),
            'espn': str(self.espn).strip(),
            'team': str(self.team).strip(),
            'season': self.season
        }

        return data

    def __repr__(self):
        return f"{self.full_name, self.espn, self.team, self.season}"

class Logos(BaseModel):
    logos_pkey = PrimaryKeyField(null=False)
    team_abr = CharField(3)
    team_logo = CharField(150)

    def __repr__(self):
        return f"{self.team_abr, self.team_logo}"

# class Teams(db.Model):
#     teams_pkey = db.Column(db.Integer, primary_key=True)
#     season = db.Column(db.Integer)
#     team = db.Column(db.String(3))
#     nfl = db.Column(db.String(3))
#     nfl_team_id = db.Column(db.Integer)
#     espn = db.Column(db.String(3))
#     pfr = db.Column(db.String(3))
#     pff = db.Column(db.String(3))
#     pfflabel = db.Column(db.String(3))
#     fo = db.Column(db.String(5))
#     full_name = db.Column(db.String(40))
#     location = db.Column(db.String(30))
#     short_location = db.Column(db.String(20))
#     nickname = db.Column(db.String(20))
#     hyphenated = db.Column(db.String(40))
#     sbr = db.Column(db.Integer)
#     sbr_wins = db.Column(db.String(40))
#     sbr_name = db.Column(db.String(40))
#     draft_kings = db.Column(db.String(40))
#
#     def __repr__(self):
#         return f"{self.full_name}"

# class Logos(db.Model):
#     logos_pkey = db.Column(db.Integer, primary_key=True)
#     team_abr = db.Column(db.String(3))
#     team_logo = db.Column(db.String(150))
#
#     def __repr__(self):
#         return f"{self.team_abr}"
