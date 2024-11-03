from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db
import pandas as pd

# Initialize Blueprint
sales = Blueprint('sales', __name__, template_folder='templates', static_folder='static')
