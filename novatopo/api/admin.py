from django.contrib import admin

from .models import Activity, ActivityAvailable, Business, Booking, BusinessActivity
# Register your models here.

admin.site.register(Activity)
admin.site.register(ActivityAvailable)
admin.site.register(Business)
admin.site.register(Booking)
admin.site.register(BusinessActivity)
