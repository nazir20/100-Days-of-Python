# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()
# print(data)
#
#
#
# import csv
#
# with open('weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)
#
#
#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
#
#

# weather_data = pandas.read_csv('weather_data.csv')
# data_dict = weather_data.to_dict()
# print(data_dict)
# temp_list = weather_data['temp'].to_list()
# print(temp_list)
#
# @get data in a row
# print(weather_data[weather_data.temp == weather_data.temp.max()])
#
# @create a dataframe from scratch:
# data_dict = {
#     'students': ['Demir', 'Kaya', 'Taylan'],
#     'scores': [100, 97, 85]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
#
#
#
# import pandas
#
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# #
# grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
# red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
# #
# # @constructing our data frame:
# data_dict = {
#     'Fur Color': ['Grey', 'Cinnamon', 'Black'],
#     'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# #
# df = pandas.DataFrame(data_dict)
# print(df)












