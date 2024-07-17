from django.contrib import admin
from .models import GuestBookEntry

@admin.register(GuestBookEntry)
class GuestBookEntryAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'entry_text', 'created_at', 'updated_at', 'status')
    list_filter = ('status',)
    search_fields = ('author_name', 'author_email', 'entry_text')
