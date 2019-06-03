from django.contrib import admin
from projects.models import Project, Comment

class ProjectAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
