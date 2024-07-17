from django.db import models
from django.urls import reverse

class GuestBookEntry(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    )

    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    entry_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.author_name + ' - ' + self.entry_text[:20]

    def get_absolute_edit_url(self):
        return reverse('edit_entry', args=[str(self.id)])
