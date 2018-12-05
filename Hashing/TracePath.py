# Given a HashMap with all the points, find the starting point
# and print out the complete path from start to end
# input is a HashMap
# map = {
# "NewYork" -> "Chicago"
# "Boston" -> "Texas"
# "Missouri" -> "NewYork"
# "Texas" -> "Missouri"
# }

# Output: "Boston->Texas , Texas->Missouri , Missouri->NewYork ,
# NewYork->Chicago, "

# Create a reverse Map of given map i.e if given map has (N,C) then
# reverse map will have (C,N) as key value pair
# Traverse original map and see if corresponding key exist
# in reverse Map
# If it doesn't exist then we found our starting point.
# After starting point is found, simply trace the complete
# path from original map.
def tracePath(map):
    result = ""
    reverseMap = dict()
    #To fill reverse map, iterate through the given map
    keys = list(map.keys())
    for x in range(len(keys)):
        reverseMap[map.get(keys[x])] = keys[x]
    #Find the starting point of itinerary
    from_loc = ""
    for i in range(len(keys)):
        if (not keys[i] in reverseMap):
            from_loc = keys[i]
            break
	#Trace complete path
    to = map.get(from_loc)
    while (to != None):
        result += from_loc + "->" + to + ", "
        from_loc = to
        to = map.get(to)
    return result

map = {
    "NewYork":"Chicago",
    "Boston" : "Texas",
    "Missouri" : "NewYork",
    "Texas" : "Missouri"}
result = tracePath(map)
print(result)
# Output:Boston->Texas, Texas->Missouri, Missouri->NewYork, NewYork->Chicago