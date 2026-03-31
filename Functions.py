# Import pi from math library
from math import pi

# Function to calculate area of a circle
def area_of_circle(radius):
    # Validate radius
    if radius <= 0:
        return "Invalid input. Radius must be greater than 0."
    
    # Compute area
    area = pi * radius ** 2
    
    # Return area rounded to 2 decimal places
    return round(area, 2)


# Example usage
r = float(input("Enter the radius of the circle: "))
result = area_of_circle(r)
print("Area of the circle:", result)