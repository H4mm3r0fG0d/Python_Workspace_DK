import random
import time

class Ship:
    def __init__(self, mmsi, name, latitude, longitude, speed, course):
        self.mmsi = mmsi
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.course = course

class AISMessage:
    def __init__(self, ship):
        self.ship = ship

    def generate_position_report(self):
        position_report = f"!AIVDM,1,1,,A,18{self.ship.mmsi},0,5,{self.ship.latitude},{self.ship.longitude},{self.ship.speed},{self.ship.course},0"
        return position_report

class AISTransponder:
    def __init__(self, ship):
        self.ship = ship
        self.message = AISMessage(ship)

    def broadcast_position_report(self):
        print(self.message.generate_position_report())

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
        for transponder in transponders:
            transponder.broadcast_position_report()
            time.sleep(5)


if __name__ == "__main__":
    main()