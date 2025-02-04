from flask import Flask, render_template, request, url_for
from flask_babel import Babel, _

app = Flask(__name__)

# Configure the application to use Babel
app.config['LANGUAGES'] = ['en', 'fa']  # English and Persian
app.config['BABEL_DEFAULT_LOCALE'] = 'fa' # Default language is Persian

babel = Babel(app)

# Simulate some blog posts (you can replace this with a database or other data source)
blog_posts = [
    {'id': 1, 'title': 'Chiquita’s New Sunburst Gold Pineapple is as Good as Gold!', 'content': 'This is the content of the first blog post.'},
    {'id': 2, 'title': 'Second Blog Post', 'content': 'Content for the second blog post.'}
]
# Funct
# ion to get the current locale
def get_locale():
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Initialize Babel
babel.init_app(app, locale_selector=get_locale)

# Function to determine text direction
def get_direction(lang):
    return 'rtl' if lang == 'fa' else 'ltr'



@app.route('/')
def index():
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    return render_template('index.html', lang=lang, direction=direction)

@app.route('/blog')
def blog():
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    return render_template('blog.html', lang=lang, direction=direction, blog_posts=blog_posts)

@app.route('/blog/<int:post_id>')
def show_post(post_id):
    post = next(post for post in blog_posts if post['id'] == post_id)
    return render_template('blog_post.html', blog_post=post)

@app.route('/search')
def search():
    query = request.args.get('query')
    # Implement your search logic here
    results = f"نتایج جستجو برای: {query}" if query else "جستجویی انجام نشد."
    return render_template('search_results.html', query=query, results=results)

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('static', filename='en'))  # Should output "/?lang=en"
    app.run(debug=True)
