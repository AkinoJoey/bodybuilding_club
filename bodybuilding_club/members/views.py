from django.shortcuts import render, get_object_or_404
import random    
from django.views.generic import TemplateView
from .models import Member
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self):
        image_list = ['image1.webp', 'image2.webp', 'image3.webp']
        random_image = image_list[random.randint(0, len(image_list)-1)]
        context = {
            "random_image": f"members/images/index_background/{random_image}"
        
        }
        
        return context

def members(request):
    members = Member.objects.all().values()
    context = {
        'members':  members
    }
    return render(request, 'all_members.html', context)

def details(request, id):
    member = Member.objects.get(id=id)
    context = {
        'member': member
    }
    
    return render(request, 'details.html', context)

def rules(request):
    return render(request, 'rules.html')

def testing(request):
    return render(request, 'base.html')
