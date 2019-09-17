from django.contrib import admin
from .models import Commission, TestItem, AssignedTo

# Register your models here.

admin.site.register(Commission)
admin.site.register(TestItem)
admin.site.register(AssignedTo)