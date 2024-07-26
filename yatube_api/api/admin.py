from django.contrib import admin
from posts.models import Comment, Follow, Group, Post

admin.site.empty_value_display = 'Не задано'
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Group)
