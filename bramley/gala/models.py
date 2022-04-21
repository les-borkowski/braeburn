from django.db import models

class Query(models.Model):
    url = models.URLField(max_length=255, blank=None)
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='queries', on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return f'{self.id} {self.url} {self.created}'