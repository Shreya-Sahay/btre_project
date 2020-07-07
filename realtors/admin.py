from django.contrib import admin

# Register your models here.

# as in model class is Listing
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_per_page = 25
# to register - name of model is Listing

admin.site.register(Realtor,RealtorAdmin)