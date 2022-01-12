# Tracklog Analysis
## Analyzing data imported from Foreflight

## What is the purpose of this script?
The purpose of this script is to demonstrate using the power of Python and Data Acquisition to solve and analyze problems in a real world scenario. 

This script is a simple script that imports, parses, and analyzes data from a .CSV file. 
This .CSV file comes straight from Foreflight's logging feature online that keeps a track log of your flight with associated data such as speed and altitude.

## Getting from numbers to applicable information

1. Data starts in raw for stores in a .CSV
![Image of .CSV file](/assets/Screen%20Shot%202022-01-11%20at%2019.38.33.png)

2. Import that data into a Python script creating an object
3. Then methods are create to access different information about that object such as: speed or altitude at a given time
4. Functions such as "vertical_climb" allow us to calculate valuable information letting us know our climb rate
5. Now we debug

## Debugging and solving errors in code
Using the power of "breakpoints" in Visual Studio Code and it's debugging tool, it was straightforward identifying where the bugs where.
Type Error was the most common bug because throughout manipulating the data from string to float you need to make sure the variable was in its proper from before it could be further processed.
Calculation such as the ones used in "vertical_climb" where very simple but applied the value of **writing out your logic on paper first**.
This helped solve any confusion that syntax would create. 