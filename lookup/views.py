# Comment to test if Github is updating
from django.shortcuts import render

# Create your views here.

# python function called home that passes in request
# if user goes to our webpage through web browser, they are making request to server to bring back webpage
def home(request):
    import json
    import requests
    
    api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=5&API_KEY=ACCDD6CE-E76E-41AE-84EE-841C1BA6751E")
    
    # error handling
    # parse json and assign to api variable
    try:
        api = json.loads(api_requests.content)

    # if website is down or if there is an issue, throw an error
    except Exception as e:
        api = "Error..."
    
    # after data has been assigned to api variable
    # we can pass that into our app in our context variable
    # {'api': api}
    # now we can access api variable on homepage
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})