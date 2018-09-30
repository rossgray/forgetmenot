from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


MONTHS = (
    (1, 'January', 31),
    (2, 'February', 29),
    (3, 'March', 31),
    (4, 'April', 30),
    (5, 'May', 31),
    (6, 'June', 30),
    (7, 'July', 31),
    (8, 'August', 31),
    (9, 'September', 30),
    (10, 'October', 31),
    (11, 'November', 30),
    (12, 'December', 31),
)
MONTH_CHOICES = ((num, name) for (num, name, _) in MONTHS)
DAY_OF_MONTH_CHOICES = ((i, str(i)) for i in range(1, 31))


class Person(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dob = models.DateField('date of birth', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OccasionType(models.Model):
    key = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    # for user-created occasions
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                                   null=True)

    class Meta:
        unique_together = (('created_by', 'name'),)


class TrackedOccasion(models.Model):
    occasion_type = models.ForeignKey(OccasionType, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    month = models.IntegerField(choices=MONTH_CHOICES)
    day_of_month = models.IntegerField(choices=DAY_OF_MONTH_CHOICES)

    class Meta:
        unique_together = (('occasion_type', 'person'),)
