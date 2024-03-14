'''
You are asked to implement a program for managing the database of a city public transportation center.
The information is stored in a file whose name is passed as command line argument. Each line in the
file contains: the ID number of the public transport bus, the number of the route the bus serves, the
geometric coordinates in meters (abscissa and ordinate, i.e., x-axis and y-axis) and the time in seconds
(all the time values belong to the same day) when the bus is checked. For example, the file can contain:
2187 13 10 1003 18000
3002 4 5000 5 18100
2187 13 100 2030 18500
3002 4 5000 1100 18600
2187 13 300 3300 19200
3002 4 5000 2200 19200
1976 4 5000 5 18600
1976 4 5000 1100 19600
1976 4 5000 2200 20100
We make the following assumptions:
• All the file can be loaded in memory
• Each bus serves only one line
• Multiple buses can serve the same line
The program receives the following parameters from the command line: 1) the name of the file containing
the database and, 2) a flag, followed by an additional parameter.
• If the flag is ’-b’, the next parameter is a busId. The program should print the total distance
traveled by the given bus
• If the flag is ’-l’, the next parameter is a lineId. The program should print the average speed of
buses traveling on the line
For example:
$> python lab_1_2.py lab_1_2.txt -b 1976
1976 - Total Distance: 2195.0
$> python lab_1_2.py lab_1_2.txt -l 4
4 - Avg Speed: 1.6884615384615385
'''

import sys

class BusRecord:
    def __init__(self, busId, lineId, x, y, t):
        self.busId = busId
        self.lineId = lineId
        self.x = x
        self.y = y
        self.t = t


def loadAllRecords(fName):
    try:
        lRecords = []
        with open(fName) as f:
            for line in f:
                busId, lineId, x, y, t = line.split()
                record = BusRecord(busId, lineId, int(x), int(y), int(t))
                lRecords.append(record)
        return lRecords
    except:
        raise  # If we do not provide an exception, the current exception is propagated


def euclidean_distance(r1, r2):
    return ((r1.x - r2.x) ** 2 + (r1.y - r2.y) ** 2) ** 0.5


def computeBusDistanceTime(lRecords, busId):
    busRecords = sorted([i for i in lRecords if i.busId == busId], key=lambda x: x.t)
    if len(busRecords) == 0:
        return None, None
    totDist = 0.0
    for prev_record, curr_record in zip(busRecords[:-1], busRecords[1:]):
        totDist += euclidean_distance(curr_record, prev_record)
    totTime = busRecords[-1].t - busRecords[0].t
    return totDist, totTime


def computeLineAvgSpeed(lRecords, lineId):
    lRecordsFiltered = [i for i in lRecords if i.lineId == lineId]
    busSet = set([i.busId for i in lRecordsFiltered])
    if len(busSet) == 0:
        return 0.0
    totDist = 0.0
    totTime = 0.0
    for busId in busSet:
        d, t = computeBusDistanceTime(lRecordsFiltered, busId)
        totDist += d
        totTime += t
    return totDist / totTime


if __name__ == '__main__':

    lRecords = loadAllRecords(sys.argv[1])
    if sys.argv[2] == '-b':
        print('%s - Total Distance:' % sys.argv[3], computeBusDistanceTime(lRecords, sys.argv[3])[0])
    elif sys.argv[2] == '-l':
        print('%s - Avg Speed:' % sys.argv[3], computeLineAvgSpeed(lRecords, sys.argv[3]))
    else:
        raise KeyError()