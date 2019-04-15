from django.contrib import admin
from .models import Post, Category, Tag, TeamName, Team, ProjectName, Project


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time',
                    'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(TeamName)
admin.site.register(ProjectName)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Tag)
# Register your models here.
