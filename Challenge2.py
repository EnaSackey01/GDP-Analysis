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

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))



x = get_state_gdp(list_data, "New York", "2020")
y = get_state_gdp(list_data, "New York", "2019")

print(x, y)

def get_percent_change(state, year1, year2):
    old = float(get_state_gdp(list_data, state, year1))
    new = float(get_state_gdp(list_data, state, year2))

    perc_change = ((old - new)/old) *100
    return str(perc_change) +"%"

#print(float(x) - float(y))
print(get_percent_change("New York", "2020", "2019"))
