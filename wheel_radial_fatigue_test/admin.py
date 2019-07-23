from django.contrib import admin
from .models import WhRaFaTest
from .list_of_samples import Sample
from .list_of_check import TestCheck
from .list_of_torque_check import TorqueValue
from .list_of_photo import CheckPhoto
from .method.list_of_stand import WhRaFaTeStand
from .method.detail_of_stand import WhRaFaTeStandDetail

# Register your models here.

admin.site.register(WhRaFaTest)
admin.site.register(Sample)
admin.site.register(TestCheck)
admin.site.register(TorqueValue)
admin.site.register(CheckPhoto)
admin.site.register(WhRaFaTeStand)
admin.site.register(WhRaFaTeStandDetail)