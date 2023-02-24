import uvicorn
import sample_data
import os

from backend import create_app, db
from flask_migrate import Migrate
from betbot_backend.models import User, Consideration, BotLog
from dotenv import load_dotenv

def populate_db(tables=('Consideration', 'User', 'BotLog')):
    """
    Populates the database with sample data
    : Args
        : tables - required tables to populate with data\
        otherwise empty tables will be created
    """
    for record in sample_data.considerations:
        # keys in each record should match model attribute names
        db.session.add(Consideration(**record)) # d={'team_1': '', ...}

    for record in sample_data.users:
        db.session.add(User(**record))

    for record in sample_data.bot_log:
        db.session.add(BotLog(**record))
    
    db.session.commit()

load_dotenv()
print(os.getenv("DATABASE_URL"))
app = create_app('development')



#dispatcher = DispatcherMiddleware(app.wsgi_app, {})
#run_simple('0.0.0.0', 5000, dispatcher, use_reloader=False, use_evalex=False)

migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()
    populate_db()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Consideration=Consideration)

if __name__ == '__main__':
    #run_simple('0.0.0.0', 5000, dispatcher, use_reloader=False, use_evalex=False)
    #app()
    #app.run(host='0.0.0.0')
    #app.wsgi_app = DispatcherMiddleware(app.wsgi_app)
    uvicorn.run(app.wsgi_app, host="0.0.0.0", port=8000)


