from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)  # Correct usage
    content = models.TextField()  # No max_length here
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title