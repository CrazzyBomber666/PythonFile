from django.shortcuts import render

# Create your views here.
def index(request, process=None):
    print('перешел')
    # setting = request.GET['settings']
    if request.GET != {}:
        a = list(request.GET.keys())
        if a[0] == 'settings':
            if request.GET['settings'].lower() == 'start':
                print('Я попал на старт')
                import subprocess
                process={'a':'f'}
                # program = ["python", "pars.py"]
                # process = subprocess.Popen(program)
                # request.session['process'] = process
                # subprocess.call(["python", "pars.py"])
        elif a[0] == 'SMS':
            print(process)
            print('Я попал на смс', request)
            # process.communicate(input=request.GET['SMS'])
    return render(request=request, template_name='Parsing/WorkParsing.html', context=process)