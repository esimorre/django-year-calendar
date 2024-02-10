from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django_year_calendar',
    version='0.1.2',
    description='A year calendar application for django',
    url='https://github.com/esimorre/django-year-calendar',
    
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    platforms=['any'],
    packages=["django_year_calendar",],
    include_package_data=True,
    zip_safe=False,
    keywords=['django', 'calendar'],
    install_requires=['django',],
)