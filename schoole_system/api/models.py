from django.db import models

from authentication.models import User


class Assignment(models.Model):
    title = models.CharField(max_length=500, null=False, blank=True, verbose_name='assignment title')
    teacher = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE, verbose_name='teacher name')

    def __str__(self):
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=500, null=False, blank=True, verbose_name='choice title')
    
    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=2000, null=False, blank=True, verbose_name='question')
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice,null=False, blank=True, on_delete=models.CASCADE, related_name='answer')
    assignment = models.ForeignKey(Assignment, null=False, blank=True, on_delete=models.CASCADE, related_name='assignment')
    order = models.IntegerField(null=False, blank=True, verbose_name='order')

    def __str__(self):
        return self.question
