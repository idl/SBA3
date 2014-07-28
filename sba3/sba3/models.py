from django.db import models

# Create your models here.

class Answers(models.Model):
    user_id = models.CharField(max_length=10, db_index = True)