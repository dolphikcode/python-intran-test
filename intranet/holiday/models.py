from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    # additional fields in profile
    profile_photo = models.ImageField(upload_to='profile_pics',blank=True)
    profile_vacation_left = models.IntegerField(default=0)
    profile_vacation_new = models.IntegerField(default=26)

    def __str__(self):
        return self.user.last_name

class VacationReason(models.Model):
    vacation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.vacation_type


class Holiday(models.Model):
    vacation_begining = models.DateField()
    vacation_length = models.IntegerField(default=0)
    vacation_reason = models.ForeignKey(VacationReason, on_delete=models.PROTECT, default=1)
    vacation_status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.vacation_begining), self.vacation_reason, self.vacation_status