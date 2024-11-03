@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, description, cover_image FROM books")
    books = cursor.fetchall()
    cursor.close()
    return render_template('books.html', books=books)

@app.route('/authors')
def authors():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, biography FROM authors")
    authors = cursor.fetchall()
    cursor.close()
    return render_template('authors.html', authors=authors)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)