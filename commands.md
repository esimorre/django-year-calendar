
### Generate wheel
```bash
python setup.py bdist_wheel
```

### publish on pypi
```bash
twine upload --verbose dist/*.whl
```

### update install local
```bash
pip uninstall django_year_calendar
python setup.py install
```