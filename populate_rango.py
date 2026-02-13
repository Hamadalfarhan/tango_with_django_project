import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()

from rango.models import Category

def populate():

    def add_cat(name, views=0, likes=0):
        c, created = Category.objects.get_or_create(name=name)
        c.views = views
        c.likes = likes
        c.save()
        return c

    add_cat("Python", views=128, likes=64)
    add_cat("Django", views=64, likes=32)
    add_cat("Other Frameworks", views=32, likes=16)

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
