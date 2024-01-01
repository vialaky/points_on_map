import re

points = {}
str_latitude = ''
str_longitude = ''
result = []

with open('points.txt', encoding="utf8") as f:
    text = f.read()


# pat = r'\d\d'
pat = '([0-9]{2}.[0-9]+)[\s,]+([0-9]{2}.[0-9]+)'


points = re.findall(pat, text)

for point in points:
    # print('lat:', match.group(1), 'long:', match.group(2))
    print(point)

print(len(points))


