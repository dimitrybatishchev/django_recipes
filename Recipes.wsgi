import os
import sys	
sys.path.append('/var/www/django_recipes/Recipes')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Recipes.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
