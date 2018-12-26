#Naive o(n^2) memory o(1) Find Two Numbers that Adds up to "n" 
def findTwoSum(arr, value):
  for i in range(len(arr)):
    member = value - arr[i]
    for j in range(i+1, len(arr), 1):
      if(arr[j]== member):
        return [arr[i], arr[j]]
  return []
print(findTwoSum([1,3], 4))

#-----------------------------------------------
#Given an array of integers and a value, determine if there are
# any two integers in the array which sum equal to the given value.
#Using dictionary - O(n) and memory O(n)
def find_sum_two(v, val):
    found_values = set()
    for a in v:
        if val - a in found_values:
            return True # or return [a, val-a]
        found_values.add(a)
    return False

def test(v, val, expected):
    output = find_sum_two(v, val)
    print("exist(v," + str(val) + ") = " + str(output) + "\n")
    assert expected == output

v = [2, 1, 8, 4, 7, 3]
test(v, 3, True)
test(v, 20, False)
test(v, 1, False)
test(v, 2, False)
test(v, 7, True)

#----------------------------------------------
# O(n) if array is sorted other wise O(nlogn) because you need to sort them first, memory O(1).
#This solution works if data is sorted
def find_sum_of_two_2(v, val):
    i = 0
    j = len(v) - 1
    while i < j:
        s = v[i] + v[j]
        if s == val:
            return True
        if s < val:
            i += 1
        else:
            j -= 1
    return False

def test2(v, val, expected):
    v = sorted(v)
    output = find_sum_of_two_2(v, val)
    print("exist2(v, " + str(val) + ") = " + str(output) + "\n")
    assert expected == output


v = [2, 1, 8, 4, 7, 3]
test2(v, 3, True)
test2(v, 20, False)
test2(v, 1, False)
test2(v, 2, False)
test2(v, 7, True)
