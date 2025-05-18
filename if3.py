"""Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.

Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
"""


countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()
def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None
country1 = find_country(city1)
country2 = find_country(city2)
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print(f"{city1} is in {country1}, and {city2} is in {country2}")
else:
    print("One or both cities are not in the list.")
