from django.db import models


# Create your models here.

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
        if len(self.text) >= 50:
            return f"{self.text[:150]}..."
        else:
            return f"{self.text[:150]}"


class CommentTest(models.Model):
    title = models.CharField(max_length=80)
    test = models.ForeignKey(Test, related_name="comment", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
