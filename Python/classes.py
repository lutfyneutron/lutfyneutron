""""
class Point():
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY


p = Point(2, 5)
print(p.x)
print(p.y)
"""


class Flight():
    def __init__(self, capacity):
        self.capasicy = capacity
        self.passengers = []

    def add_passenges(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capasicy - len(self.passengers)


flight = Flight(4)
peoples = ["Harry", "Ron", "Hermione", "Ginny", "Voldemort"]
for person in peoples:
    if flight.add_passenges(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seat for {person}")
    print(f"Available sets is {flight.open_seats()}")
