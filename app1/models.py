from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.contrib.auth.models import User,AbstractUser

# Category Model
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=60)
    description=models.TextField()
    url=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:100px; height:80px;"/>'.format(self.image)) 
    
    def __str__(self):
        return self.title
    

# Post Model
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=HTMLField()
    url=models.CharField(max_length=100,default='')
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    video=models.FileField(upload_to='video/%y',default='Video')
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px, height:20px;"/>'.format(self.image))
  
class SignUpModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=70,null=True)
    city=models.CharField(max_length=80,null=True)
    def __str__(self):
        return self.user.username

