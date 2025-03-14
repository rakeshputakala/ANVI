from django.db import models
from django.contrib.auth.models import User

class DataSet(models.Model):
    INDUSTRY_CHOICES = (
        ('Technical', 'Technical'),
        ('Medical', 'Medical'),
        ('Education', 'Education'),
        ('Science', 'Science'),
        ('Automotive', 'Automotive'),
                        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.FileField(upload_to='uploads/')
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

