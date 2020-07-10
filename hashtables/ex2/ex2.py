#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    #prepopulate list with length of tickets
    route=[None]*length

    destination_lookup = {}

    #loop through and store destination
    for ticket in tickets:
        destination_lookup[ticket.source] = ticket.destination

    #build chain starting with source = NONE
    next_destination = destination_lookup["NONE"]

    #look up ticket destinations
    # and add it to destinations array
    # stop when destination = NONE
    for current in range (0,length):
        route[current] = next_destination

        next_destination = destination_lookup[next_destination]

    return route
