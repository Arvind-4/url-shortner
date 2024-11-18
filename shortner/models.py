from django.db import models
from shortner.validators import validate_url
from shortner.utils import generate_short_path

class URL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url])
    shortcode   = models.CharField(max_length=6, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)

 

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = generate_short_path()
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(URL, self).save(*args, **kwargs)
