from django.contrib import admin
from holiday.models import Holiday, VacationReason
from holiday.models import UserProfileInfo

# Register your models here.
admin.site.register(Holiday)
admin.site.register(VacationReason)
admin.site.register(UserProfileInfo)