"""
with open("weather_data.csv") as data:
    data = data.readlines()
"""
from pandas import DataFrame

"""
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
"""


import pandas

data: DataFrame = pandas.read_csv("weather_data.csv")


"""
data_dict = data.to_dict()
print(data_dict)
"""

"""
temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)
print(average)
"""

# print(data["temp"].mean())

# print(data["temp"].max())
"""
print(data["condition"])
print(data.condition)
"""

# Get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

"""
monday = data[data.day == "Monday"]
monday_temp = monday.temp * 9/5 + 32
print(monday_temp)
"""

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")




