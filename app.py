from flask import Flask, render_template, request, url_for
from flask_babel import Babel, _
import re

app = Flask(__name__)

# Configure the application to use Babel
app.config['LANGUAGES'] = ['en', 'fa']  # English and Persian
app.config['BABEL_DEFAULT_LOCALE'] = 'fa' # Default language is Persian

babel = Babel(app)

# Function to generate slugs from titles
def generate_slug(title):
    # print(re.sub(r'\s+', '-', title.strip()).lower())
    return re.sub(r'\s+', '-', title.strip()).lower()

# Blog data including latest blog as part of the list
blog_posts = [
    {
        "title": "عنوان مقاله ویژه",
        "image": "static/images/featured-blog.jpg",
        "link": "/blog/latest",
        "description": "توضیح کوتاه درباره این مقاله ویژه. اطلاعات مفید و خواندنی.",
        "tags": ["ویژه", "مهم"],
        "date": "12 بهمن 1402",
        "reading_time": "5 دقیقه"
    },
    {
        "title": "مقاله ۱",
        "image": "static/images/blog1.jpg",
        "link": "/blog/1",
        "description": "توضیح مختصر درباره مقاله ۱.",
        "tags": ["تکنولوژی", "کسب و کار"],
        "date": "10 بهمن 1402",
        "reading_time": "4 دقیقه"
    },
    {
        "title": "مقاله ۲",
        "image": "static/images/blog2.jpg",
        "link": "/blog/2",
        "description": "نگاهی به جدیدترین روندهای طراحی.",
        "tags": ["طراحی", "خلاقیت"],
        "date": "8 بهمن 1402",
        "reading_time": "6 دقیقه"
    },
    {
        "title": "مقاله ۳",
        "image": "static/images/blog3.jpg",
        "link": "/blog/3",
        "description": "نکات مهم برای موفقیت در بازاریابی.",
        "tags": ["بازاریابی", "استارتاپ"],
        "date": "6 بهمن 1402",
        "reading_time": "7 دقیقه"
    },
    {
        "title": "مقاله ۴",
        "image": "static/images/blog4.jpg",
        "link": "/blog/4",
        "description": "راهنمای کامل یادگیری برنامه‌نویسی.",
        "tags": ["برنامه‌نویسی", "آموزش"],
        "date": "4 بهمن 1402",
        "reading_time": "3 دقیقه"
    }
]

# Add slug field dynamically
for post in blog_posts:
    post["slug"] = generate_slug(post["title"])

# Function to get the current locale
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
    # latest_posts = get_latest_posts(4)  # Fetch the latest 4 posts from DB
    # , latest_posts=latest_posts
    return render_template('index.html', lang=lang, direction=direction, blogs=blog_posts, latest_blog=blog_posts[0])

@app.route('/blog')
def blog():
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    return render_template('blog.html', lang=lang, direction=direction, blog_posts=blog_posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    # Find the requested blog post by slug
    post = next((p for p in blog_posts if p["slug"] == slug), None)
    
    if post is None:
        return "Blog post not found", 404

    # post.image = post.image[:-4] + "-" + post.image[-5] + ".jpg" # Modify image path
    print(post["image"])
    return render_template('blog_post.html', post=post, lang=lang, direction=direction)

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
