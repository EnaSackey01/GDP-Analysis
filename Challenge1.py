import csv

def get_highest_gdp(data, year):

        highest_gdp = float(data[0][year])
        state = ""
        #get each row
        for gdp in data:
        #get the vaue of that year for this row
            value=float(gdp[year])
            #if the value of the row is greater than my max
            if value > highest_gdp:
                #make this my new maximum
                highest_gdp = value
                state= gdp["GeoName"]
        #return state
        return state


def get_lowest_gdp(data, year):
    
        
        lowest_gdp = float(data[0][year])
        state = ""
        #get each row
        for gdp in data:
        #get the vaue of that year for this row
            value=float(gdp[year])
            #if the value of the row is greater than my max
            if value < lowest_gdp:
                #make this my new maximum
                lowest_gdp = value
                state= gdp["GeoName"]
        #return state
        return state

# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

years = [str(year) for year in range(1997, 2021)]
Highest_States=[]
for year in years:
    state=get_highest_gdp(list_data, year)
    Highest_States.append(state)
with open("highest_gdp.csv", "w") as outfile:
    # load in data as DictReader
    writer = csv.writer(outfile)
  
    writer.writerow(years)
    writer.writerow(Highest_States)

years = [str(year) for year in range(1997, 2021)]
Lowest_States=[]
for year in years:
    state=get_lowest_gdp(list_data, year)
    Lowest_States.append(state)
with open("lowest_gdp.csv", "w") as outfile:
    # load in data as DictReader
    writer = csv.writer(outfile)
  
    writer.writerow(years)
    writer.writerow(Lowest_States)
