from elevator import elevator
from elevator import status
from elevator import direction
import sys
import datetime
from time import sleep

time_taken_for_passenger = 10

class elevator_manager(object):

    def __init__(self, elevators):
        self.elevators = elevators

    def choose_elevator(self, current_floor, desired_floor):
        print 'User wants to go %s %s' % (current_floor, desired_floor)

        chosen_elevator = self.find_closest_idle_elevator(current_floor)
        if chosen_elevator == None:
            # Find if any valid transit elevator
            chosen_elevator = self.find_earliest_moving_elevator()
            print 'sleeping for %s' % ((chosen_elevator.destination_time - datetime.datetime.now()).seconds())
            sleep((chosen_elevator.destination_time - datetime.datetime.now()).seconds())

        chosen_elevator.set_transit_params(current_floor, desired_floor)

        self.print_status(elevators)
        #print 'chosen_elevator is %s' % (chosen_elevator)
        return chosen_elevator

    def find_earliest_moving_elevator(self):
        #user_direction = self.get_user_direction(user_current_floor, user_desired_floor)

        earliest_elevator = None
        earliest_time = sys.maxsize

        for elevator in elevators:
            if elevator.status == status.IN_TRANSIT:
                # if elevator is going in same direction
                if elevator.destination_time < earliest_time:
                    earliest_time = elevator.destination_time
                    earliest_elevator = elevator

        return earliest_elevator;

    def get_user_direction(self, source, destination):
        if source < destination:
            user_direction = direction.UP
        else:
            user_direction = direction.DOWN

        return user_direction

    def find_closest_idle_elevator(self, user_current_floor):
        nearest_elevator =  None
        nearest_distance = sys.maxsize

        for elevator in self.elevators:
            if elevator.status == status.IDLE:
                if abs(elevator.current_floor - user_current_floor) < nearest_distance:
                    nearest_distance = abs(elevator.current_floor - user_current_floor)
                    nearest_elevator = elevator

        return nearest_elevator


    def print_status(self,elevators):
        for item in elevators:
            print item.name, item.current_floor, item.status, item.transit_source, item.transit_destination


if __name__ == '__main__':

    A = elevator('A', elevator.MIN_FLOOR, direction.UP, status.IDLE,10)
    B = elevator('B', elevator.MIN_FLOOR, direction.UP, status.IDLE,10)
    C = elevator('C', elevator.MIN_FLOOR, direction.UP, status.IDLE, 10)


    elevators = [A,B,C]
    e = elevator_manager(elevators)

    # user A wants to go to 5th floor from 0th floor
    e.choose_elevator(0,5)

    # user B wants to go to 5th floor from 3rd floor
    e.choose_elevator(3, 5)