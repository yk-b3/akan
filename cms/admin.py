from django.contrib import admin
from cms.models import WebService, Parameter, GenericParameter

admin.site.register(WebService)
admin.site.register(Parameter)
admin.site.register(GenericParameter)

# Register your models here.
