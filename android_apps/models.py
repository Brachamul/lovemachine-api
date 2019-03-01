import uuid
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe



class AndroidApp(models.Model):

	# TODO : arrange neatly based on data type for more efficiency, rather than
	# storing everything in CharFields
	google_app_id = models.CharField(unique=True, max_length=256) # "com.kiloo.subwaysurf"
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
		return reverse("app-detail", kwargs={'google_app_id': self.google_app_id})

	class Meta:
		ordering = ["-reviews", ]

	def price(self):
		return self.display_price if self.display_price else "Free"

	def html_thumbnail(self, size=170):
		if self.thumbnail :
			return mark_safe('\
				<img src="{url}"\
				style="max-width: {size}px; max-height: {size}px; border: 1px solid #ccc; border-radius: 4px;"\
				title="{name}"/>'.format(url=self.thumbnail, size=size, name=self.__str__()))
		else:
			return ""