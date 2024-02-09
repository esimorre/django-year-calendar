Django year calendar
====================
a django app based on [js-year-calendar](https://github.com/year-calendar/js-year-calendar/)
<img src="https://year-calendar.github.io/assets/img/calendar.png">

Dynamic view implemented with Bootstrap 5 and JS Fetch API (no jquery). Popups are not supported,
they are replaced by a modal dialog raised on  date range selection.

Get started
===========

Clone the repository or download the project

optional: set a django environnement, then activate
```bash
python -m venv venv
venv\Scripts\activate.bat (windows)
. venv/bin/activate       (linux)
pip install django
```

Install django_year_app (or put current directory in PYTHONPATH)
```bash
pip install django_year_app
```

Go to the example django project, initialize the project then run dev server
```bash
cd example_project
python manage.py migrate
python manage.py runserver
```






Usage in an existing django project
========
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

You may add some settings in your settings.py file:
```python
CALENDAR_LANG  = "fr"   # see https://github.com/year-calendar/js-year-calendar/tree/master/locales
CALENDAR_WEEKSTART = 1  # monday
CALENDAR_WEEKNUMBER = True # display week number

CALENDAR_TPL = "django_year_calendar/bootstrap5"
# style: 'border' | 'background' | [custom_template] for 'custom' style
CALENDAR_RENDERER = 'background'

CALENDAR_VIEWS = [
    ...
    {'manager': 'app.models.MyModel[.MyManager[.a_method]]',
     'color': 'blue',
     'style': 'background | border'},
    ...
]
```

Add some code to your models to display on the calendar, 
```bash
class MyEvent(models.Model):
    ...
    # required
    def start_date(self) -> DateField | date :
        ...
        return some_date
    # required    
    def end_date(self):
        ...
        return another_date
    
    # optional
    def color(self) -> str:
        return 'blue'
    def infos(self) -> str:
        return "my birthday"
    def style(self) -> str ('background' | 'border' ):
        if self.type == 'yellow': return 'background'
        return 'border'
```

### TODO

soon ...

