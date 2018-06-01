from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^patient/new$', views.new_patient),
]