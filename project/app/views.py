from django.shortcuts import render
from .forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def regi(request):
    form=Registration()
    if request.method=='POST':
        data=Registration(request.POST)
        if data.is_valid():
            Name=data.cleaned_data['stu_name']
            Email=data.cleaned_data['stu_email']
            Contact=data.cleaned_data['stu_contact']
            # print(Name,Email,Contact)
            my_list1={'id':1,'name':'himanshi','email':'himanshi@gmail.com','contact':'7000621585'}
            my_list2={'id':2,'name':'vedansh','email':'ved@gmail.com','contact':'888'}
            my_list=[my_list1,my_list2]
            request.session['data']=my_list
        # return render(request,'set.html')
    return render(request,'regi.html',{'form':form})


def login(request):
    form=Login()
    if request.method=='POST':
        data=Login(request.POST)
        if data.is_valid():
           Email=data.cleaned_data['email']
           Contact=data.cleaned_data['contact'] 
           print(Email,Contact) 
           data1=request.session.get('data','Guest')    
        # return  render(request,'get.html',{'name':data1})
    return render(request,'login.html',{'form':form})


def delete(request):
    if 'data' in request.session:
        del request.session['data']
    #request.session.flush()      
    return render(request,'home.html')




# def regi(request):
#     form=Registration()
#     if request.method=='POST':
#         data=Registration(request.POST)
#         if data.is_valid():
#             Name=data.cleaned_data['stu_name']
#             Email=data.cleaned_data['stu_email']
#             Contact=data.cleaned_data['stu_contact']
#             # print(Name,Email,Contact)
#             # data.save()
#             response=render(request,'regi.html')
#             response.set_cookie('name',Name)
#             response.set_cookie('email',Email)
#             response.set_cookie('contact',Contact)
#             return response    
#     return render(request,'regi.html',{'form':form})


# def login(request):
#     # print(request.COOKIES)
#     form=Login()
#     if request.method=='POST':
#         data=Login(request.POST)
#         if data.is_valid():
#             Email=data.cleaned_data['email']
#             Contact=data.cleaned_data['contact']
#             # print(Email,Contact)
#             nm=request.COOKIES['name']
#             em=request.COOKIES['email']
#             con=request.COOKIES['contact']
#             data={
#                 'name':nm,
#                 'email':em,
#                 'contact':con
#             }
#             return render(request,'get.html',data)
#     return render(request,'login.html',{'form':form})


# def delete(request):
        
#         res=render(request,'home.html')
#         res.delete_cookie('name')
#         res.delete_cookie('email')
#         res.delete_cookie('contact')
#         return res   