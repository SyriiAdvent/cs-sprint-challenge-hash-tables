#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):# O(2n)
    cache = {}
    route = []
    # preload cache O(n) still even with a next for loop
    for i in range(length):
        start = tickets[i].source
        end = tickets[i].destination
        cache[start] = end
        # if we find the starting ticket, insert it.
        if start == 'NONE':
            route.insert(0, end)
    for i in range(length):
        if route[i] in cache and route[i] != 'NONE':
            route.append(cache.get(route[i]))

    print(cache)
    # print(route)
    return route


# ticket_6 = Ticket("LAX", "SFO")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_10 = Ticket("BHM", "FLG")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_1 = Ticket("PIT", "ORD")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_5 = Ticket("NONE", "LAX")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
# print(reconstruct_trip(tickets, 10))