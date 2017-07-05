from django.conf.urls import url,include
from . import views

urlpatterns = [
        url(r'^login/',views.loginpage,name='login'),
        url(r'^submit/',views.submit,name='submit'),
        url(r'^signin/',views.signin,name='signin'),
        url(r'^home/',views.home,name='home'),
        url(r'^demo/',views.demo,name='demo'),
        url(r'^logout/',views.signout,name='logout'),

]