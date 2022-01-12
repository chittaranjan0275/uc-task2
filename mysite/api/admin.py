from django.contrib import admin


# Register your models here.
from api.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'age', 'income', 'address', 'registration_number', 'registration_date','is_married')
    pass


admin.site.register(UserProfile, UserProfileAdmin)
