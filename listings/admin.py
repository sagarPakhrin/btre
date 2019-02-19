from django.contrib import admin
from listings.models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price', 'list_date','realtor')
    # this allows us to click on the title or the id to go to the details of the listings
    list_display_links = ('id','title')
    # this helps us to filter listings based on realtor
    list_filter = ('realtor',)
    list_editable = ('is_published',)
admin.site.register(Listing, ListingAdmin)

