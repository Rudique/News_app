from django.db import models

# Create your models here.


class NewsModel(models.Model):
    title = models.CharField(verbose_name='title', max_length=100)
    content = models.CharField(verbose_name='content', max_length=1500)
    created_at = models.DateTimeField(verbose_name='date_of_creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date_of_editing', auto_now=True)
    active = models.BooleanField(verbose_name='active', default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        active = "active" if self.active is True else "not active"
        return f"{self.title} {self.created_at} {active}"


class CommentModel(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    comment = models.CharField(verbose_name='comment', max_length=1500)
    article = models.ForeignKey(to='NewsModel', default=None, on_delete=models.CASCADE)

    def __str__(self):
        text = self.comment if len(self.comment) <= 15 else self.comment[:15] + '...'
        return f"{self.name} {text}"
