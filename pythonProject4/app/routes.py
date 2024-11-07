from flask import render_template, request, redirect, url_for, flash
from . import app

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/manga')
def manga():
    return render_template('Manga.html')

@app.route('/all_manga', methods=['GET', 'POST'])
def all_manga():
    if request.method == 'POST':
        # Process the form data (e.g., save to database, etc.)
        manga_name = request.form['manga_name']
        manga_genre = request.form['manga_genre']
        manga_price = request.form['manga_price']
        author = request.form['author']
        # Add your processing logic here
        flash('Manga updated successfully!', 'success')
        return redirect(url_for('all_manga'))
    return render_template('All_Manga.html')
@app.route('/authors')
def authors():
    return render_template('Authors.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        comments = request.form['comments']
        # Process the form data (e.g., save to database, send email, etc.)
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')