from django.shortcuts import render

# Create your views here.
def index(request):
    print('перешел')
    # setting = request.GET['settings']
    if request.GET != {}:
        a = list(request.GET.keys())
        if a[0] == 'settings':
            if request.GET['settings'].lower() == 'start':
                print('Я попал на старт')
        #         import subprocess
        #         subprocess.call(["python", "pars copy.py"])
        elif request.GET.keys() == 'SMS':
            print('Я попал на смс')
    return render(request=request, template_name='Parsing/WorkParsing.html')