from django.db import models


class SampleModel(models.Model):
    property_a = models.CharField(max_length=100)
    property_b = models.IntegerField()

    class Meta:
        verbose_name = "sample"
        verbose_name_plural = "samples"
        ordering = ['property_a']

    def __str__(self):
        return f"Representation of {self.property_a}"
