from django.conf import settings
from django.shortcuts import render

from django_file_upload.forms import UploadFileForm
from django_file_upload.utils import pred_attack, save_uploaded_file


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            default_filename = "test_data.csv"
            # If you want to save file just unccomment it
            save_uploaded_file(request.FILES["file"], default_filename)
            result = pred_attack(
                path_csv=settings.BASE_DIR / "static/{}".format(default_filename)
            )
            return render(request, "index.html", {"result": result})
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})
