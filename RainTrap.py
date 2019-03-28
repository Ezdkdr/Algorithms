# a function that takes a list of positive integers as argument. The elements represent the lengths of the towers
# it returns the number of units of water trapped between the towers
#from typing import List, Any


def measure_trapped_water(arr):
    i = 0
    trapped_water_units = 0
    j = len(arr) - 1
    added = True
    while added:
        while i < j and arr[i] == 0:
            i += 1
        while i < j and arr[j] == 0:
            j -= 1
        water_units = j - i + 1
        for k in range(i, j + 1):
            if arr[k] > 0:
                water_units -= 1
                arr[k] -= 1
        if water_units <= 0 or i == j:
            added = False
        else:
            trapped_water_units += water_units
    return trapped_water_units


l = list(input("input the list of items (comma separated): "))  # type: List[Any] # example: 0,1,0,0,2,0,4,0,3,0,0,2,1,0,3,0
print ("The quantity of trapped water units is :", measure_trapped_water(l))
