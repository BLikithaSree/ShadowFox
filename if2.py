"""Write a program to determine which country a city belongs to. Given
list of cities per country:
Australia = \["Sydney","Melbourne","Brisbane","Perth"]
UAE = \["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = \["Mumbai","Bangalore","Chennai","Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
"""

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter a city name: ").strip()
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")
