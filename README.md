# GDP_Analysis

A repository analysis gdp of each US State in a particulat year
This repository also includes the functions


`def get_highest_gdp(data, year):`  
  This function will return the name of the state that has the highest GDP for the specified year. It takes in a string `year` as an argument. `data` and will be a `DictReader` object containing data.  

`def get_lowest_gdp(data, year):`  
  This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` as an argument. `data` and will be a `DictReader` object containing data.  

`def get_state_gdp(data, state, year):`  
  This function will return the single gdp value of a specific state for a specific year column. The name of the state will be passed in `state`, and the year will be passed in via `year`.

`def get_all_state_gdp(data, year):`  
  This function will return gdp values of all in-data-state for some the specific year column stated. The name of the state will be passed in `data`, and the year will be passed in via `year`.


## Results_Comparisons.py

This file holds data comparisons between 2 varying years of GDP values for a particular states.

We can see here that New York experienced a drop in GDP from 2019 to 2020? Informally, a few changed which could have caused this shift could have been due to the pandemic, a drop in employment rate, a drop in annual household income, or a combination of all three and more.

In addition to this info tdata is provided for each states GDP status over the 2 varying years to calculate whethere there was a rise or drop in GDP value. Indicating which states might have suffered or thrived during the pandemic.


## Challenge 1

This file contains the code to create  CSV files `highest_gdp.csv` & `lowest_gdp.csv` representative of the state with the highest & lowest GDP for each year.

## Challenge 2
This file creates a function called `get_percent_change` that calculates the [percent change]from 2019 to 2020 for each state.
  
  
