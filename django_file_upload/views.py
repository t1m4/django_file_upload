from django.http import HttpResponse
from django.shortcuts import render

from django_file_upload.forms import UploadFileForm
from django_file_upload.utils import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("You successfully uploaded file")
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
