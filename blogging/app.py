from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and configure SQLite
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Post model for storing blog posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def home():
    posts = Post.query.all()  # Fetch all posts from the database
    return render_template('home.html', posts=posts)

# Route to create a new post
@app.route('/post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Add new post to the database
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post.html')

# Route to search for posts by title
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    search_results = Post.query.filter(Post.title.like(f"%{query}%")).all()
    return render_template('home.html', posts=search_results)

# Route to delete a post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)