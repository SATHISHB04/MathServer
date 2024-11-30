# Ex.05 Design a Website for Server Side Processing
## Date:27.11.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<html>
<head>
    <title>Power Calculation</title>
</head>
<body style="text-align: center; background-color: black; padding: 20px; color: white;">
    <h1 style="background-color: cyan; color: white; font-size: 50px; padding: 20px; border-radius: 10px;">
        Power of Lamp Filament
    </h1>
    <form method="POST" style="background-color: cyan; display: inline-block; padding: 50px; border-radius: 10px;">
        {% csrf_token %}
        
        <!-- Input fields for intensity and resistance -->
        <label for="intensity" style="color: white; font-size: large; background-color: red; padding: 5px; border-radius: 5px;">Intensity (I) in amperes:</label><br>
        <input type="number" id="intensity" name="intensity" step="0.01" value="{{ intensity }}" required style="padding: 8px; margin: 10px; border-radius: 5px; width: 200px;"><br><br>
        
        <label for="resistance" style="color: white; font-size: large; background-color: red; padding: 5px; border-radius: 5px;">Resistance (R) in ohms:</label><br>
        <input type="number" id="resistance" name="resistance" step="0.01" value="{{ resistance }}" required style="padding: 8px; margin: 10px; border-radius: 5px; width: 200px;"><br><br>
        
        <input type="submit" value="Calculate" style="background-color: yellow; color: black; padding: 10px 20px; border: none; cursor: pointer; font-size: medium; border-radius: 5px;"><br><br>
        
        <!-- Power result field -->
        <label for="power" style="color: white; font-size: large;">Power (P) in watts:</label><br>
        <input type="number" id="power" name="power" value="{{ power }}" readonly style="padding: 8px; margin: 10px; border-radius: 5px; width: 200px; background-color: white; color: black;"><br>
    </form>
</body>
</html>
views.py
from django.shortcuts import render

def EnergyCalc(request):
    # Initialize context with default values
    context = {
        'power': "0", 
        'intensity': "0", 
        'resistance': "0"
    }
    
    # Check if the form was submitted via POST method
    if request.method == 'POST':
        print("POST method is used")
        
        # Retrieve intensity and resistance from the form submission
        intensity = request.POST.get('intensity', '0')
        resistance = request.POST.get('resistance', '0')
        
        # Debugging output to terminal
        print('Request:', request)
        print('Intensity:', intensity)
        print('Resistance:', resistance)
        
        try:
            # Convert intensity and resistance to integers
            intensity = float(intensity)  # using float to allow decimal values
            resistance = float(resistance)  # using float to allow decimal values

            # Power calculation using the formula P = I^2 * R
            power = (intensity ** 2) * resistance
            
            # Pass the results to the template via context
            context['power'] = round(power, 2)  # rounding the result to 2 decimal places
            context['intensity'] = round(intensity, 2)
            context['resistance'] = round(resistance, 2)

            # Debugging output
            print(f'Calculated Power: {power}')

        except ValueError as e:
            # Handle invalid inputs
            print(f'Error in calculation: {e}')
            context['power'] = "Invalid input. Please enter valid numbers."

    # Render the template with context data
    return render(request, 'mathapp/math.html', context)
urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel route
    path('', views.EnergyCalc, name="EnergyCalc"),  # Home route for the calculator
]

```

## SERVER SIDE PROCE!
[alt text](<Screenshot (40).png>)SSING:


## HOMEPAGE:


## RESULT:
![alt text](<Screenshot (41).png>)

The program for performing server side processing is completed successfully.
