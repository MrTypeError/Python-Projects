import pandas as pd

data = pd.read_csv("Python-Projects/CSV_and_Pandas/Squral_Data_analysis_using_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
far_color = data["Primary Fur Color"].to_list()

# first Approach

gray , black , cinimon = 0 , 0 , 0
for i in far_color:
    if (i == "Gray"):
        gray += 1
    elif i == "Cinnamon":
        cinimon += 1 
    else:
        black += 1

counter_data = {
    "Far Color" : ["Gray" , "Cinnamon" , "Black"],
    "Count" : [gray , cinimon , black]
}



new_data = pd.DataFrame(counter_data)
new_data.to_csv("Python-Projects/CSV_and_Pandas/Squral_Data_analysis_using_pandas/Fur_Color_Counter.csv")