from django.contrib import admin

from .models import playersInfo
from .models import predictions
# Register your models here.

admin.site.register(playersInfo)
admin.site.register(predictions)
