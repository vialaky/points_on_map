# Points on map

This project was created to visually display points on the map. The coordinates of the points are extracted from a text message that we can receive from someone via instant messenger or e-mail.



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

The project first prompts the user to enter their location. You need to type the name of the locality where you are located and press Enter. If there are several settlements with the same name, select yours by number in the list.
The Python script then parses the text file, extracts the coordinates of the points from it and displays them on an interactive map.
The red dot is your location (the one you specified).
After all, the script shows the number of points found in the text and the distance to the nearest one relative to your location.
