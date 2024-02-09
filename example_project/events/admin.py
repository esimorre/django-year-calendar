from django.contrib import admin

from events.models import MyEvent, Week


@admin.register(MyEvent)
class MyEventAdmin(admin.ModelAdmin):
    list_display = ('type', 'start', 'end', 'style', 'color')
    save_as = True

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'task')
    save_as = True