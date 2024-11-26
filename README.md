# Ex.05 Design a Website for Server Side Processing
## Date:

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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator for Lamp Filament</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f9;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        input, button {
            padding: 10px;
            margin: 10px;
            font-size: 16px;
            width: 200px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body style="background-color:yellowgreen;">
    <h1>Calculate Power of Lamp Filament</h1>
    <form id="powerForm">
        <label for="intensity">Enter Current Intensity (I in Amps):</label><br>
        <input type="number" id="intensity" required><br><br>

        <label for="resistance">Enter Resistance (R in Ohms):</label><br>
        <input type="number" id="resistance" required><br><br>

        <button type="button" onclick="calculatePower()">Calculate power</button>
    </form>

    <div class="result" id="result"></div>

    <script>
        function calculatePower() {
            // Get the values of intensity and resistance
            const intensity = document.getElementById('intensity').value;
            const resistance = document.getElementById('resistance').value;

            // Validate input values
            if (!intensity || !resistance || intensity <= 0 || resistance <= 0) {
                alert("Please enter valid positive numbers for both intensity and resistance.");
                return;
            }

            // Calculate power using the formula P = I^2 * R
            const power = Math.pow(intensity, 2) * resistance;

            // Display the result
            document.getElementById('result').textContent = `Power (P) = ${power.toFixed(2)} Watts`;
        }
    </script>
</body>
</html>

views.py
from django.shortcuts import render 
def powercalc(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('intensity','0')
        R = request.POST.get('resistance','0')
        print('request=',request) 
        print('intensity=',I) 
        print('resistance=',R) 
        power = (int(I) * int(I) ) * int(R) 
        context['power'] = power
        context['intensity'] = I
        context['resistance'] = R 
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

urls.py
from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powercalculator/',views.powercalc,name="powercalculator"),
    path('',views.powercalc,name="powercalculatorroot")
]
```
# SERVER SIDE PROCESSING:
#![alt text](<Screenshot (30).png>)

# HOMEPAGE:
#![alt text](<Screenshot (29).png>)


## RESULT:
The program for performing server side processing is completed successfully.
