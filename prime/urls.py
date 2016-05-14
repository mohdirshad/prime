from django.conf.urls import patterns, include, url
from django.contrib import admin
from primeapp.views import Nth_Prime

urlpatterns = patterns('',
    url(r'', Nth_Prime.as_view()),
)
