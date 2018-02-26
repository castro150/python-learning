class Airplane(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.classes = {}
        self.seats = 0
        self.revenue = 0

    def add_class(self, airplane_class):
        self.classes[airplane_class.name] = airplane_class
        self.seats += airplane_class.seats

    def available_classes(self):
        return {
            name: airplane_class for name, airplane_class in self.classes.iteritems() if airplane_class.seats > 0
        }.keys()

    def print_classes(self):
        for name, airplane_class in self.classes.iteritems():
            print name + ': ' + str(airplane_class.price)

    def book_seat(self, airplane_class_name):
        if self.seats > 0 and self.classes[airplane_class_name].book_seat():
            self.seats -= 1
            self.revenue += self.classes[airplane_class_name].price
            return True
        return False


class AirplaneClass(object):
    def __init__(self, name, seats, price):
        self.name = name
        self.seats = seats
        self.price = price

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            return True
        return False


def sell(plane):
    print '\n\nDear passenger, for our flight from {} to {}, we have that classes: '.format(plane.origin, plane.destination)
    plane.print_classes()
    print 'We have available tickets for this classes: '
    for airplane_class in plane.available_classes():
        print airplane_class
    buy = raw_input('Each one did you want to buy?')
    plane.book_seat(buy)
    print 'Thanks! Here your ticket'

    print '\n\nActual revenue: ' + str(plane.revenue) + '\n\n'

    if raw_input('Another passenger? (y/n)').lower().startswith('y'):
        sell(plane)


def run():
    plane = Airplane('BH', 'SP')
    class1 = AirplaneClass('First', 1, 100)
    class2 = AirplaneClass('Second', 2, 50)
    class3 = AirplaneClass('Third', 7, 10)
    plane.add_class(class1)
    plane.add_class(class2)
    plane.add_class(class3)
    sell(plane)

run()
