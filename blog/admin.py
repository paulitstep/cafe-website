from django.contrib import admin

from blog.models import Post, Profile, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)

