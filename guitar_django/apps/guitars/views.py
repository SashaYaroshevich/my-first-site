from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Guitar

def index(request):
    latest_guitars_list = Guitar.objects.order_by('id')
    return render(request, 'guitars/list.html', {'latest_guitars_list': latest_guitars_list})

def detail(request, guitar_id):
    try:
        a = Guitar.objects.get( id = guitar_id )
    except:
        raise Http404("Гитара не найдена!")
    
    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'guitars/detail.html', {'guitar': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, guitar_id):
    try:
        a = Guitar.objects.get( id = guitar_id )
    except:
        raise Http404("Гитара не найдена!")
    
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('guitars:detail', args = (a.id,)))
