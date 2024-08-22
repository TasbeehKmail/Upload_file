# fileupload_app/views.py

from django.shortcuts import render
from .models import UploadedFile
from .forms import FileUploadForm
from django.http import JsonResponse

# عرض لتحميل الملفات


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = FileUploadForm()
    return render(request, 'fileupload_app/upload.html', {'form': form})

# عرض لعرض الملفات المرفوعة والبحث عنها


def list_files(request):
    query = request.GET.get('q')  # الحصول على نص البحث من المستخدم
    if query:
        files = UploadedFile.objects.filter(file__icontains=query)
    else:
        files = UploadedFile.objects.all()

    return render(request, 'fileupload_app/list_files.html', {'files': files, 'query': query})
