# Map of Rodent related complaints in NYC 2024 

Personal mini project on visualizing data onto a map

## Data
The Dataset for this project is from NYC Open Data's 311 call database. This can be found at https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9. For the puposes of this project, only the 2024 incidents were used.

A supporting data set with the eoncodings for the NYC districts as a map json was found at https://data.cityofnewyork.us/City-Government/2020-Community-District-Tabulation-Areas-CDTAs-/xn3r-zk6y. This was used to visualize the counts.

# Project
Using the cleaned (with a python CLI argparse tool) dataset for 311 complaints relating to rodents, I matched the Community district where the complaints were made and filled a map figure with colours based on the counts.
