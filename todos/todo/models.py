from django.db import models
from django.contrib import admin

# Create your models here.
importance_choices = (
                      ('A', 'Very Important'),
                      ('B', 'Important'),
                      ('C', 'Medium'),
                      ('D', 'UnImportant'),
                      )

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    importance = models.CharField(
                                  max_length=1,
                                  choices=importance_choices)
    def __unicode__(self):
        return self.title
    
    def text_importance(self):
        choices = dict(importance_choices)
        return choices[self.importance]
    
