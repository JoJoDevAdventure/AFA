from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255,null=True)
    family_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name