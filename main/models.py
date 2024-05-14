from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Survey_question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.subject
    
class Survey_answer(models.Model):
    question = models.ForeignKey(Survey_question,on_delete=models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField()
    
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # 연락처 필드 추가
    last_name = None