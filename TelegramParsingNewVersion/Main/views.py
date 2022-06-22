from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import *
import subprocess

# Create your views here.
def page_login(request):
    if request.user.is_authenticated:
        return redirect('Telegram')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(to='Telegram')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='Main/Login.html', context=context)

def page_quit(request):
    logout(request)
    return redirect('Login')

class SaveForms:

    def __init__(self):
            self.sms_form = SMSForm()
            self.number_phone_form = NumberPhoneForm()
            self.name_channel_form = NameChannelForm()
            self.password_form = PasswordForm()
    
    def set_number_phone_form(self, req_number_phone_form):
        self.number_phone_form = NumberPhoneForm(req_number_phone_form)
    
    def set_sms_form(self, req_sms):
        self.sms_form = SMSForm(req_sms)

    def set_password_form(self, req_password):
        self.password_form = PasswordForm(req_password)

    def set_req_name_channel_form(self, req_name_channel):
        self.name_channel_form = NameChannelForm(req_name_channel)

    def get_req_sms_form(self):
        return self.sms_form

    def get_req_number_phone_form(self):
        return self.number_phone_form

    def get_req_password_form(self):
        return self.password_form
    
    def get_req_name_channel_form(self):
        return self.name_channel_form

# class Process:

#     def __init__(self, process):
#         self.process = process

#     def input_text(self, value):
#         self.process.communicate(input=value)

#     def input_text_2(self, value):
#         self.process.stdin.write(value)
#         self.process.stdin.close()

def page_telegram(request):
    global form     #, process
    # print(request.user) отвечает за вошедшего пользователя
    if not request.user.is_authenticated:
        return redirect('Login')
    if request.GET != {}:
        if 'START' in request.GET:
            # program = ["python", r"C:\Users\EXCLUSIVE\Desktop\unit.py"]
            subprocess.Popen(["python", r"pars.py"])#"C:\Users\EXCLUSIVE\Desktop\python файлы\TelegramParsingNewVersion\pars.py"
            # process = Process(process=start_script)
        elif 'number_phone' in request.GET:
            form.set_number_phone_form(request.GET)
            with open(file='number_phone.txt', mode='w', encoding='utf-8') as file:
                file.write(request.GET['number_phone'])
            # os.write(process.stdout.fileno(), request.GET['number_phone'])
            # process.input_text(value=request.GET['number_phone'])
            # process.input_text_2(request.GET['number_phone'])
        elif 'sms_code' in request.GET:
            form.set_sms_form(request.GET)
            with open(file='sms_code.txt', mode='w', encoding='utf-8') as file:
                file.write(request.GET['sms_code'])
            # process.input_text(value=request.GET['sms_code'])
        elif 'password' in request.GET:
            form.set_password_form(request.GET)
            with open(file='password.txt', mode='w', encoding='utf-8') as file:
                file.write(request.GET['password'])
        elif 'name_channel' in request.GET:
            form.set_req_name_channel_form(request.GET)
            with open(file='name_channel.txt', mode='w', encoding='utf-8') as file:
                file.write(request.GET['name_channel'])
            # process.input_text(value=request.GET['name_channel'])
    else:
        form = SaveForms()
    context = {
        'number_phone_form': form.get_req_number_phone_form(),
        'sms_form': form.get_req_sms_form(),
        'password_form': form.get_req_password_form(),
        'name_channel_form': form.get_req_name_channel_form()
    }
    return render(request, template_name='Main/Telegram.html', context=context)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')