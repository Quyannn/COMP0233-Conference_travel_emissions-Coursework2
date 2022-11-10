from typing import Dict, List
import math

class City:
    def __init__(self,city:str,country:str,attendee:int,lat:float,lon:float):
        self.city  = city
        self.country = country
        self.attendee = attendee
        self.lat, self.lon = lat, lon
        
        # Validate the infomation
        if not isinstance(city,str) or city == '':
            raise ValueError('City should be a string.')
        if not isinstance(country,str) or country =='':
            raise ValueError('Country should be a string.')
        if not isinstance(attendee, int) or attendee < 0:
            raise ValueError('Attendee should be a positive integer.')
        if not isinstance(lat,float) or lat > 90 or lat < -90:
            raise ValueError('Latitude should be a float in [-90,90].')
        if not isinstance(lon,float) or lon > 180 or lon < -180:
            raise ValueError('Longitude should be a float in [-180,180].')
            
    # The function to compute distance between two cities.
    def distance_to(self, other: 'City') -> float:
        R = 6371
        lat_departure = self.lat
        lat_destination = other.lat
        lon_departure = self.lon
        lon_destination = other.lon
        distance = 2 * R * math.asin(math.sqrt(math.pow(math.sin((lat_destination-lat_departure)/2), 2))+
                                     math.cos(lat_departure) * math.cos(lat_destination) * 
                                     math.pow(math.sin((lon_destination-lon_departure)/2),2))
                                              
        return distance                                      

    # The function to compute CO2 estimation
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

