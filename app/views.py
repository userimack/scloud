from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import HomeForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            request.session['track_url'] = form.cleaned_data['track_url']
            request.session['user_url'] = form.cleaned_data['user_url']
            request.session['follow'] = form.cleaned_data['follow']          
            print "sheesh"
            return HttpResponseRedirect('/music/')
    else:
        form = HomeForm()

    return render(request,'app/index.html',{ 'form' : form })


def music(request):
    track_url = request.session.get('track_url',None)
    user_url = request.session.get('user_url',None)
    follow = request.session.get('follow',None)
    c = {'track_url':track_url}
    return render_to_response('app/music.html',c)


def upload(request):
    return render(request,'app/upload.html',{ })
