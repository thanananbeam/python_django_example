from django.conf.urls import include, url
from register.views import *



urlpatterns = [
    url(r'^$', HomeView.as_view(), name='frontend_home'),   
    url(r'^register', RegisterView.as_view(), name='frontend_register'),
]


