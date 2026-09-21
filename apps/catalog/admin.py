from django.contrib import admin
from .models import *
admin.site.register([Genre,Person,Content,Season,Episode,LiveEvent])
