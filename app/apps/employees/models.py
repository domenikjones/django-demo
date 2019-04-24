from django.db import models


PROFESSIONALITY = (
    (0, 'Trainee'),
    (1, 'Junior'),
    (2, 'Medior'),
    (3, 'Senior'),
    (4, 'Lead'),
    (5, 'Manager'),
)


class Employee(models.Model):

    first_name = models.CharField("First name", max_length=45, null=False, blank=False)
    last_name = models.CharField("Last name", max_length=45, null=False, blank=False)
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)

    active = models.BooleanField("Active", default=True)
    professionality = models.SmallIntegerField('Professionality', default=0, choices=PROFESSIONALITY)

    def get_job_query(self, restaurant=None, job=None):
        if restaurant and job:
            qs = self.jobs.filter(restaurant=restaurant, pk=job.pk)
        elif restaurant:
            qs = self.jobs.filter(restaurant=restaurant)
        elif job:
            qs = self.jobs.filter(pk=job.pk)
        else:
            qs = self.jobs.all()
        return qs

    def weekly_income(self, restaurant=None, job=None):
        money = 0
        qs = self.get_job_query(restaurant, job)
        for _job in qs:
            money += job.salary * _job.hours
        return money

    def weekly_hours(self, restaurant=None, job=None):
        hours = 0
        qs = self.get_job_query(restaurant, job)
        for _job in qs:
            hours += _job.hours
        return hours

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        app_label = 'employees'
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ('first_name', 'last_name')
