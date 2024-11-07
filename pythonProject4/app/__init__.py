from flask import Flask, g, render_template
from .app_factory import create_app
from flask import Blueprint

manga_bp = Blueprint('manga', __name__)

@manga_bp.route('/all_manga', methods=['GET', 'POST'])
def all_manga():
    return render_template('all_manga.html')

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment variable
# shows the app where to look for the routes
from . import routes

