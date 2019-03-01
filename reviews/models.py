from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from android_apps.models import AndroidApp
from android_users.models import AndroidUser



class AndroidAppReview(models.Model):

	''' An AndroidAppReview is given by an AndroidUser to an AndroidApp '''

	android_user = models.ForeignKey(AndroidUser, on_delete=models.CASCADE)
	android_app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
	rating = models.PositiveSmallIntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(100)]
		# Should be 0, 34, 66 or 100
		)
	date = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ("android_user", "android_app")