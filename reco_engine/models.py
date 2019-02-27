from play_store.models import AndroidApp

class AndroidUser(models.Model):

	gpgs_id = models.CharField(unique=True, max_length=256) # "Google Play Games Services"
	date_joined = models.DateTimeField(auto_now_add=True)
	date_last_connected = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "User #" + gpgs_id


class AndroidAppReview(models.Model):

	''' An AndroidAppReview is given by an AndroidUser to an AndroidApp '''

	android_user = models.ForeignKey(AndroidUser, on_delete=models.CASCADE)
	android_app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)