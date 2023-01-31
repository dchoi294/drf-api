from django.contrib import admin

# Register your models here.
from .models import Practice

# register the model
admin.site.regist(Practice)