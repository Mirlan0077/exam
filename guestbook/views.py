from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GuestBookEntry
from .forms import GuestBookEntryForm

def index(request):
    entries = GuestBookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/index.html', {'entries': entries})

def add_entry(request):
    if request.method == 'POST':
        form = GuestBookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestBookEntryForm()
    return render(request, 'guestbook/add_entry.html', {'form': form})

def edit_entry(request, entry_id):
    entry = get_object_or_404(GuestBookEntry, pk=entry_id)
    if request.method == 'POST':
        form = GuestBookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestBookEntryForm(instance=entry)
    return render(request, 'guestbook/edit_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(GuestBookEntry, pk=entry_id)
    if request.method == 'POST':
        author_email_input = request.POST.get('author_email_input', '')
        if author_email_input == entry.author_email:
            entry.delete()
            messages.success(request, 'Запись успешно удалена.')
        else:
            messages.error(request, 'Введенный email не совпадает с email автора записи.')
        return redirect('index')
    return render(request, 'guestbook/delete_entry.html', {'entry': entry})