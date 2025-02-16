import os

# Function to load description from file
def load_description(post_number):
    # Get the current working directory (where the script is running)
    current_directory = os.getcwd()
    
    # Build the path relative to the current working directory
    file_path = os.path.join(current_directory, f"static\content\description{post_number}.txt")
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    else:
        print(file_path)
        return "No description available"

# Blog data including latest blog as part of the list
blog_posts = [
    {
        "title": "عنوان مقاله ویژه",
        "image": "static/images/featured-blog.jpg",
        "link": "/blog/latest",
        "description": load_description(0),  # Load description from description0 file
        "tags": ["ویژه", "مهم"],
        "date": "12 بهمن 1402",
        "reading_time": "5 دقیقه"
    },
    {
        "title": "مقاله ۱",
        "image": "static/images/blog1.jpg",
        "link": "/blog/1",
        "description": load_description(1),  # Load description from description1 file
        "tags": ["تکنولوژی", "کسب و کار"],
        "date": "10 بهمن 1402",
        "reading_time": "4 دقیقه"
    },
    {
        "title": "مقاله ۲",
        "image": "static/images/blog2.jpg",
        "link": "/blog/2",
        "description": load_description(2),  # Load description from description2 file
        "tags": ["طراحی", "خلاقیت"],
        "date": "8 بهمن 1402",
        "reading_time": "6 دقیقه"
    },
    {
        "title": "مقاله ۳",
        "image": "static/images/blog3.jpg",
        "link": "/blog/3",
        "description": load_description(3),  # Load description from description3 file
        "tags": ["بازاریابی", "استارتاپ"],
        "date": "6 بهمن 1402",
        "reading_time": "7 دقیقه"
    },
    {
        "title": "مقاله ۴",
        "image": "static/images/blog4.jpg",
        "link": "/blog/4",
        "description": load_description(4),  # Load description from description4 file
        "tags": ["برنامه‌نویسی", "آموزش"],
        "date": "4 بهمن 1402",
        "reading_time": "3 دقیقه"
    }
]

# Print the blog posts to see the output
for post in blog_posts:
    print(post['title'], ":", post['description'])
