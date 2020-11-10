#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # store source and destination value
    trip = {}
    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    # create list to hold next route
    route = []

    next_route = trip["NONE"]
    # while the next is not None
    while next_route != "NONE":
        # append to the destination to next route
        route.append(next_route)
        # change value of the next route
        next_route = trip[next_route]

    route.append("NONE")

    return route
