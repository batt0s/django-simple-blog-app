from django.db import models

from ckeditor.fields import RichTextField


class Article(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=120, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publish date")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Article", related_name="comments")
    comment_author = models.CharField(max_length=30, verbose_name="Name")
    comment_author_email = models.EmailField(max_length=50, verbose_name="Email Address")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-pub_date']