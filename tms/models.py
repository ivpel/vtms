import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tms:project_detail', kwargs={'pk': self.pk})


class Suite(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tms:suite_detail', kwargs={'pk': self.pk})


class Case(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    pre_requisites = models.TextField()
    test_steps = models.TextField()
    pub_date = models.DateTimeField('date published')

    statuses = [
        ('p', 'Passed'),
        ('f', 'Failed'),
        ('n', 'New'),
        ('i', 'In progress')
    ]
    case_status = models.CharField(
        max_length=2,
        choices=statuses,
        default=statuses[-2][1]
    )

    automation_statuses = [
        ('a', 'Automated'),
        ('m', 'Manual')
    ]
    automated = models.CharField(
        max_length=2,
        choices=automation_statuses,
    )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name
