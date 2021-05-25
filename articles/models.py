from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user, get_user_model
from django.db import models
from django.urls import reverse



class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),       # the user that is creating the model
        on_delete = models.CASCADE
    )
    image = models.ImageField(upload_to='static/images/', default='static/images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # /article/<id>
        return reverse("article_detail", args=[str(self.id)])

    def get_id(self):
        return self.id


class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name="comments"
        )
    comment = models.CharField(max_length=140)
    star = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )


    def __str__(self):
        my_string = f'{self.article}, {self.comment}, {self.star}, {self.author}'
        return my_string

    def get_absolute_url(self):
        id = self.article.get_id()
        # id2 = self.article.get_id
        # print(f'hello world: {id} {id2}')
        # return reverse('article_list')
        return reverse("article_detail", args=[str(id)])