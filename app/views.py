from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import HomeForm

from app.utils import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']
            print file, file.name, "Debug point"
            upload(file)

            # request.session['track_url'] = form.cleaned_data['track_url']
            # request.session['user_url'] = form.cleaned_data['user_url']
            # request.session['follow'] = form.cleaned_data['follow']    
            track_url = form.cleaned_data['track_url']
            user_url = form.cleaned_data['user_url']
            follow =  form.cleaned_data['follow']        
            print track_url , user_url, follow
            return HttpResponseRedirect('/music/')
    else:
        print "Blank Form"
        form = HomeForm()

    return render(request,'app/index.html',{ 'form' : form })


def music(request):
    # track_url = request.session.get('track_url',None)
    # user_url = request.session.get('user_url',None)
    # follow = request.session.get('follow',None)
    # c = {'track_url':track_url}
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            filename = request.FILES['file'].name
            file = request.FILES['file']
            print file," + ", filename

            print "Debug point 22222"
            upload(file,filename)

            # request.session['track_url'] = form.cleaned_data['track_url']
            # request.session['user_url'] = form.cleaned_data['user_url']
            # request.session['follow'] = form.cleaned_data['follow']      
            track_url = form.cleaned_data['track_url']
            user_url = form.cleaned_data['user_url']
            follow =  form.cleaned_data['follow']  
            track_id = resolve_url(track_url)
            print "Track Id: ", track_id
            if user_url and follow:
                flw(user_url)
                print "Follow called"       
            #print track_url , user_url, follow

            # return HttpResponseRedirect('/music/')
            print "Mack2"
    else:
        print "Else part"
        form = HomeForm()
        
    return render(request,'app/music.html', {'track_id':track_id, 'user_url':user_url,'follow':follow})


# def upload(request):
#     return render(request,'app/upload.html',{ })
