from django.db import models

# Create your models here.



class Comment(models.Model):
    comment_content = models.CharField(null=True, max_length = 500, verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.comment_content)

