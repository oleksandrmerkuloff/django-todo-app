from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
