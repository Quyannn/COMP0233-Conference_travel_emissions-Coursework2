from cities import City, CityCollection
from pathlib import Path
import csv


filepath = Path("attendee_locations.csv")


def read_attendees_file(filepath) -> CityCollection:
    data = []
    csv_reader = csv.reader(open(filepath))
    for line in csv_reader:
        data.append(line)
    
    return data[1:]


citydata = read_attendees_file(filepath)
#print(citydata[1][0])
city1 = City(citydata[1][3],citydata[1][1],int(citydata[1][0]),float(citydata[1][4]),float(citydata[1][5]))
city2 = City(citydata[56][3],citydata[56][1],int(citydata[56][0]),float(citydata[56][4]),float(citydata[56][5]))
distance_12 = city1.distance_to(city2)
