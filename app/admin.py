from django.contrib import admin
from .models import Placement, Bid, PlacementBid, Company

# Register your models here.
class PlacementBidAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer','confirmed','placement')


admin.site.register(PlacementBid,PlacementBidAdmin)
admin.site.register(Bid)
admin.site.register(Company)