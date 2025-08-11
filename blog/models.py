from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):

    CHOICES =(('pub','Published'),('drf','Drafting'))

    #title
    #author
    #text
    #date_created
    #date_modified
    #status


    title = models.CharField(max_length=100)
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # status = models.BooleanField(default=False) # pishnahad khod django
    status = models.CharField(choices=CHOICES, max_length=3)
    def __str__(self):
        return f"{self.title} ----- {self.author}"

    def get_absolute_url(self):
        return reverse ('post-detail', args=[self.id])
