from django.contrib import admin

# Register your models here.
from djangogamers.apps.authentication.models import Gamer, Developer, Publisher, StaffMember

admin.site.register(Gamer)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(StaffMember)