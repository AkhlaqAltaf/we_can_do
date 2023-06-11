from django.db import models

# Create your models here.

class Contact(models.Model):
      email = models.EmailField()
      message = models.TextField()
      date_time = models.DateField()

      def __str__(self):
          return self.email
      


class MCQ(models.Model):
    
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)