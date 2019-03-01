from django.contrib import admin

from .models import AndroidAppReview



class AndroidAppReviewAdmin(admin.ModelAdmin):

	list_display = (
		'android_user',
		'android_app',
		'rating',
		'date',
	)

admin.site.register(AndroidAppReview, AndroidAppReviewAdmin)