def max(list):
    if(len(list) == 2):
        return list[0] if list[0] > list[1] else list[1]

    sub_Max = max(list[1:])
    return list[0] if list[0]>sub_Max else sub_Max

print(max([1,2,3,6,5,4,10]))