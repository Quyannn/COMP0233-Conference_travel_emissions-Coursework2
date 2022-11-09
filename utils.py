from cities import City, CityCollection

def read_attendees_file(filepath: str) -> CityCollection:
    raise NotImplementedError

def is_pos_int(attendee):
    return isinstance(attendee, int) and attendee > 0

def is_valid_location(lat, lon):
    return -90 <= lat <= 90 and -180 <= lon <= 180

def is_valid_city(city):
    return isinstance(city, str)

def is_valid_country(country):
    return isinstance(country, str)

def is_valid_state(state):
    return isinstance(state, str)

def validate_all_info(attendee,country,city,lat,lon):
    #Validate the infomation input.
    if not is_pos_int(attendee):
        raise ValueError("Attendee should be a positive integer.")
    if not is_valid_country(country):
        raise ValueError("Country should be a string.")
    if not is_valid_city(city):
        raise ValueError("City should be a string.")
    if not is_valid_location(lat, lon):
        raise ValueError("Latitude should in [-90,90] and longitude should in [-180,180].")
