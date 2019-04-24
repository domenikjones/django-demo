from django.db import models

from employees.models import Employee


class Restaurant(models.Model):

    name = models.CharField("Name", max_length=255, null=True, blank=False)
    address = models.CharField("Address", max_length=255, null=True, blank=False)
    city = models.CharField("City", max_length=45, null=True, blank=False)
    zip = models.CharField("ZIP", max_length=45, null=True, blank=False)
    country = models.CharField("Country", max_length=45, null=True, blank=False)

    employees = models.ManyToManyField(Employee, through="Job")

    def __str__(self):
        return self.name if self.name else ""

    class Meta:
        app_label = 'restaurants'
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        ordering = ('name',)


class Job(models.Model):

    restaurant = models.ForeignKey("Restaurant", related_name='jobs', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='jobs', on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=45, null=True, blank=False)
    salary = models.FloatField("Salary/h", default=0)
    hours = models.SmallIntegerField("Hours", default=0)

    class Meta:
        app_label = "restaurants"
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
