from django.contrib import admin

# Register your models here.

# as in model class is Listing
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','addess','city','state','zipcode')
    list_per_page = 25

# to register - name of model is Listing

admin.site.register(Listing,ListingAdmin)