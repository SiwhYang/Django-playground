from django.db import models
#from django.db.models.enums import _TextChoicesMeta
from django.db.models.fields import TextField
from django.utils import timezone
from django.urls import reverse
# Create your models here.

 
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#這是給單一使用者    
    title = models.CharField(max_length=250)
    text = models.TextField()
    ceeate_date = models.DateField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)
    #hit publish button and call function below will make sure publish time is correct
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):  #call出此fnuction 列出所有已被驗證過的comment
        return self.comments.filter(approved_comments=True)
    #一但建立完成就call下列function get_absolute_url是djagno內建會自動尋找，此段是將網址導向post_detail並加入pk(剛建立的)
    def get_absolute_url (self):
        return reverse("post_detail",kwargs={'pk':self.pk})

class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url (self):
        return reverse("post_list",kwargs={'pk':self.pk})
        
