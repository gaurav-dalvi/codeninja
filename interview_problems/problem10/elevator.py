import datetime

time_taken_per_floor = 20

class status():
    IDLE = 0
    IN_TRANSIT = 1
    OUT_OF_ORDER = 2
    MAINTENANCE = 3

class direction():
    UP = 0
    DOWN = 1

class elevator(object):

    MAX_FLOOR = 10
    MIN_FLOOR = 0

    def __init__(self, name, current_floor, direction, status, capacity):
        self.name = name
        self.current_floor = current_floor
        self.direction = direction
        self.status = 0
        self.capacity = capacity
        self.transit_start_time = 0
        self.transit_source = None
        self.transit_destination = None
        self.destination_time = None

    def set_time(self,time):
        self.transit_start_time = time

    def set_transit_params(self, source, destination):
        self.current_floor = source
        if source < destination:
            self.direction = direction.UP
        else:
            self.direction = direction.DOWN

        self.transit_source = source
        self.transit_destination = destination
        self.transit_start_time = datetime.datetime.now()
        self.status = status.IN_TRANSIT
        total_floors = self.transit_destination - self.transit_source
        total_time = total_floors * time_taken_per_floor
        self.destination_time = self.transit_start_time + datetime.timedelta(seconds=total_time)

    def reached_destination(self, destination):
        self.status = status.IDLE
        self.current_floor = destination
        self.transit_start_time = None
        self.transit_source = None
        self.transit_destination = None

    def print_elevator_info(self):
        print self.name, self.current_floor, self.status