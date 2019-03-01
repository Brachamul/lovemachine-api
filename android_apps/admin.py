from django.contrib import admin

from .models import AndroidApp

class AndroidAppAdmin(admin.ModelAdmin):

	list_display = (
		'image',
		'name',
		'dev_id',
		'rating',
		'price',
	)

	readonly_fields = (
		'image',
	)

	def image(self, obj):
		return obj.html_thumbnail(size=48)

admin.site.register(AndroidApp, AndroidAppAdmin)