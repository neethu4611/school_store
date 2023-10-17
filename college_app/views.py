from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Register,Department,Course
def collegestore(request):
    dept=Department.objects.all()
    return render(request,'templates/index.html',{'dept':dept})
def reg(request):


    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     dob = request.POST.get('dob')
    #     age = request.POST.get('age')
    #     phone = request.POST.get('phone')
    #     email = request.POST.get('email')
    #     course = request.POST.get('course')
    #     purpose = request.POST.get('purpose')
    #     material = request.POST.get('material')
    #     address = request.POST.get('address')
    #     dept_name=request.POST.get('dept_name')
    #     register=Register.objects.create_user(name=name,dob=dob,age=age,phone=phone,e_mail=email,course=course,purpose=purpose,material=material,address=address,dept_name=dept_name)
    #     register.save();
    #       messages.success(request, 'Order confirmed')
    #       return redirect('/')
            return render(request, 'reg.html')
