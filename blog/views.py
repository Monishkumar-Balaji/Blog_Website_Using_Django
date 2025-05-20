from django.shortcuts import render,redirect
from django.http import HttpResponse
import logging
from .models import Post,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
# posts = [{'id':1,'title':'post 1','content': 'content of post 1'},
#              {'id':2,'title':'post 2','content': 'content of post 2'},
#              {'id':3,'title':'post 3','content': 'content of post 3'},
#              {'id':4,'title':'post 4','content': 'content of post 4'}
#              ]

# Create your views here.
def index(request):
    blog_title = "Latest Posts"

    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
 
    return render(request,'index.html',{'page_obj':page_object})

def detail(request,slug):
    #post = next((item for item in posts if item['id'] == post_id),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    try:
        post = Post.objects.get(slug = slug)
        related_posts= Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request,'detail.html',{'post':post,'related_posts':related_posts})

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(response):
    return HttpResponse("New url")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        

        if form.is_valid():
            logger = logging.getLogger("TESTING")
            logger.debug(f'POST DATA is { form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = 'Your Form is submitted successfully.'
            return render(request,'contact.html',{'form':form,'success_message':success_message})
        else:
            logger = logging.getLogger("TESTING")
            logger.debug('Form Validation failure')
        # print(name,email)
        return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'about.html',{'about_content':about_content})