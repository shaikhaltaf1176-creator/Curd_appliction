from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EntryForm
from .models import Entry


def entry_list(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your entry has been saved.')
            return redirect('entry_list')
    else:
        form = EntryForm()

    return render(
        request,
        'entries/index.html',
        {'form': form, 'entries': Entry.objects.all()},
    )
