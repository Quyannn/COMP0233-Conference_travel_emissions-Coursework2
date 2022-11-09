from typing import Dict, List
import csv
import numpy as np
import utils
from utils import validate_all_info

data = []
csv_reader = csv.reader(open("attendee_locations.csv"))
for line in csv_reader:
    data.append(line)
#print(data[1][1])

class City:
    
    def __init__(self,city,country,attendee,lat,lon):
        '''
        if city == '' or not isinstance(city,str):
            raise ValueError('Invalid city name, it should be a string.')
            
        if country == '' or not isinstance(country,str):
            raise ValueError('Invalid country name, it should be a string.')
            
        if atttendee 
        if lat > 90 or lat < -90
        '''
        utils.validate_all_info(city,country,attendee,lat,lon)
        self.city  = city
        self.country = country
        self.attendee = attendee
        self.lat, self.lon = lat, lon
    

    
    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError
        
city1 = City(data[1][3], data[1][1], data[1][0], data[1][4], data[1][5])
print(city1)

'''
class CityCollection:
    ...

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions() -> List[City]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError
'''
