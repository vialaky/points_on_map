import folium
from folium.plugins import MarkerCluster

import geopy
from geopy import distance
from geopy.geocoders import Nominatim

import re
import sys
import webbrowser


# Initialize variables
numbers = []
points = []
distance2point = {}

pat = '[0-9]{2}.[0-9]+'     # pattern for searching coordinates
symbol1 = '.'
symbol2 = ','

geolocator = Nominatim(user_agent="points_on_map")     # Geocoder’s initialization)


# Reading the message
with open('message.txt', encoding="utf8") as f:
    digits = re.findall(pat, f.read())

for item in digits:
    if symbol1 in item:
        numbers.append(float(item))
    elif symbol2 in item:
        numbers.append(float(item.replace(',', '.')))
    elif item.isdigit():
        numbers.append(float(item[:2] + symbol1 + item[2:]))

for i in range(0, len(numbers), 2):
    points.append(list((numbers[i], numbers[i + 1])))


while True:

    try:
        # print('2')
        address = str(input('Enter your location: \n'))  # Получаем интересующий нас адрес
        locations = geolocator.geocode(address,
                                       exactly_one=False)  # Создаем переменную, которая состоит из нужного нам адреса
        locations_ua = [loc_ua for loc_ua in locations if 'Україна' in loc_ua.address]

        size = len(locations_ua)
        for i in range(size):
            print(i + 1, locations_ua[i])
        if size == 1:
            location = locations_ua[i]
            # break
        elif size > 1:
            print('Enter the number of your place:')
            num = int(input())

            location = locations_ua[num - 1]
            print(f'Your location is: \n{location}')
            # break
        else:
            print('!!! No matches. Try again!')

        # print('3')

        print(location.latitude, location.longitude)  # И теперь выводим GPS-координаты нужного нам адреса

        my_location = [location.latitude, location.longitude]

        map = folium.Map(
            location=my_location,
            zoom_start=10
        )

        folium.CircleMarker(
            location=my_location,
            radius=4,
            color='red',
            fill_color='Red',
            fill_opacity=0.9
        ).add_to(map)

        marker_cluster = MarkerCluster().add_to(map)

        for point in points:
            folium.Marker(
                location=point,
            ).add_to(marker_cluster)

            distance2point[points.index(point) + 1] = round(distance.distance(my_location, tuple(point)).km, 1)

        output_file = "map.html"
        map.save(output_file)
        webbrowser.open(output_file, new=2)  # open in new tab

        print('Number of locations in message:', len(points))

        print('Min distance:', min(distance2point.values()))
        sys.exit()

    except TypeError:
        print('!!! No matches. Try again!')
    except geopy.exc.GeocoderUnavailable:  # requests.exceptions.ConnectionError:
        print('Bad connect. Restart...')
