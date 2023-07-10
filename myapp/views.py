from django.shortcuts import render,redirect

from .models import Person,Customer
from .forms import CustomerForm
# Create your views here.
def customer_form(request):
    form=CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("customers-list")
    ctx={
        "form":form
    }
    return render(request,"form.html",ctx)






def main(request):
    if request.POST:
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
    return render(request,'index.html')


# def register(request):
#     if request.POST:

#         print(request.POST)
#     return render(request,'register.html')