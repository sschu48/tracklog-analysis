# Created by Sean Schumacher
# Jan 9 2021
# Project created to analyze tracklog data from Foreflight

# import required modules
import csv, math
from datetime import datetime

# import OS for debugging
import os

# create class for new file
class Tracklog:
    # class variables
    times = []
    timestamps = []
    altitudes = []
    speeds = []

    def __init__(self, tracklog):
        # import tracklog
        with open(tracklog) as tracklog_csv:
            tracklog_reader = csv.DictReader(tracklog_csv)

            # parse through tracklog file and create lists
            for row in tracklog_reader:
                times = list(row['Time'].split(':'))
                self.times.append(times)
                self.timestamps.append(row['Time'])
                self.altitudes.append(float(row['Altitude']))
                self.speeds.append((row['Speed']))
    
    # return highest speed
    def highest_speed(self):
        return float(max(list(self.speeds)))

    # return lowest speed
    def lowest_speed(self):
        return float(min(list(self.speeds)))

    # return highest altitude
    def highest_altitude(self):
        return float(max(list(self.altitudes)))

    # return lowest altitude
    def lowest_altitude(self):
        return float(min(list(self.altitudes)))


    # return average speed
    def average_speed(self):
        sum = 0
        for item in self.speeds: sum += float(item)

        return sum / len(self.speeds)

    # return average altitude
    def average_speed(self):
        sum = 0
        for item in self.altitudes: sum += float(item)

        return sum / len(self.altitudes)

    # return vertical climb speed
    def vertical_climb(self, initial, final):
        # find altitudes at specific times
        initial_altitude = float(self.altitudes[self.timestamps.index(initial)])
        final_altitude = float(self.altitudes[self.timestamps.index(final)])

        # strptime variables
        strptime_initial = datetime.strptime(initial, "%H:%M:%S")
        strptime_final = datetime.strptime(final, "%H:%M:%S")
        time_dif = strptime_final - strptime_initial

        return float((final_altitude - initial_altitude) / time_dif.total_seconds() * 60)

if __name__ == '__main__':
    # debugging code
    # create tracklog 1
    tracklog1 = Tracklog('tracklog-1.csv')

    tracklog1_vc = tracklog1.vertical_climb('20:25:45', '21:39:40')
    print('The vertical climb is: {vc}'.format(vc=tracklog1_vc))