import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = 0
red = 0
black = 0

for fur_color in data["Primary Fur Color"]:
    if fur_color == "Gray":
        grey += 1
    if fur_color == "Cinnamon":
        red += 1
    if fur_color == "Black":
        black += 1

fur_color_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

squirrel_count = pandas.DataFrame(fur_color_count)
squirrel_count.to_csv("squirrel_count.csv")