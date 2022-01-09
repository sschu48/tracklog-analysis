# Created by Sean Schumacher
# Jan 9 2021
# Project created to analyze tracklog data from Foreflight

# import required modules
import csv, datetime

# create class for new file
class Tracklog:
    def __init__(self, tracklog):
        # Python variables holding data from tracklog
        self.tracklog_values = []

        # import tracklog
        with open(tracklog, newline='') as tracklog_csv:
            fields = ['Time', 'Timestamp', 'Altitude', 'Speed']
            tracklog_reader = csv.DictReader(tracklog_csv)

            # parse through tracklog file
            for row in tracklog_reader:
                row_data = {
                    'Timestamp': row['Timestamp'],
                    'Altitude': row['Altitude'],
                    'Speed': row['Speed']
                }
                # add to python list
                self.tracklog_values.append(row_data)
        # file closed

    # find average of values in numerical row)
    def find_average(self, row):
        # sum of row values
        sum = 0

        # iterate through row values and add to sum
        for item in self.tracklog_values:
            sum += item[row]
        
        # return average
        return sum / len(self.tracklog_values)