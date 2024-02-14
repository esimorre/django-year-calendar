Django year calendar
====================

![dyc-img](https://github.com/esimorre/django-year-calendar/assets/697460/09fa7e8b-34e7-4765-b1e2-c0a96a32979a)

A django app based on [js-year-calendar](https://github.com/year-calendar/js-year-calendar/)

Dynamic view implemented with Bootstrap 5 and JS Fetch API (no jquery); popups are not supported, they are replaced by a modal component.

Get started
===========

Clone the repository or download the project

Optional: set a django environnement, then activate
```bash
python -m venv venv
venv\Scripts\activate.bat (windows)
. venv/bin/activate       (linux)
pip install django
```

Install django_year_calendar (or give an access)
```bash
pip install django-year-calendar
#  or
python setup.py install
# or put current directory in PYTHONPATH
```

Go to the example django project, initialize the project then run dev server
```bash
cd example_project
python manage.py migrate
python manage.py loaddata sample_data.json
python manage.py runserver
```
Check then http://localhost:8000

You can also go to the admin panel http://localhost:8000/admin (login admin passwd admin) to browse models
and add some more data.

Usage for an existing django project
====================================

Add the django_year_app to your project
```bash
INSTALLED_APPS = [
    ...
    'django_year_calendar',
]
```

Add some routes to views in the urls.py file
```bash
urlpatterns = [
    ...
    path('my_calendar', include('django_year_calendar.urls')),
    path('minimal_fr', TemplateView.as_view(template_name='django_year_calendar/minimal.html',
                                            extra_context = {'calendar_lang': 'fr'})),
    ...
]
```

You may (or not) add some settings in your settings.py file:
```python
CALENDAR_LANG  = "fr"   # see https://github.com/year-calendar/js-year-calendar/tree/master/locales
CALENDAR_WEEKSTART = 1  # monday
CALENDAR_WEEKNUMBER = True # display week number

CALENDAR_TPL = "django_year_calendar/bootstrap5"
# style: 'border' | 'background' | [custom_template] for 'custom' style
CALENDAR_RENDERER = 'background'

CALENDAR_VIEWS = [
    # place background display view(s) first
    ...
    { 'manager': 'app.models.MyModel[.myManager[.a_method]]' [, 'border':True] [, 'force_color': 'PaleGreen'] },
        # manager:      name of an object that generates events     (see MyEvent below) 
        # border:       set to True to force border type display    (overrides the event style() method)
        # force_color:  forces event color display                  (overrides the event color() method)
    ...
]
```

Add some code to the models to display on the calendar, 
```bash
class MyEvent(models.Model, EventMixin): # without EventMixin, advanced features will not be available
    ...
    # REQUIRED
    def start_date(self) -> DateField | date :
        ...
        return some_date
    # REQUIRED    
    def end_date(self):
        ...
        return another_date
    
    # optional
    def color(self) -> str:
        return 'blue' # https://www.w3.org/wiki/CSS/Properties/color/keywords
        
    def style(self) -> str ('background' | 'border' ):
        return 'border'
```

You can make your own views in various ways depending on your needs:
 * new templates based on the provided ones in django_year_calendar/templates
 * parameters in the urls.py file
 * new views based on CalendarView provided by the django_year_calendar app

See example_project for more details.

### Future

 * Customizing the calendar view based on user rights
 * Helpers for building event editing views
 * ...

