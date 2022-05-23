from django.shortcuts import render

# Create your views here.
class Process:

    def __init__(self, process):
        self.process = process

    def input_text(self, value):
        self.process.communicate(input=value)

def index(request):
    print('перешел')
    import subprocess
    program = ["python", r"C:\Users\EXCLUSIVE\Desktop\Untitled-1.py"]
    fun = subprocess.Popen(program, stdin=subprocess.PIPE, encoding='utf-8')
    process = Process(process=fun)
    # setting = request.GET['settings']
    if request.GET != {}:
        a = list(request.GET.keys())
        if a[0] == 'settings':
            if request.GET['settings'].lower() == 'start':
                print('Я попал на старт')
                import subprocess
                program = ["python", r"C:\Users\EXCLUSIVE\Desktop\Untitled-1.py"]
                # process = Process(subprocess.Popen(program))
                # program = subprocess.Popen(program)

        elif a[0] == 'SMS':
            print('Я попал на смс', request.GET['SMS'])
            process.input_text(value=request.GET['SMS'])
    return render(request=request, template_name='Parsing/WorkParsing.html')