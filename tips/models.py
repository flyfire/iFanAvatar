from django.db import models

# Create your models here.
class Tips(models.Model):
    date=models.CharField(max_length=30)
    tips=models.CharField(max_length=512)
    
    
    def __str__(self):
        return self.date
    class Meta:
        ordering = ["-date"]
    class Admin:
        list_display = ('date', 'tips')
        list_filter = ('date')
        ordering = ('-date',)
        search_fields = ('tips',)
        
