
from django.shortcuts import render
from .forms import ImageUploadForm
from .prediction import leaf_recognition
from .models import Leaf


def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded file
            image = request.FILES['image']
            image_path = handle_uploaded_file(image)
            predicted_name = leaf_recognition(image_path)
            try:
                # Case-insensitive matching
                leaf = Leaf.objects.get(latinName__iexact=predicted_name[0])
                uses = leaf.medicinalUses
                medicinal_list = []
                for i, use in enumerate(uses.split(',')):
                    use = use.strip()
                    if i == 0:
                        medicinal_list.append(use[2:-1])
                    elif i == (len(uses.split(',')) - 1):
                        medicinal_list.append(use[1:-2])
                    else:
                        medicinal_list.append(use[1:-1])
                leaf.medicinalUses = medicinal_list
                context = {
                    'leaf': leaf,
                    'prediction': predicted_name,
                    'image_path': image_path
                }
                return render(request, 'results.html', context)
            except Leaf.DoesNotExist:
                return render(request, 'results.html', {'error': 'No details found for the predicted leaf.'})
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})


def handle_uploaded_file(f):
    import os
    path = 'media/' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path
