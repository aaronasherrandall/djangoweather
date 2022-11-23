from django.shortcuts import render

# Create your views here.

# python function called home that passes in request
# if user goes to our webpage through web browser, they are making request to server to bring back webpage
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})