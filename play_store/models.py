import uuid
from django.db import models
from django.urls import reverse



class AndroidApp(models.Model):

	# TODO : arrange neatly based on data type for more efficiency, rather than
	# storing everything in CharFields
	store_id = models.CharField(unique=True, max_length=256) # "com.kiloo.subwaysurf"
	name = models.CharField(max_length=256) # "Subway Surfers"
	dev_id = models.CharField(max_length=128) # "5062298237373103345"
	category = models.CharField(max_length=128, blank=True, null=True) # "GAME"
	subcategory = models.CharField(max_length=128, blank=True, null=True) # "GAME_CASUAL"
	short_description = models.CharField(max_length=256, blank=True, null=True) # 
	long_description = models.TextField(max_length=5000, blank=True, null=True) # Can be pretty long
	thumbnail = models.CharField(max_length=256, blank=True, null=True)
	screenshots = models.CharField(max_length=1200, blank=True, null=True)
	rating = models.IntegerField(blank=True, null=True) # 0 to 100"
	reviews = models.IntegerField(blank=True, null=True) # "27725352"
	installs = models.CharField(max_length=64, blank=True, null=True) # 1,000,000,000+
	maturity = models.CharField(max_length=64, blank=True, null=True) # PEGI 3
	size = models.CharField(max_length=64, blank=True, null=True) # "76M", not INT because can be "Varies with device"
	is_free = models.BooleanField(blank=True, null=True)
	display_price = models.CharField(max_length=64, blank=True, null=True)
	full_price = models.CharField(max_length=64, blank=True, null=True)
	has_ads = models.BooleanField(blank=True, null=True)
	has_iaps = models.BooleanField(blank=True, null=True) # In-app purchases
	current_version = models.CharField(max_length=64, blank=True, null=True)
	android_version = models.CharField(max_length=64, blank=True, null=True)
	last_updated = models.CharField(max_length=64, blank=True, null=True)
	last_fetched = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("app-detail", kwargs={'store_id': self.store_id})

	class Meta:
		ordering = ["-reviews", ]
