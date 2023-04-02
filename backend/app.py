import uvicorn
import sample_data
import os

from src import create_app, db
from flask_migrate import Migrate
from src.models import User, Consideration, BotLog
from dotenv import load_dotenv


def populate_db(table_names=('considerations', 'users', 'botlog')):
    """
    Populates the database with sample data
    : Args
        : tables - required tables to populate with data\
        otherwise empty tables will be created
    """
    def is_table_empty(table):
        return db.session.query(table).count() == 0
    
    data = (sample_data.considerations, sample_data.users, sample_data.bot_log)
    tables = (Consideration, User, BotLog)

    for table_name, table, s_data in zip(table_names, tables, data):
        if not is_table_empty(table):
            app.logger.info(f'{table_name} table is not empty. continuing...')
            continue

        for record in s_data:
            app.logger.info(f'{table_name} table is empty. Inserting sample record : {record}')
            db.session.add(table(**record))
            
    db.session.commit()


load_dotenv()
#print(os.getenv("DATABASE_URL"))
app = create_app('development')
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()
    populate_db()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Consideration=Consideration)

if __name__ == '__main__':
    uvicorn.run(app.wsgi_app, host="0.0.0.0", port=8000)


