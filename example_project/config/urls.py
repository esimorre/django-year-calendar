"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import django_year_calendar
from django_year_calendar.views import CalendarView

urlpatterns = [
    #path('', CalendarView.as_view(), name='home'),
    path('', include('django_year_calendar.urls')),

    path('admin/', admin.site.urls),
    path('minimal',    TemplateView.as_view(template_name='django_year_calendar/minimal.html')),
    path('minimal_fr', TemplateView.as_view(template_name='django_year_calendar/minimal.html',
                                            extra_context = {'calendar_lang': 'fr'})),
    path('style',    TemplateView.as_view(template_name='django_year_calendar/calendar_style.html')),
    path('bootstrap',TemplateView.as_view(template_name='django_year_calendar/bootstrap5.html')),

]
