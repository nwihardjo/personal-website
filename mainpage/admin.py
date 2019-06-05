from django.contrib import admin
from mainpage.models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
	pass

class TechnologyAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)

