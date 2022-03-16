from django.contrib import admin

from tutorial.models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ['property_a', 'property_b']