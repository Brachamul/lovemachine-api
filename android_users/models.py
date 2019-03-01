from django.db import models



class AndroidUser(models.Model):

	''' AndroidUsers are created through Google Play Game Services (GPGS)'''

	google_gamer_id = models.CharField(unique=True, max_length=256)

	date_joined = models.DateTimeField(auto_now_add=True)
	date_last_connected = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.google_gamer_id