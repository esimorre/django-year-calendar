from datetime import timedelta

from django.db import models

from django_year_calendar.models import EventMixin


class MyEvent(models.Model):
    type = models.CharField(max_length=10)
    start = models.DateField()
    end = models.DateField()

    def color(self):
        return self.type
    def start_date(self):
        return self.start
    def end_date(self):
        return self.end
    def infos(self):
        return "info test color: %s" % self.type
    def style(self):
        if self.type == 'yellow': return 'background'
        return 'border'

class Week(models.Model, EventMixin):
    task = models.CharField(max_length=100)
    monday = models.DateField()

    def start_date(self):
        return self.monday
    def end_date(self):
        return self.monday + timedelta(days=7)
