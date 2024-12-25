# import csv
# with open("Python-Projects/CSV_and_Pandas/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
# print(temperatures)


import pandas

# data = pandas.read_csv("Python-Projects/CSV_and_Pandas/weather_data.csv")
# print(data)
# print(data["temp"]) # this is a series 
# my_list = data["temp"].to_list()
# print(my_list)

# sum =0
# max_finder = 0
# for i in my_list:
#     # sum+= i
#     if max_finder < i:
#         max_finder = i

# print(max_finder) # finding the max value using normal logic
# print(data["temp"].max()) # finding the max value using max function in pandas
# # print(sum/len(my_list))

# #get data in columns
# print(data["condition"])
# print(data.condition)

# #get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# find mondays temp and convert it to fahrenheit

# monday = data[data.day == "Monday"]
# my_temp = (monday.temp[0])*(9/5)+32
# print(my_temp)

# How to create a dataframe from scratch
data_dict = {
    "students" : ["Amy" , "James" , "Angela"],
    "scores" : [33 , 22 , 46]
}
data = pandas.DataFrame(data_dict)
data.to_csv("output.xlsx")