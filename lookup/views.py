# Comment to test if Github is updating
from django.shortcuts import render

# Create your views here.

# python function called home that passes in request
# if user goes to our webpage through web browser, they are making request to server to bring back webpage
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=ACCDD6CE-E76E-41AE-84EE-841C1BA6751E")
        
        # error handling
        # parse json and assign to api variable
        try:
            api = json.loads(api_requests.content)

        # if website is down or if there is an issue, throw an error
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"    
    
        
        # after data has been assigned to api variable
        # we can pass that into our app in our context variable
        # {'api': api}
        # now we can access api variable on homepage
        return render(request, 'home.html', {'api': api,
        'category_description': category_description,
        'category_color': category_color})

    else:
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=5&API_KEY=ACCDD6CE-E76E-41AE-84EE-841C1BA6751E")
        
        # error handling
        # parse json and assign to api variable
        try:
            api = json.loads(api_requests.content)

        # if website is down or if there is an issue, throw an error
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"    
    
        
        # after data has been assigned to api variable
        # we can pass that into our app in our context variable
        # {'api': api}
        # now we can access api variable on homepage
        return render(request, 'home.html', {'api': api,
        'category_description': category_description,
        'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})