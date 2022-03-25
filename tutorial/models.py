from django.db import models

from tutorial.choices import SampleChoices


class SampleModelBase(models.Model):
    name = models.CharField(max_length=100)


class SampleModel(models.Model):
    """
    A Sample Model with examples of different attribute types.
    """
    attr_char = models.CharField(max_length=100)
    attr_int = models.IntegerField()
    attr_bool = models.BooleanField(default=True)
    attr_fk = models.ForeignKey('tutorial.SampleModelBase', on_delete=models.CASCADE)
    attr_choices = models.CharField(max_length=100, choices=SampleChoices.choices, default=SampleChoices.CHOICE_1)

    class Meta:
        verbose_name = "sample"
        verbose_name_plural = "samples"
        ordering = ['attr_char']

    def __str__(self):
        return f"Representation of {self.attr_char}"
