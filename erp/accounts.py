from django.shortcuts import render

def accounts_view(request):
    # Your view logic here
    return render(request, 'accounts_dashboard.html')


