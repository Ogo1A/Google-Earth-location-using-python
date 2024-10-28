import webbrowser
def find_city_on_google_earth(city_name):
 google_earth_url=f'https://earth.google.com/web/search/{city_name}'
 webbrowser.open(google_earth_url)
city_name=input("Enter a city name:")
find_city_on_google_earth(city_name)