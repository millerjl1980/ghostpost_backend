from django.shortcuts import render, HttpResponseRedirect
from ghostpost.forms import AddPostForm

# Create your views here.
def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("http://localhost:3000/")
    else:
        form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})
