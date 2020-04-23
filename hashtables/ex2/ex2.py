#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    

    # put tickets array in hashtable
    for tix in tickets:
        hash_table_insert(hashtable, tix.source, tix.destination)
    # find 1st flight in route
    #     first_flight = hash_table_retrieve(tickets_hash, tix.source == "None")
    # # add it to the route array
    #     route.append(first_flight)
    route = []
    dest = hash_table_retrieve(hashtable, 'NONE')

    # while the val of i location is not None, get the i-1th location and append to route
    while dest != 'NONE':
        route.append(dest)
        dest = hash_table_retrieve(hashtable, dest)
    return route