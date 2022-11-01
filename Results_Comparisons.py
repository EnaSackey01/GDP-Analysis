from cgi import print_directory
import csv

def get_state_gdp(data, state, year):
        for row in data:
            if row ["GeoName"]==state:
                return row[year]


# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)
        
#First calculation to decifer a drop or rise in GDP value between 2020 & 2019       
twenty = float(get_state_gdp(list_data,"New York", "2020"))
nineteen = float(get_state_gdp(list_data,"New York", "2019"))
dif=twenty-nineteen
if dif<0:
    print("There was a drop in New York GDP by"+" "+str(abs(dif)))
else:
    print("There was an rise in New York GDP by"+" "+str(abs(dif)))

state = ["Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
for name in state:
    twenty = float(get_state_gdp(list_data, name, "2020"))
    nineteen = float(get_state_gdp(list_data, name, "2019"))
    dif=twenty-nineteen
    if dif<0:
        print("There was a drop in "+name+" GDP by"+" "+str(abs(dif)))
    else:
        print("There was an rise in "+name+" GDP by"+" "+str(abs(dif)))