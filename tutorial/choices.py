from django.db import models


class SampleChoices(models.TextChoices):
    # code   = database  , label
    CHOICE_1 = 'choice_1', "Choice 1"
    CHOICE_2 = 'choice_2', "Choice 2"
