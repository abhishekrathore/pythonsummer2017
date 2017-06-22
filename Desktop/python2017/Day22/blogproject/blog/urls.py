from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^home/',views.posts,name='home'),
        url(r'^post/(?P<post_id>[0-9]+)/$',views.post,name='post'),
        url(r'^author/(?P<author_id>[0-9]+)/$',views.author,name='author'),
        url(r'^comment/(?P<post_id>[0-9]+)/$',views.comment_submit,name='comment')

]