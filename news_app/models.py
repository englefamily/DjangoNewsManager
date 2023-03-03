from django.db import models

# Create your models here.


class NewsPost(models.Model):
    headline = models.CharField(null=False, max_length=50, db_index=True) # Chose the indexing for Database
    content = models.CharField(null=False, max_length=5000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'newspost'
        indexes = [
            models.Index(fields=['headline', 'content'])
        ]


    def __str__(self):
        return f"post_id: {self.pk}"