import csv
import numpy as np
from dataclasses import dataclass

data = []
csv_reader = csv.reader(open("attendee_locations.csv"))
for line in csv_reader:
    data.append(line)
    
@dataclass
class City:
    city: str
    country: str
    attendee: int
    lat: float
    lon: float
    
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
    
    def __init__(self,city,country,N,lat,lon):
        self.city = city
        self.country = country
        self.N = N
        self.lat = lat
        self.lon = lon
        
    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError

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
