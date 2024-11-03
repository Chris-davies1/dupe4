from flask import Flask
from sales import sales_bp  # Import the sales blueprint
from .sales import sales

app = Flask(__name__)

# Register the sales blueprint
app.register_blueprint(sales_bp, url_prefix='/sales')


def get_db():
    if 'db' not in g or not is_connection_open(g.db):
        print("Re-establishing closed database connection.")
        g.db = pymysql.connect(
            # Database configuration
            # Configure MySQL
            host = 'y2w3wxldca8enczv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user = 'xx3y6i1bvtn9x2su',
            password = 'o28oyq7g4mf4ph0s',
            database = 'g0cd5yfzxmoyyg0p',
            cursorclass=pymysql.cursors.DictCursor  # Set the default cursor class to DictCursor
        )
    return g.db

def is_connection_open(conn):
    try:
        conn.ping(reconnect=True)  # PyMySQL's way to check connection health
        return True
    except:
        return False

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None and not db._closed:
        print("Closing database connection.")
        db.close()


