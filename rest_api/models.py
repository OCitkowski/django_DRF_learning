from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    quality = models.BigIntegerField()
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'date_update']
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'


    def __str__(self):
        return f"{self.title} - {self.date_update}..."


class CommentTest(models.Model):
    title = models.CharField(max_length=80)
    test = models.ForeignKey(Test, related_name="comment", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f"{self.title} ..."
