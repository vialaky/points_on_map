import re
import webbrowser

import folium

# Import folium MarkerCluster plugin
from folium.plugins import MarkerCluster
# Import folium MousePosition plugin
from folium.plugins import MousePosition
# Import folium DivIcon plugin
from folium.features import DivIcon

# pat = '[0-9]{2}.[0-9]+[\s,]+[0-9]{2}.[0-9]+'
pat = '[0-9]{2}.[0-9]+'
pat1 = r'[0-9]{2}[.][0-9]+'

numbers = []
locations = []

symbol1 = '.'
symbol2 = ','

with open('points.txt', encoding="utf8") as f:
    digits = re.findall(pat, f.read())

# print(digits)

for item in digits:
    if symbol1 in item:
        numbers.append(float(item))
    elif symbol2 in item:
        numbers.append(float(item.replace(',', '.')))
    elif item.isdigit():
        numbers.append(float(item[:2]+symbol1+item[2:]))

for i in range(0, len(numbers), 2):
    locations.append(list((numbers[i], numbers[i+1])))

# for loc in locations:
#     print(loc)
# for number in numbers:
# numbers = re.sub(pat, pat1, digits)
#
# # for point in points_str:
# #     print(point)
#
# print(numbers)

# correct_numbers = re.sub(pat, pat1, )

# numbers = [float(x) for x in digits]
# print(numbers)

# for item in digits:
#     if item[2] == ',':
#         item[2]

# points = list(map(list, points_str))

# points = [[x[0], x[1]] for x in points_str]

# print(points[0])

# for point in points:
#     print(point)
#
#
# print(points)

# for p in points_str:
#     print(p)

# print(float(points[0][0]))

# print(points_str)

# for point in points:
#     # print('lat:', match.group(1), 'long:', match.group(2))
#     print(point)

# print(len(digits), '/', len(numbers))
print('Количество точек:', len(locations))

# my_location = [48.737780, 37.584170]    # Kramatorsk
my_location = [49.223800, 37.291500]    # Izyum





map = folium.Map(
    location = my_location,
    zoom_start = 10
)

marker_cluster = MarkerCluster().add_to(map)



# add a red marker to Saint Petersburg
# create a feature group (создать группу функций)
# saint_petersburg = folium.map.FeatureGroup()

# style the feature group (стиль группы объектов)
# saint_petersburg.add_child(
#     folium.features.CircleMarker(
#         my_location, radius = 5,
#         color = 'red', fill_color = 'Red'
#     )
# )

# add the feature group to the map  (добавить группу объектов на карту)
# m.add_child(saint_petersburg)


for point in locations:
    # point = list(point)
    # print(point)

    folium.Marker(
        location=point,
    ).add_to(marker_cluster)


output_file = "map.html"
map.save(output_file)
webbrowser.open(output_file, new=2)  # open in new tab