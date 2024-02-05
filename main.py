import folium
from folium.plugins import MarkerCluster

import geopy
from geopy import distance
from geopy.geocoders import Nominatim

import re
import sys
import webbrowser


# Initiate variables
location = []
numbers = []
points = []
distance2point = {}

pat = '[-0-9]{1,2}.[0-9]+'     # pattern for searching coordinates
symbol1 = '.'
symbol2 = ','

geolocator = Nominatim(user_agent="points_on_map")     # Geocoder’s initialization


# Read the message and finding the elements according to the pattern
with open('message.txt', encoding="utf8") as f:
    digits = re.findall(pat, f.read())

# Bring found elements back to form "(X)X.XXXXXXX"
for item in digits:
    if symbol1 in item:
        numbers.append(float(item))
    elif symbol2 in item:
        numbers.append(float(item.replace(',', '.')))
    elif item.isdigit():
        numbers.append(float(item[:2] + symbol1 + item[2:]))

# Make a list of coordinates
for i in range(0, len(numbers), 2):
    points.append(list((numbers[i], numbers[i + 1])))


while True:

    try:
        # Type our location
        address = str(input('Enter your location: \n'))
        locations = geolocator.geocode(address, exactly_one=False)
        size = len(locations)

        # Use it if there is only one match
        if size == 1:
            location = locations[0]
            print(f'Your location is: \n{location}')

        # Offer to select if there is more than one match
        elif size > 1:
            for i in range(size):
                print(i + 1, locations[i])
            print('Enter the number of your place:')
            num = int(input())
            location = locations[num - 1]
            print(f'Your location is: \n{location}')
        else:
            print('!!! No matches. Try again!')

        # Display the coordinates of our location (latitude, longitude)
        print(location.latitude, location.longitude)
        my_location = [location.latitude, location.longitude]

        # Create a Folium Map object
        my_map = folium.Map(
            location=my_location,
            zoom_start=6
        )

        # Initiate a red circle marker
        folium.CircleMarker(
            location=my_location,
            radius=4,
            color='red',
            fill_color='Red',
            fill_opacity=0.9
        ).add_to(my_map)

        # Initiate a cluster of markers
        marker_cluster = MarkerCluster().add_to(my_map)

        # Add points to map
        for point in points:
            folium.Marker(
                location=point,
            ).add_to(marker_cluster)

            # Calculate the distance from my location to each point
            distance2point[points.index(point) + 1] = round(distance.distance(my_location, tuple(point)).km, 1)

        # Launch a webpage with the map
        output_file = "map.html"
        my_map.save(output_file)
        webbrowser.open(output_file, new=2)  # open map in new tab

        print('Number of locations in message:', len(points))
        print('Min distance:', min(distance2point.values()), 'km')
        sys.exit()

    except TypeError:
        print('!!! No matches. Try again!')
    except geopy.exc.GeocoderUnavailable:
        print('Bad connect. Restart...')
