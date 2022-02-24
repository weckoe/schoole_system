from django.db import models

from authentication.models import User

class Assignment(models.Model):
   title = models.CharField(max_length=500, null=False, verbose_name='assignment title')
   teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='teacher name')
