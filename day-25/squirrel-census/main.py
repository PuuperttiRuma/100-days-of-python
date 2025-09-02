import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Mitä pitikään tehä?
# oravien väreistä piti tehdä csv joka laskee niiden määrät


fur_color_series = data["Primary Fur Color"]

black_rows = data[fur_color_series == "Black"]
black_series = black_rows["Primary Fur Color"]
cinnamon_rows = data[fur_color_series == "Cinnamon"]
cinnamon_series = cinnamon_rows["Primary Fur Color"]
gray_rows = data[fur_color_series == "Gray"]
gray_series = gray_rows["Primary Fur Color"]

fur_color_counts_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_series.count(), cinnamon_series.count(), gray_series.count() ]
}

fur_color_counts_data = pandas.DataFrame(fur_color_counts_dict)
fur_color_counts_data.to_csv("fur_color_counts.csv")
