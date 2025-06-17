from django.db import models
from django.contrib.auth.models import AbstractUser

#User Role
USER_ROLE_CHOICES = (
    ('seeker','job seeker'),
    ('employer','Employer')
)

class CustomUser(AbstractUser):
    role= models.CharField(max_length=10, choices=USER_ROLE_CHOICES)

    def __str__(self):
        return f"{self.username}({self.role})"
    
class Job(models.Model):
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role':'employer'})
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} at {self.location}"
    
APPLICATION_STATUS =(
    ('pending','Pending'),
    ('accepted','Accepted'),
    ('rejected','Rejected'),
)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    seeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role':'seeker'})
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=10 ,choices=APPLICATION_STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.seeker.username} applied to {self.job.title}"