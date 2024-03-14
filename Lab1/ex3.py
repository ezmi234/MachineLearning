'''
A text file contains information on a group of people born in a given year. The format is the following:
<name> <surname> <birthplace> <birthdate>
The first three fields are strings (with no blanks), <birthdate> is a string with format DD/MM/YYYY/
Each line corresponds to a person, and births are not sorted. Write a program that computes
• The number of births for each city
• The number of births for each month
• The average number of births per city (number of births over number of cities)
Example:
Mario Rossi Torino 02/03/2019
Franca Valeri Asti 10/05/2019
Marco Verdi Torino 05/04/2019
Giancarlo Magalli Torino 01/06/2019
Giovanna Bianchi Asti 10/03/2019
The program should output (in no particular order)
Births per city:
Torino: 3
Asti: 2
Births per month:
March: 2
April: 1
May: 1
June: 1
Average number of births: 2.50
'''

mapOfMonths = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


if __name__ == '__main__':
    cities = {}
    months = {}
    with open("ex3_data.txt", "r") as f:
        for line in f:
            elements = line.split()
            if elements[2] not in cities:
                cities[elements[2]] = 1
            else:
                cities[elements[2]] += 1
            month = int(elements[3].split("/")[1])
            if month not in months:
                months[month] = 1
            else:
                months[month] += 1

    print("Births per city:")
    for k in cities.keys():
        print("{}: {}".format(k, cities[k]))
    print("Births per month:")
    for k in months:
        print("{}: {}".format(mapOfMonths.get(k), months[k]))
    print("Average number of births: {}".format(
        sum(cities.values())/len(cities)
    ))

