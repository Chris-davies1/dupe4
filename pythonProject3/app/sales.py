from flask import Blueprint, render_template

# Define Blueprint
sales = Blueprint('sales', __name__)

# Route example for testing
@sales.route('/show_sales')
def show_sales():
    return render_template('sales_data.html')