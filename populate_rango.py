import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def add_page(cat, title, url, views=0):
    p, created = Page.objects.get_or_create(category=cat, title=title)
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, likes=0):
    c, created = Category.objects.get_or_create(name=name)
    c.likes = likes
    c.save()
    return c


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'https://docs.python.org/3/tutorial/', 'views': 128},
        {'title': 'Learn Python in 10 Minutes', 'url': 'https://www.korokithakis.net/tutorials/python/', 'views': 64},
        {'title': 'How to Think Like a Computer Scientist', 'url': 'https://runestone.academy/ns/books/published/thinkcspy/index.html', 'views': 32},
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/stable/intro/tutorial01/', 'views': 128},
        {'title': 'Django Rocks', 'url': 'https://www.djangorocks.com/', 'views': 64},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 32},
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'https://bottlepy.org/docs/dev/', 'views': 32},
        {'title': 'Flask', 'url': 'https://flask.palletsprojects.com/', 'views': 64},
    ]

    cats = {
        'Python': {'pages': python_pages, 'likes': 64},
        'Django': {'pages': django_pages, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'likes': 16},
    }

    for cat_name, cat_data in cats.items():
        c = add_cat(cat_name, likes=cat_data['likes'])

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    
    for c in Category.objects.all():
        print(f"- {c.name} ({c.likes} likes)")
        for p in Page.objects.filter(category=c):
            print(f"  * {p.title} ({p.views} views) -> {p.url}")


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
