import tastypie
from tastypie.resources import ModelResource
from tastypie import fields

from .models import Post,User
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        authorization = Authorization()

class PostResource(ModelResource):
    class Meta:
        user = fields.ForeignKey(UserResource,'user')
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()





