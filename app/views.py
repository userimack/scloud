from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from wsgiref.util import FileWrapper
import StringIO
import mimetypes
from django.conf import settings

from .forms import HomeForm

from app.utils import *
# Create your views here.


def index(request):
    # if request.method == 'POST':
    #     form = HomeForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         file = request.FILES['file']

    #         print file, file.name, "Debug point"

    #         upload(file)

    #         # request.session['track_url'] = form.cleaned_data['track_url']
    #         # request.session['user_url'] = form.cleaned_data['user_url']
    #         # request.session['follow'] = form.cleaned_data['follow']    
    #         track_url = form.cleaned_data['track_url']
    #         user_url = form.cleaned_data['user_url']
    #         follow =  form.cleaned_data['follow']        
    #         print track_url , user_url, follow
    #         return HttpResponseRedirect('/music/')
    # else:
    #     
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
            
            print "Debug point 22222"

            #upload(file,filename)

            track_url = form.cleaned_data['track_url']
            user_url = form.cleaned_data['user_url']
            follow =  form.cleaned_data['follow']  
            track_id = resolve_url(track_url)
            obj = form.save()
            print "Track Id: ", track_id

            # if user_url and follow:
            #     flw(user_url)

            #     print "Follow called"       
            file1 = Home.objects.get(id=obj.id)
            print file1
            print "Mack2"
    else:
        print "Else part"
        form = HomeForm()
        
    return render(request,'app/music.html', {'track_id':track_id, 'user_url':user_url,'follow':follow,'file':file1.file})

# def download(request,file):

#     file_path = settings.MEDIA_ROOT +'/'+ file
#     # file_wrapper = FileWrapper(file)  #(file(file_path,'rb'))
#     # file_mimetype = mimetypes.guess_type(file_path)
#     # response = HttpResponse(file_wrapper, content_type=file_mimetype )
    
#     # response['Content-Length'] = os.stat(file_path).st_size
#     # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file) 
#     # return response
#     #myfile = StringIO.StringIO()
#     file_wrapper = FileWrapper(file)
#     file_mimetype = mimetypes.guess_type(file_path)
#     response = HttpResponse(content_type='mp3/music' )
#     response['X-Sendfile'] = file_path
#     # response = HttpResponse(content_type='mp3/music')
#     response['Content-Disposition'] = 'attachment; filename=%s' % file
#     #response.write(file)
#     return response

# def location(request,pk):
#     obj2=Home.objects.get(pk=pk)
#     return render(request,'app/music.html',{'obj2':obj2})
