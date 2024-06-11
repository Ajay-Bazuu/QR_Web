from django.shortcuts import render
from .models import FilesCollect

urlExtractedFromBack=FilesCollect.url_text
print(urlExtractedFromBack)
# Create your views here.
def home(request):
    return render(request,'QRGeneratorApp/home.html')

def convert_(request):
    if request.method=='POST':
        print(request.FILES)
        url_copied=request.POST['url_copied'] 
        bg_image=request.FILES['image_upload']
        FilesCollect.objects.create(url_text=url_copied,img_upload=bg_image)
        
    return render(request,'QRGeneratorApp/convert_.html')

def viewData(request):
    files = FilesCollect.objects.all()
    return render(request, 'QRGeneratorApp/viewData.html', {'files': files})

