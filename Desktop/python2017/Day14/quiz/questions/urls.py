from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index),
    url(r'^aboutus/', views.aboutus),
    url(r'^courses/', views.courses),
    url(r'^form/', views.form),
    url(r'^submit/', views.submit)

]
