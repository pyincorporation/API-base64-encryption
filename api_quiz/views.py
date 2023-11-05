from django.shortcuts import render
from .forms import *
from .api_request import get_user_creadentions
from django.http import HttpResponse
from .crypto import *
from .models import *
# from .crypto import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_encr = encrypt_data(password)
            get_user = get_user_creadentions(username, password)
            
            try:
              UserAccount.objects.create(username=encrypt_data(get_user[0]['usajili']), email = encrypt_data('mail@gmail.com'), majina = encrypt_data(get_user[0]['majina']), password=password_encr, sex = encrypt_data(get_user[0]['jinsia']))
              return render(request, 'api_quiz/index.html', {
              'login_form':SearchUserForm(), 
              'success':True
            })
            except Exception:
                return render(request, 'api_quiz/index.html', {
                'login_form':SearchUserForm(), 
                'error':True
              })
    return render(request, 'api_quiz/index.html', {
      'login_form':SearchUserForm()
    })

def show_users(request):
    user_dic = {}
    get_users =  UserAccount.objects.filter(is_staff=False)
    for user in get_users:
        # user_lis =[]
        user_dic['username']=decrypt_data(user.username)
        user_dic['sex']=decrypt_data(user.sex)
        user_dic['majina']=decrypt_data(user.majina)
    return render(request, 'api_quiz/show_users.html', {
        'users':user_dic
    })