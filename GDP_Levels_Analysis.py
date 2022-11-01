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
        return "Highest GDP State"+" - "+state


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
        return "Lowest GDP Stats"+" - "+state

def get_state_gdp(data, state, year):
        for row in data:
            if row ["GeoName"]==state:
                return row["GeoName"]+" - "+row[year]

def get_all_states_gdp(data, year):
    state = ["Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    for name in state:
        for row in data:
            if row["GeoName"]==name:
                print(row["GeoName"],"-",float(row[year]))


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

# get any state's gdp for 2020 using "get_state_gdp(list_data, 'state', '2020')"
print(get_state_gdp(list_data,"New York", "2020"))

# get all the state's gdps for 2020 using "get_states_gdp(list_data, '2020')"
get_all_states_gdp(list_data, "2020")
