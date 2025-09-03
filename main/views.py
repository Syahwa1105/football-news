from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437533',
        'name': 'Qoriana Syahwa Maharani',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
