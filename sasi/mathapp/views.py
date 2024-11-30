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
