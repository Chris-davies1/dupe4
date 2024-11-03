from flask import Flask, g
from .app_factory import create_app
from .db_connect import close_db, get_db
from .sales import sales  # Import the sales blueprint

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment variable

# Register the sales blueprint
app.register_blueprint(sales, url_prefix='/sales')

@app.before_request
def before_request():
    g.db = get_db()

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)