from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings

from .forms import HomeForm

from app.utils import *
# Create your views here.


def index(request):
    print "Blank Form"
    form = HomeForm()

    return render(request,'app/index.html',{ 'form' : form })


def music(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            filename = request.FILES['file'].name
            file = request.FILES['file']
            
            upload(file,filename) # Here upload function is called to upload the file

            track_url = form.cleaned_data['track_url']
            user_url = form.cleaned_data['user_url']
            follow =  form.cleaned_data['follow']  
            track_id = resolve_url(track_url)
            obj = form.save()
            print "Track Id: ", track_id

            if user_url and follow:
                flw(user_url)
                print "Follow called"  

            file1 = Home.objects.get(id=obj.id)
            print file1 #Obtaing the home object of the file to pass to the button
            print "Mack2"
    else:
        form = HomeForm()
        
    return render(request,'app/music.html', {'track_id':track_id, 'user_url':user_url,'follow':follow,'file':file1.file})
