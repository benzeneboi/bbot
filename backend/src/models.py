from . import db
from sqlalchemy.ext.hybrid import hybrid_property
import sqlalchemy as sa
import datetime

def define_delta_time_column(game_date_time, curr_date_time):
    delta_time = sa.column(sa.Interval, nullable=False)
    delta_time = delta_time.column_property(sa.func.coalesce(sa.func.timezone('UTC', game_date_time) - sa.func.timezone('UTC', curr_date_time), datetime.timedelta(0)))
    return delta_time

class BotLog(db.Model):
    """Logs the state of the bot"""
    __tablename__ = 'botlog'
    id = db.Column(db.Integer, primary_key=True)
    started = db.Column(db.DateTime)
    stopped = db.Column(db.DateTime)
    error = db.Column(db.Boolean)

class Consideration(db.Model):
    """shows all recently considered bets"""
    __tablename__ = 'considerations'
    id = db.Column(db.Integer, primary_key=True)
    team_1 = db.Column(db.String(40))
    team_2 = db.Column(db.String(40))
    sport = db.Column(db.String(40))
    game_date_time = db.Column(db.DateTime(timezone=True))#db.Column(db.String)#
    curr_date_time = db.Column(db.DateTime(timezone=True), server_default=sa.text('NOW()'))#db.Column(db.String)
    #notified = db.Column(db.Boolean)
    #game_status = db.Column(db.String(20)) # passed/upcoming
    #sa.Interval()
    #sa.DateTime()
    bet_window = db.Column(db.Integer)
    
    

    @hybrid_property
    def should_bet(self):
        return self.game_date_time- self.curr_date_time < self.bet_window

    @hybrid_property
    def game_status(self):
        assert self.game_date_time is not None and self.curr_date_time is not None
        if self.game_date_time - self.curr_date_time <= 0:
            return "passed"
        return "upcoming"

    @hybrid_property
    def time_delta(self):
        if self.game_date_time is not None and self.curr_date_time is not None:
            return self.game_date_time - self.curr_date_time
        return 0

        #return self.game_date_time - self.curr_date_time

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(
        db.String(64), unique=True, index=True
    )

    def __repr__(self):
        return f"<User {self.email} >"