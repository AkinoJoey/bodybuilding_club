from django.shortcuts import render
import random    
from .models import Member

def index(request):
    image_list = ['image1.webp', 'image2.webp', 'image3.webp']
    random_image = image_list[random.randint(0, len(image_list)-1)]
    context = {
        "random_image": f"members/images/index_background/{random_image}"
    
    }
    
    return render(request,'index.html', context)

def notablesList(request):
    members = Member.objects.all().values()
    context = {
        'members':  members
    }
    return render(request, 'all_members.html', context)

def notablesDetail(request, notablesIndex):
    member = Member.objects.get(id=notablesIndex)
    context = {
        'member': member
    }
    
    return render(request, 'details.html', context)

def rules(request):
    return render(request, 'rules.html')

def externalLinks(request):
    link_list = ["https://en.wikipedia.org/wiki/Arnold_Schwarzenegger","https://en.wikipedia.org/wiki/Ronnie_Coleman","https://en.wikipedia.org/wiki/Lee_Haney"]
    context = {
        "link_list": link_list
    }
    
    return render(request, 'externalLinks.html', context)
def testing(request):
    return render(request, 'base.html')