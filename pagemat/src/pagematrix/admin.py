from django.contrib import admin

# Register your models here.
from .models import pagematrix

class pagematrixAdmin(admin.ModelAdmin):
	class meta:
		model = pagematrix

admin.site.register(pagematrix,pagematrixAdmin)