from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django_year_calendar',
    version='0.1.7',
    description='A year calendar application for django',
    url='https://github.com/esimorre/django-year-calendar',
    
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    platforms=['any'],
    packages=["django_year_calendar",],
    package_data = {"django_year_calendar.static.css": ["*.css"],
                    "django_year_calendar.templates": ["*.html", "*.js"]},
    include_package_data=True,
    zip_safe=False,
    keywords=['django', 'calendar'],
    install_requires=['django',],
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only"
    ],
    project_urls = {  # Optional
        "Bug Reports": "https://github.com/esimorre/django-year-calendar/issues",
        "Say Thanks!": "https://year-calendar.github.io/",
        "Source": "https://github.com/esimorre/django-year-calendar",
    },
)