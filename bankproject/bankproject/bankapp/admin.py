from django.contrib import admin

from . models import Branch
from . models import District

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)