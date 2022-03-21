from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
import requests

    

# Create your views here.
def index(request):
    response = requests.get('https://medber.herokuapp.com/medicines').json()
    
    return render(request,'home.html',{'response':response})

def denglu(request):
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['pwd'])
        if user is None:
            return render(request,'login.html',{ "Error":"用户名不存在！" })
        else:
            login(request, user)
            return redirect('shop:index')
    else:
        return render(request,'login.html')
# def xiaomi(request):
#     return render(request,'child.html')
def dengchu(request):
    logout(request)
    return redirect('shop:index')

def register(request):
    if request.method == 'POST':
        register_list = customize(request.POST)
        if register_list.is_valid():
            register_list.save()
            user = authenticate(username=register_list.cleaned_data['username'],password=register_list.cleaned_data['password1'])
            user.email = register_list.cleaned_data['email']
            register_user(user=user,nickname=register_list.cleaned_data['nickname'],phone=register_list.cleaned_data['phone'],Verification_problem=register_list.cleaned_data['Verification_problem'],Verification_answer=register_list.cleaned_data['Verification_answer']).save()
            # login(request,user)
            return redirect('shop:index')
    else:
        register_list = customize()

    info = {'注册表单':register_list}
    return render(request,'register.html',info)

def shouji(request):#商品所有目录页
    # content = {'所有商品': product.objects.all()}
    allcategories = goods.objects.all()
    content_list = []
    for content in allcategories:
        content_list.append((content ,product.objects.filter(category=content)[:3]))
    content = {'content_list':content_list,'allcategories':allcategories}
    return render(request,'shopping.html',content)


def specific(request,leibie_id):#商品页
    allcategories = goods.objects.all()
    need = get_object_or_404(goods, id=leibie_id)
    content_list = [(need, product.objects.filter(category=need)[:10])]
    content = {'content_list': content_list,'allcategories':allcategories}
    return render(request, 'specific.html', content)


def details(request,leibie_id,a_id):#某商品具体页
    allcategories = goods.objects.all()
    goods1 = get_object_or_404(product, id=a_id)
    content = {'goods1': goods1, 'allcategories':allcategories}
    return render(request, 'details.html', content)


