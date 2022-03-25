from django.contrib import admin

from tutorial.models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ['attr_char', 'attr_int']
