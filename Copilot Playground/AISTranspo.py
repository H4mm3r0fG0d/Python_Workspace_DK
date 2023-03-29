import random
import time
import math

class Ship:
    def __init__(self, mmsi, name, latitude, longitude, speed, course):
        self.mmsi = mmsi
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.course = course

    def update_position(self, time_diff):
        # calculate new latitude and longitude based on speed and course
        distance = self.speed * time_diff / 3600  # distance traveled in nautical miles
        bearing = math.radians(90 - self.course)  # bearing in radians
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.asin(math.sin(lat1) * math.cos(distance/6371) + math.cos(lat1) * math.sin(distance/6371) * math.cos(bearing))
        lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(distance/6371) * math.cos(lat1), math.cos(distance/6371) - math.sin(lat1) * math.sin(lat2))
        self.latitude = math.degrees(lat2)
        self.longitude = math.degrees(lon2)
class AISMessage:
    def __init__(self, ship):
        self.ship = ship

    def generate_position_report(self):
        position_report = f"!AIVDM, 1, 1,, A, Ship MMSI:18{self.ship.mmsi}, 0, 5, {self.ship.latitude}, {self.ship.longitude}, {self.ship.speed}, {self.ship.course}, 0"
        return position_report

class AISTransponder:
    def __init__(self, ship):
        self.ship = ship
        self.message = AISMessage(ship)

    def broadcast_position_report(self):
        print(self.message.generate_position_report())

    def update_and_broadcast_position_report(self, time_diff):
        self.ship.update_position(time_diff)
        self.broadcast_position_report()

def random_ship():
    mmsi = random.randint(100000000, 999999999)
    name = f"Ship-{mmsi}"
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    speed = round(random.uniform(0, 25), 1)
    course = round(random.uniform(0, 360), 1)

    return Ship(mmsi, name, latitude, longitude, speed, course)

def main():
    ships = [random_ship() for _ in range(5)]

    transponders = [AISTransponder(ship) for ship in ships]

    while True:
        start_time = time.time()

        for transponder in transponders:
            transponder.update_and_broadcast_position_report(5)
            
        time_diff = time.time() - start_time
        if time_diff < 5:    
            time.sleep(5 - time_diff)
        else:
            print("Warning: Processing time exceeded 5 seconds")

if __name__ == "__main__":
    main()