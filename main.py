import re

points = {}
str_latitude = ''
str_longitude = ''
result = []

pat = '([0-9]{2}.[0-9]+)[\s,]+([0-9]{2}.[0-9]+)'

with open('points.txt', encoding="utf8") as f:
    points = re.findall(pat, f.read())

for point in points:
    # print('lat:', match.group(1), 'long:', match.group(2))
    print(point)

print(len(points))
