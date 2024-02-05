# Points on map

This project was created to visually display points on the map. The coordinates of the points are extracted from a text message that we can receive from someone via instant messenger or e-mail.
![Display points on the map](https://github.com/vialaky/points_on_map/blob/main/docs/points_on_map_screenshot1.png)


## Installation

```
git clone https://github.com/vialaky/points_on_map.git
```

Using the requirements file.

```
pip install -r requirements.txt
```

Place the text file with the coordinates in your project folder. Let it be called "message.txt"

## Execution

```
python main.py
```

## How to use

The project first prompts the user to enter their location. You need to type the name of the locality where you are located and press Enter. 

![Enter your location](https://github.com/vialaky/points_on_map/blob/main/docs/points_on_map_screenshot2.png)

If there are several settlements with the same name, select yours by number in the list.

![Choose your location from the list](https://github.com/vialaky/points_on_map/blob/main/docs/points_on_map_screenshot3.png)

The Python script then parses the text file, extracts the coordinates of the points from it and displays them on an interactive map.
The red dot is your location (the one you specified).
After all, the script shows the number of points found in the text and the distance to the nearest one relative to your location.

![Calculate number of points and the minimal distance from your location](https://github.com/vialaky/points_on_map/blob/main/docs/points_on_map_screenshot4.png)

