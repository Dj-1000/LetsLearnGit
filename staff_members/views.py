from django.shortcuts import render,redirect
from .models import members
from .forms import staff_form

def member_view(request):
    context = {
        'form': staff_form()
    }
    if request.method == 'POST':
        form = staff_form(request.POST)
        if form.is_valid():
            obj = form.save()
            return render(request, 'staff_members/member_detail.html',{'obj': obj})

    return render(request, 'staff_members/member.html',context = context)

def member_detail_view(request, name = None):
    object = members.objects.get(FirstName =  name)
    context = {
        'obj': object
    }

    return render(request,'staff_members/member_detail.html',context=context)
    
